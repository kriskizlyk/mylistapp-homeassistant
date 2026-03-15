"""Data store for My Lists."""
from __future__ import annotations

import time
import uuid
from datetime import datetime
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import DOMAIN, STORAGE_KEY, STORAGE_VERSION


class MyListsStore:
    """Manage My Lists data."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize."""
        self.hass = hass
        self._store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
        self._data: dict[str, Any] = {"lists": [], "items": {}, "backups": [], "settings": {}}

    async def async_load(self) -> None:
        """Load data from storage."""
        data = await self._store.async_load()
        if data:
            self._data = data

    async def async_save(self) -> None:
        """Save data to storage."""
        await self._store.async_save(self._data)

    @property
    def lists(self) -> list[dict]:
        """Return all lists."""
        return self._data.get("lists", [])

    @property
    def items(self) -> dict[str, list]:
        """Return all items."""
        return self._data.get("items", {})

    @property
    def backups(self) -> list[dict]:
        """Return all backups."""
        return self._data.get("backups", [])

    @property
    def settings(self) -> dict:
        """Return settings."""
        return self._data.get("settings", {})

    def _now_iso(self) -> str:
        """Return current time as ISO string."""
        return datetime.now().isoformat()

    def _gen_id(self, prefix: str = "") -> str:
        """Generate a unique ID."""
        return f"{prefix}{uuid.uuid4().hex[:12]}"

    # === List operations ===

    def create_list(self, name: str, icon: str = "📋", color: str = "#4CAF50", list_type: str = "standard") -> dict:
        """Create a new list."""
        new_list = {
            "id": self._gen_id("lst_"),
            "name": name,
            "icon": icon,
            "color": color,
            "type": list_type,
            "createdAt": self._now_iso(),
        }
        self._data["lists"].append(new_list)
        self._data["items"][new_list["id"]] = []
        return new_list

    def update_list(self, list_id: str, **kwargs) -> dict | None:
        """Update list properties."""
        for lst in self._data["lists"]:
            if lst["id"] == list_id:
                for key, val in kwargs.items():
                    if key in ("name", "icon", "color"):
                        lst[key] = val
                return lst
        return None

    def delete_list(self, list_id: str) -> bool:
        """Delete a list and its items."""
        self._data["lists"] = [l for l in self._data["lists"] if l["id"] != list_id]
        self._data["items"].pop(list_id, None)
        return True

    def reorder_lists(self, list_ids: list[str]) -> bool:
        """Reorder lists by ID order."""
        id_map = {l["id"]: l for l in self._data["lists"]}
        self._data["lists"] = [id_map[lid] for lid in list_ids if lid in id_map]
        return True

    def duplicate_list(self, list_id: str) -> dict | None:
        """Duplicate a list with all items."""
        source = None
        for lst in self._data["lists"]:
            if lst["id"] == list_id:
                source = lst
                break
        if not source:
            return None
        new_list = self.create_list(
            name=source["name"] + " (Copy)",
            icon=source["icon"],
            color=source["color"],
            list_type=source.get("type", "standard"),
        )
        # Deep copy items
        source_items = self._data["items"].get(list_id, [])
        new_items = []
        for item in source_items:
            new_item = {**item, "id": self._gen_id("itm_")}
            if "subItems" in item:
                new_item["subItems"] = [
                    {**si, "id": self._gen_id("sub_")} for si in item["subItems"]
                ]
            new_items.append(new_item)
        self._data["items"][new_list["id"]] = new_items
        return new_list

    # === Item operations ===

    def add_item(self, list_id: str, text: str, image: str | None = None) -> dict | None:
        """Add an item to a list."""
        if list_id not in self._data["items"]:
            return None
        item = {
            "id": self._gen_id("itm_"),
            "text": text,
            "done": False,
            "subItems": [],
            "createdAt": self._now_iso(),
        }
        if image:
            item["image"] = image
        self._data["items"][list_id].append(item)
        return item

    def update_item(self, list_id: str, item_id: str, **kwargs) -> dict | None:
        """Update an item."""
        for item in self._data["items"].get(list_id, []):
            if item["id"] == item_id:
                for key, val in kwargs.items():
                    if key in ("text", "done", "image"):
                        item[key] = val
                return item
        return None

    def toggle_item(self, list_id: str, item_id: str) -> dict | None:
        """Toggle item done state."""
        for item in self._data["items"].get(list_id, []):
            if item["id"] == item_id:
                item["done"] = not item["done"]
                return item
        return None

    def delete_item(self, list_id: str, item_id: str) -> bool:
        """Delete an item."""
        items = self._data["items"].get(list_id, [])
        self._data["items"][list_id] = [i for i in items if i["id"] != item_id]
        return True

    def move_item(self, from_list: str, to_list: str, item_id: str) -> bool:
        """Move an item between lists."""
        items = self._data["items"].get(from_list, [])
        item = None
        for i in items:
            if i["id"] == item_id:
                item = i
                break
        if not item:
            return False
        self._data["items"][from_list] = [i for i in items if i["id"] != item_id]
        new_item = {**item, "id": self._gen_id("itm_"), "createdAt": self._now_iso()}
        if to_list not in self._data["items"]:
            self._data["items"][to_list] = []
        self._data["items"][to_list].append(new_item)
        return True

    def copy_item(self, from_list: str, to_list: str, item_id: str) -> bool:
        """Copy an item to another list."""
        items = self._data["items"].get(from_list, [])
        item = None
        for i in items:
            if i["id"] == item_id:
                item = i
                break
        if not item:
            return False
        new_item = {
            "id": self._gen_id("itm_"),
            "text": item["text"],
            "done": False,
            "subItems": [],
            "createdAt": self._now_iso(),
        }
        if to_list not in self._data["items"]:
            self._data["items"][to_list] = []
        self._data["items"][to_list].append(new_item)
        return True

    def clear_done(self, list_id: str) -> int:
        """Clear all completed items and sub-items."""
        items = self._data["items"].get(list_id, [])
        count = len([i for i in items if i.get("done")])
        self._data["items"][list_id] = [
            {**i, "subItems": [s for s in i.get("subItems", []) if not s.get("done")]}
            for i in items if not i.get("done")
        ]
        return count

    def uncheck_all(self, list_id: str) -> bool:
        """Uncheck all items and sub-items."""
        for item in self._data["items"].get(list_id, []):
            item["done"] = False
            for sub in item.get("subItems", []):
                sub["done"] = False
        return True

    # === Sub-item operations ===

    def add_sub_item(self, list_id: str, item_id: str, text: str, image: str | None = None) -> dict | None:
        """Add a sub-item."""
        for item in self._data["items"].get(list_id, []):
            if item["id"] == item_id:
                sub = {
                    "id": self._gen_id("sub_"),
                    "text": text,
                    "done": False,
                    "createdAt": self._now_iso(),
                }
                if image:
                    sub["image"] = image
                if "subItems" not in item:
                    item["subItems"] = []
                item["subItems"].append(sub)
                return sub
        return None

    def toggle_sub_item(self, list_id: str, item_id: str, sub_id: str) -> dict | None:
        """Toggle sub-item done state."""
        for item in self._data["items"].get(list_id, []):
            if item["id"] == item_id:
                for sub in item.get("subItems", []):
                    if sub["id"] == sub_id:
                        sub["done"] = not sub["done"]
                        return sub
        return None

    def delete_sub_item(self, list_id: str, item_id: str, sub_id: str) -> bool:
        """Delete a sub-item."""
        for item in self._data["items"].get(list_id, []):
            if item["id"] == item_id:
                item["subItems"] = [s for s in item.get("subItems", []) if s["id"] != sub_id]
                return True
        return False

    # === Mileage operations ===

    def add_fuel_entry(self, list_id: str, entry_data: dict) -> dict | None:
        """Add a fuel entry."""
        if list_id not in self._data["items"]:
            return None
        entry = {
            "id": self._gen_id("fue_"),
            **entry_data,
            "createdAt": self._now_iso(),
        }
        self._data["items"][list_id].append(entry)
        return entry

    def update_fuel_entry(self, list_id: str, entry_id: str, entry_data: dict) -> dict | None:
        """Update a fuel entry."""
        items = self._data["items"].get(list_id, [])
        for i, item in enumerate(items):
            if item["id"] == entry_id:
                items[i] = {**item, **entry_data}
                return items[i]
        return None

    def delete_fuel_entry(self, list_id: str, entry_id: str) -> bool:
        """Delete a fuel entry."""
        items = self._data["items"].get(list_id, [])
        self._data["items"][list_id] = [i for i in items if i["id"] != entry_id]
        return True

    # === Backup operations ===

    def create_backup(self, auto: bool = False, changes: str = "") -> dict:
        """Create a backup snapshot."""
        import copy
        backup = {
            "id": self._gen_id("bak_"),
            "createdAt": self._now_iso(),
            "auto": auto,
            "changes": changes,
            "lists": copy.deepcopy(self._data["lists"]),
            "items": copy.deepcopy(self._data["items"]),
        }
        self._data["backups"].append(backup)
        # Keep max 20 auto-backups
        if auto:
            auto_backups = [b for b in self._data["backups"] if b.get("auto")]
            if len(auto_backups) > 20:
                to_remove = auto_backups[:-20]
                remove_ids = {b["id"] for b in to_remove}
                self._data["backups"] = [b for b in self._data["backups"] if b["id"] not in remove_ids]
        return {"id": backup["id"], "createdAt": backup["createdAt"], "auto": auto, "changes": changes}

    def get_backups(self) -> list[dict]:
        """Get backup summaries."""
        result = []
        for b in sorted(self._data["backups"], key=lambda x: x.get("createdAt", ""), reverse=True):
            num_lists = len(b.get("lists", []))
            num_items = sum(len(v) for v in b.get("items", {}).values())
            result.append({
                "id": b["id"],
                "createdAt": b["createdAt"],
                "auto": b.get("auto", False),
                "changes": b.get("changes", ""),
                "numLists": num_lists,
                "numItems": num_items,
            })
        return result[:25]

    def restore_backup(self, backup_id: str) -> bool:
        """Restore from a backup."""
        import copy
        for b in self._data["backups"]:
            if b["id"] == backup_id:
                self._data["lists"] = copy.deepcopy(b["lists"])
                self._data["items"] = copy.deepcopy(b["items"])
                return True
        return False

    # === Settings ===

    def set_setting(self, key: str, value: Any) -> None:
        """Set a setting."""
        if "settings" not in self._data:
            self._data["settings"] = {}
        self._data["settings"][key] = value

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting."""
        return self._data.get("settings", {}).get(key, default)

    # === Full state for frontend ===

    def get_state(self) -> dict:
        """Get full state for frontend."""
        return {
            "lists": self._data["lists"],
            "items": self._data["items"],
            "settings": self._data.get("settings", {}),
        }
