# CoCT Loadshedding Interface

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![maintainer][maintenance-shield]][maintainer]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

This is a simple component to integrate with the CoCT Loadshedding API and provide [loadshedding](https://en.wikipedia.org/wiki/South_African_energy_crisis)-related status information.
Forked from [swartjean/ha-coct-loadshedding](swartjean/ha-coct-loadshedding) and [tiaanv/ha-eskom-loadshedding]](tiaanv/ha-eskom-loadshedding)

This integration exposes a sensor for the current stage of loadshedding.

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show loadshedding status information.

{% if not installed %}
## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "CoCT Loadshedding Interface".

{% endif %}

## Configuration is done in the UI

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