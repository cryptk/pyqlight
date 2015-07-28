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
import hid

from collections import OrderedDict
from time import sleep


class QLight(object):

    """Create and control a QLight.

    Please see __init__() docscrings for further details.
    """

    def __init__(self):
        """Initialize the QLight class.

        Attributes:
            lights (OrderedDict): A list of all lights and the state that they
            have been set to.  The valid states are:

                    off: The light is off.
                    on: The light is on.
                    blink: The light alternates between off and on.
                    pass: The light has not had a state set, and it will
                        maintain it's previous state on updates.

                All lights are initialized to a value of 'pass' because there
                is no known way to poll the light for the current status of the
                lights.

            sound (str): What audio pattern the light is currently playing.
                The exact pattern that is played for the 5 different tones
                varies depending on the model.  The valid states are:

                    off: No sound is playing.
                    tone_1: The first tone is playing.
                    tone_2: The second tone is playing.
                    tone_3: The third tone is playing.
                    tone_4: The fourth tone is playing.
                    tone_5: The fifth tone is playing.
                    pass: The light has not had an audio tone set, whatever
                        tone it is already playing will continue to play.

                The sound is initialized to a value of 'pass' because there is
                no known way to poll the light for the current status of the
                audio.
        """
        self._light_states = {
            'off': '00',
            'on': '01',
            'blink': '02',
            'pass': '64'
            }
        self.lights = OrderedDict([
            ('red', 'pass'),
            ('yellow', 'pass'),
            ('green', 'pass'),
            ('blue', 'pass'),
            ('white', 'pass')
            ])
        self._sound_states = {
            'off': '00',
            'tone_1': '01',
            'tone_2': '02',
            'tone_3': '03',
            'tone_4': '04',
            'tone_5': '05',
            'pass': '64'
            }
        self.sound = 'pass'

        self._usbdev = hid.Device(vid=1240, pid=59196)
        assert self._usbdev is isinstance(hid.Device)

    def update_lamp(self):
        """Generate the hexadecimal state string and update the lamp.

        This string is a 6 byte hexadecimal string (12 characters total).
        Each byte represents (in order):
            - red lamp state
            - yellow lamp state
            - green lamp state
            - blue lamp state
            - white lamp state
            - audio speaker state

        Each of the lamp states can be the following:
            00: lamp is off
            01: lamp is on
            02: lamp is blinking
            All other values will maintain the previous lamp state

        The audio speaker state can be the following:
            00: no tone is played
            01: tone 1 is played
            02: tone 2 is played
            03: tone 3 is played
            04: tone 4 is played
            05: tone 5 is played
            All other values will maintain the previous lamp state.

        This function takes no arguments, rather it references the values in
        self.lights and self.sound which allows for state tracking across
        subsequent commands.
        """
        msg = ''
        for light in self.lights:
            msg += self._light_states.get(
                self.lights.get(light, 'pass'),
                '64')
        msg += self._sound_states.get(self.sound, 'pass')
        self._send_msg(msg)

    def _send_msg(self, msg):
        """Pad a supplied message with a header and footer and delivers it.

        The header consists of two hexadecimal bytes.  The purpose/value of
        these bytes is unknown.

        The footer consists of 8 hexadecimal bytes.  The purpose/value of these
        bytes is unknown.

        Args:
            msg (str): A hexadecimal string containing the desired lamp state.
                Please see update_lamp() for a description of the format of
                this string.
        """
        header = '5700'
        footer = '400054f300000000'
        payload = header+msg+footer
        self._usbdev.write(payload.decode("hex"))

    def set_all_lights(self, state):
        """Set all lights to the same state.

        Args:
            state (str): The desired lamp state.  The valid states are:

                off: The light is off.
                on: The light is on.
                blink: The light alternates between off and on.
                pass: The lights will maintain their previous states.
        """
        for light in self.lights:
            self.lights[light] = state
        self.update_lamp()

    def set_light(self, color, state, clear_prev_states=False):
        """Set a lamp to a desired state.

        Sets a selected lamp to the desired state, optionally clearing all
        other lamps at the same time.

        Args:
            color (str): Which lamp to alter.  Availability of lamp colors
            varies depending on specific lamp model.  Valid lamp colors are:
                - red
                - yellow
                - green
                - blue
                - white

            state (str): What state to set the lamp to.  Valid lamp states are:

                off: The light is off.
                on: The light is on.
                blink: The light alternates between off and on.
                pass: The light will maintain it's previous state.

            clear_prev_state (Optional[bool]): Whether or not to set all other
                lights to off when this light is set to the provided state.
                Default is to preserve the current state of the other lights.
        """
        if clear_prev_states:
            self.set_all_lights('off')
        self.lights[color] = state
        self.update_lamp()

    def set_sound(self, tone, duration=0):
        """Play a tone from the lamp.

        Commands the lamp to play the desired tone, optionally returning to
        silence after a specified duration in milliseconds.

        Args:
            tone (str): Which tone to play.  Valid options are:
                off: Stop all sounds.
                tone_1: Play the first tone.
                tone_2: Play the second tone.
                tone_3: Play the third tone.
                tone_4: Play the fourth tone.
                tone_5: Play the fifth tone.
                pass: Continue to play the current tone.

            duration (Optional[int]): Play the tone for the specified number of
                milliseconds and then silence the audio.  A duration of 0 plays
                the audio forever (I.E. until a subsequent set_audio call),
                this is the default behavior.
        """
        self.sound = tone
        self.update_lamp()
        if duration:
            duration += 350
            sleep(duration/1000.0)
            self.sound = 'off'
            self.update_lamp()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
