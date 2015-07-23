#!/usr/bin/env python
"""Python module to control Q-Light warning towers.

This module allows for a pure python interface to control a single Q-Light
warning tower.

Limitations:
    If more than one lamp is connected to the system, there is no way to
    determine which one you are addressing.  Without a second lamp to test
    with, I cannot reliably add this functionality.

    There is no way to poll the light for it's current state that I can
    determine.  This appears to be a limitation of the Q-Lights themselves.
"""

from pylight import QLight
