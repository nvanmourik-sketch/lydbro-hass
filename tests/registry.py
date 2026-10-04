"""Device-registry lookup that works across HA versions.

HA 2026.8 added ``async_get_device_by_identifier``; from 2026.9 the old
``async_get_device`` raises under test (and is removed in 2027.8). The
suite has to pass on both sides of that line, like the integration does.
"""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr

from custom_components.lydbro.const import DOMAIN

DEVICE_MAC = "aa:bb:cc:dd:ee:ff"


def lydbro_device(hass: HomeAssistant, config_entry_id: str) -> dr.DeviceEntry | None:
    """Return the registered Lydbro One device for the config entry."""
    registry = dr.async_get(hass)
    identifier = (DOMAIN, DEVICE_MAC)
    if hasattr(registry, "async_get_device_by_identifier"):
        return registry.async_get_device_by_identifier(identifier, config_entry_id)
    return registry.async_get_device(identifiers={identifier})
