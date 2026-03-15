"""WebSocket API for My Lists."""
from __future__ import annotations

import voluptuous as vol
from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN, EVENT_LISTS_UPDATED


def async_register_websocket(hass: HomeAssistant) -> None:
    """Register websocket commands."""
    websocket_api.async_register_command(hass, ws_get_state)
    websocket_api.async_register_command(hass, ws_create_list)
    websocket_api.async_register_command(hass, ws_update_list)
    websocket_api.async_register_command(hass, ws_delete_list)
    websocket_api.async_register_command(hass, ws_reorder_lists)
    websocket_api.async_register_command(hass, ws_duplicate_list)
    websocket_api.async_register_command(hass, ws_add_item)
    websocket_api.async_register_command(hass, ws_update_item)
    websocket_api.async_register_command(hass, ws_toggle_item)
    websocket_api.async_register_command(hass, ws_delete_item)
    websocket_api.async_register_command(hass, ws_move_item)
    websocket_api.async_register_command(hass, ws_copy_item)
    websocket_api.async_register_command(hass, ws_clear_done)
    websocket_api.async_register_command(hass, ws_uncheck_all)
    websocket_api.async_register_command(hass, ws_add_sub_item)
    websocket_api.async_register_command(hass, ws_toggle_sub_item)
    websocket_api.async_register_command(hass, ws_delete_sub_item)
    websocket_api.async_register_command(hass, ws_add_fuel_entry)
    websocket_api.async_register_command(hass, ws_update_fuel_entry)
    websocket_api.async_register_command(hass, ws_delete_fuel_entry)
    websocket_api.async_register_command(hass, ws_create_backup)
    websocket_api.async_register_command(hass, ws_get_backups)
    websocket_api.async_register_command(hass, ws_restore_backup)
    websocket_api.async_register_command(hass, ws_set_setting)


async def _save_and_notify(hass: HomeAssistant) -> None:
    """Save and fire update event."""
    store = hass.data[DOMAIN]
    await store.async_save()
    hass.bus.async_fire(EVENT_LISTS_UPDATED, {"state": store.get_state()})


# === State ===

@websocket_api.websocket_command({vol.Required("type"): "my_lists/get_state"})
@callback
def ws_get_state(hass, connection, msg):
    """Get full state."""
    store = hass.data[DOMAIN]
    connection.send_result(msg["id"], store.get_state())


