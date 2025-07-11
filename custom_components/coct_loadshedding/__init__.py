"""
Custom integration to integrate the CoCT Loadshedding Interface with Home Assistant.

For more details about this integration, please refer to
https://github.com/tinuva/ha-coct-loadshedding
"""
import asyncio
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .coct_interface import coct_interface
from .loadshedding_schedule import *

from .const import (
    CONF_SCAN_PERIOD,
    DEFAULT_SCAN_PERIOD,
    CONF_AREA,
    DEFAULT_AREA,
    DOMAIN,
    PLATFORMS,
    STARTUP_MESSAGE,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)

    scan_period = timedelta(
        seconds=entry.options.get(CONF_SCAN_PERIOD, DEFAULT_SCAN_PERIOD)
    )

    coct_area = entry.options.get(CONF_AREA, DEFAULT_AREA)

    coordinator = CoCTDataUpdateCoordinator(hass, scan_period, coct_area)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    #for platform in PLATFORMS:
    #    if entry.options.get(platform, True):
    #        coordinator.platforms.append(platform)
    #        hass.async_add_job(
    #            hass.config_entries.async_forward_entry_setup(entry, platform)
    #        )
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    if not entry.update_listeners:
        entry.add_update_listener(async_reload_entry)

    return True


class CoCTDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(self, hass, scan_period, coct_area):
        """Initialize."""
        self.api = coct_interface()
        self.platforms = []

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=scan_period)
        self.coct_area = int(coct_area)

    async def _async_update_data(self):
        """Update data via library."""
        try:
            data = await self.api.async_get_data(self.coct_area)
            return data.get("data", {})
        except Exception as exception:
            raise UpdateFailed(exception)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Handle removal of an entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
                if platform in coordinator.platforms
            ]
        )
    )

    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
