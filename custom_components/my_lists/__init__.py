"""My Lists - Checklist and mileage tracking for Home Assistant."""
from __future__ import annotations

import os
import voluptuous as vol
from homeassistant.components import frontend
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .store import MyListsStore
from .websocket import async_register_websocket

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.Schema({})},
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up My Lists from configuration.yaml."""
    store = MyListsStore(hass)
    await store.async_load()
    hass.data[DOMAIN] = store

    # Register websocket API
    async_register_websocket(hass)

    # Register panel
    panel_dir = os.path.join(os.path.dirname(__file__), "frontend")
    await hass.http.async_register_static_paths(
        [StaticPathConfig("/my_lists", panel_dir, False)]
    )

    frontend.async_register_built_in_panel(
        hass,
        component_name="iframe",
        sidebar_title="My Lists",
        sidebar_icon="mdi:clipboard-check",
        frontend_url_path="my-lists",
        config={"url": "/my_lists/index.html"},
        require_admin=False,
    )

    return True