# === Lists ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/create_list",
    vol.Required("name"): str,
    vol.Optional("icon", default="📋"): str,
    vol.Optional("color", default="#4CAF50"): str,
    vol.Optional("list_type", default="standard"): str,
})
@websocket_api.async_response
async def ws_create_list(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.create_list(msg["name"], msg["icon"], msg["color"], msg["list_type"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/update_list",
    vol.Required("list_id"): str,
    vol.Optional("name"): str,
    vol.Optional("icon"): str,
    vol.Optional("color"): str,
})
@websocket_api.async_response
async def ws_update_list(hass, connection, msg):
    store = hass.data[DOMAIN]
    kwargs = {k: msg[k] for k in ("name", "icon", "color") if k in msg}
    result = store.update_list(msg["list_id"], **kwargs)
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/delete_list",
    vol.Required("list_id"): str,
})
@websocket_api.async_response
async def ws_delete_list(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.delete_list(msg["list_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/reorder_lists",
    vol.Required("list_ids"): [str],
})
@websocket_api.async_response
async def ws_reorder_lists(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.reorder_lists(msg["list_ids"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/duplicate_list",
    vol.Required("list_id"): str,
})
@websocket_api.async_response
async def ws_duplicate_list(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.duplicate_list(msg["list_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


# === Items ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/add_item",
    vol.Required("list_id"): str,
    vol.Required("text"): str,
    vol.Optional("image"): str,
})
@websocket_api.async_response
async def ws_add_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.add_item(msg["list_id"], msg["text"], msg.get("image"))
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/update_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
    vol.Optional("text"): str,
    vol.Optional("done"): bool,
    vol.Optional("image"): str,
})
@websocket_api.async_response
async def ws_update_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    kwargs = {k: msg[k] for k in ("text", "done", "image") if k in msg}
    result = store.update_item(msg["list_id"], msg["item_id"], **kwargs)
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/toggle_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
})
@websocket_api.async_response
async def ws_toggle_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.toggle_item(msg["list_id"], msg["item_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/delete_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
})
@websocket_api.async_response
async def ws_delete_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.delete_item(msg["list_id"], msg["item_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/move_item",
    vol.Required("from_list"): str,
    vol.Required("to_list"): str,
    vol.Required("item_id"): str,
})
@websocket_api.async_response
async def ws_move_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.move_item(msg["from_list"], msg["to_list"], msg["item_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/copy_item",
    vol.Required("from_list"): str,
    vol.Required("to_list"): str,
    vol.Required("item_id"): str,
})
@websocket_api.async_response
async def ws_copy_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.copy_item(msg["from_list"], msg["to_list"], msg["item_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/clear_done",
    vol.Required("list_id"): str,
})
@websocket_api.async_response
async def ws_clear_done(hass, connection, msg):
    store = hass.data[DOMAIN]
    count = store.clear_done(msg["list_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"cleared": count})


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/uncheck_all",
    vol.Required("list_id"): str,
})
@websocket_api.async_response
async def ws_uncheck_all(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.uncheck_all(msg["list_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


# === Sub-items ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/add_sub_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
    vol.Required("text"): str,
    vol.Optional("image"): str,
})
@websocket_api.async_response
async def ws_add_sub_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.add_sub_item(msg["list_id"], msg["item_id"], msg["text"], msg.get("image"))
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/toggle_sub_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
    vol.Required("sub_id"): str,
})
@websocket_api.async_response
async def ws_toggle_sub_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.toggle_sub_item(msg["list_id"], msg["item_id"], msg["sub_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/delete_sub_item",
    vol.Required("list_id"): str,
    vol.Required("item_id"): str,
    vol.Required("sub_id"): str,
})
@websocket_api.async_response
async def ws_delete_sub_item(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.delete_sub_item(msg["list_id"], msg["item_id"], msg["sub_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


# === Fuel entries ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/add_fuel_entry",
    vol.Required("list_id"): str,
    vol.Required("date"): str,
    vol.Optional("station", default=""): str,
    vol.Optional("grade", default=""): str,
    vol.Optional("address", default=""): str,
    vol.Optional("costPerL", default=0): vol.Coerce(float),
    vol.Required("liters"): vol.Coerce(float),
    vol.Required("curKm"): vol.Coerce(float),
    vol.Required("prevKm"): vol.Coerce(float),
})
@websocket_api.async_response
async def ws_add_fuel_entry(hass, connection, msg):
    store = hass.data[DOMAIN]
    entry_data = {k: msg[k] for k in ("date", "station", "grade", "address", "costPerL", "liters", "curKm", "prevKm")}
    result = store.add_fuel_entry(msg["list_id"], entry_data)
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/update_fuel_entry",
    vol.Required("list_id"): str,
    vol.Required("entry_id"): str,
    vol.Required("date"): str,
    vol.Optional("station", default=""): str,
    vol.Optional("grade", default=""): str,
    vol.Optional("address", default=""): str,
    vol.Optional("costPerL", default=0): vol.Coerce(float),
    vol.Required("liters"): vol.Coerce(float),
    vol.Required("curKm"): vol.Coerce(float),
    vol.Required("prevKm"): vol.Coerce(float),
})
@websocket_api.async_response
async def ws_update_fuel_entry(hass, connection, msg):
    store = hass.data[DOMAIN]
    entry_data = {k: msg[k] for k in ("date", "station", "grade", "address", "costPerL", "liters", "curKm", "prevKm")}
    result = store.update_fuel_entry(msg["list_id"], msg["entry_id"], entry_data)
    await _save_and_notify(hass)
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/delete_fuel_entry",
    vol.Required("list_id"): str,
    vol.Required("entry_id"): str,
})
@websocket_api.async_response
async def ws_delete_fuel_entry(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.delete_fuel_entry(msg["list_id"], msg["entry_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": True})


# === Backups ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/create_backup",
    vol.Optional("auto", default=False): bool,
    vol.Optional("changes", default=""): str,
})
@websocket_api.async_response
async def ws_create_backup(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.create_backup(msg["auto"], msg["changes"])
    await store.async_save()
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({vol.Required("type"): "my_lists/get_backups"})
@callback
def ws_get_backups(hass, connection, msg):
    store = hass.data[DOMAIN]
    connection.send_result(msg["id"], store.get_backups())


@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/restore_backup",
    vol.Required("backup_id"): str,
})
@websocket_api.async_response
async def ws_restore_backup(hass, connection, msg):
    store = hass.data[DOMAIN]
    result = store.restore_backup(msg["backup_id"])
    await _save_and_notify(hass)
    connection.send_result(msg["id"], {"success": result})


# === Settings ===

@websocket_api.websocket_command({
    vol.Required("type"): "my_lists/set_setting",
    vol.Required("key"): str,
    vol.Required("value"): vol.Any(str, int, float, bool, None),
})
@websocket_api.async_response
async def ws_set_setting(hass, connection, msg):
    store = hass.data[DOMAIN]
    store.set_setting(msg["key"], msg["value"])
    await store.async_save()
    connection.send_result(msg["id"], {"success": True})
