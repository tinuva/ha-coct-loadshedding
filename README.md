# CoCT Loadshedding Interface

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![maintainer][maintenance-shield]][maintainer]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

This is a simple component to integrate with the CoCT Loadshedding API and provide [loadshedding](https://en.wikipedia.org/wiki/South_African_energy_crisis)-related status information.
Forked from [swartjean/ha-coct-loadshedding](swartjean/ha-coct-loadshedding) and [tiaanv/ha-eskom-loadshedding]](tiaanv/ha-eskom-loadshedding)

This integration exposes a sensor for the current stage of loadshedding. It also calculates the loadshedding schedule for COCT and can provide a sensor indicating if the selected Area is currently in loadshedding, as well as when the next loadshedding slot for the selected area will be. This depends of course on the current loadshedding stage.

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show loadshedding status information.

**This component will create the following sensors.**

Sensor | Description
-- | --
`sensor.coct_loadshedding_stage` | Show Current Loadshedding Stage from CoCT API (Numeric).
`sensor.coct_loadshedding_load_shedding_active` | Is the configured Area currently in loadshedding (True/False).
`sensor.coct_loadshedding_next_load_shedding` | When the next scheduled loadshedding for the area will take place (DateTime).

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `coct_loadshedding`.
4. Download _all_ the files from the `custom_components/coct_loadshedding/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "CoCT Loadshedding Interface"

## Configuration is done in the UI

1. Configure the Scan Period (update frequency in seconds). Default is 900s.
2. Configure the Area as per COCT map.

NOTE: Long refresh rates kan delay the change of the sensor, as the current implementation does not run on ZERO hour, and refresh times are dependent on startup time. This generally is not an issue in practice. It just seems erratic if you are monitoring the sensor(s).

<!---->

[buymecoffee]: https://www.buymeacoffee.com/tinuva
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/tinuva/ha-coct-loadshedding.svg?style=for-the-badge
[commits]: https://github.com/tinuva/ha-coct-loadshedding/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/tinuva/ha-coct-loadshedding.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%20%40tinuva-blue.svg?style=for-the-badge
[maintainer]: https://github.com/tinuva
[releases-shield]: https://img.shields.io/github/v/release/tinuva/ha-coct-loadshedding?style=for-the-badge
[releases]: https://github.com/tinuva/ha-coct-loadshedding/releases
