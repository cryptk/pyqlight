pyqlight
=======

A python interface for Q-Light warning light towers.  Includes both a module
which can be included as well as a command line utility suitable for one-shot controls.

USAGE
=====
```
usage: pyqlight [-h] [-r [STATE]] [-y [STATE]] [-g [STATE]] [-b [STATE]]
               [-w [STATE]] [-a [STATE]] [-t [TONE]] [-d [DURATION]]

control a Q-Light warning tower. All lamps should have red, yellow and green
lights available. Blue and white lights may or may not be available depending
on exact model.

optional arguments:
  -h, --help            show this help message and exit

Light Controls:
  Valid states are "off", "on", "blink", "pass"

  -r [STATE], --red [STATE]
                        Desired state of red lamp. (default: pass)
  -y [STATE], --yellow [STATE]
                        Desired state of yellow lamp. (default: pass)
  -g [STATE], --green [STATE]
                        Desired state of green lamp. (default: pass)
  -b [STATE], --blue [STATE]
                        Desired state of blue lamp. (default: pass)
  -w [STATE], --white [STATE]
                        Desired state of white lamp. (default: pass)
  -a [STATE], --all-lights [STATE]
                        State of all lamps. (default: None)

Tone Controls:
  valid tone options are "off", "tone_1", "tone_2", "tone_3", "tone_4",
  "tone_5", "pass"

  -t [TONE], --tone [TONE]
                        Desired tone to play. (default: pass)
  -d [DURATION], --duration [DURATION]
                        Duration to play tone (in ms). (default: 0)

Written by Chris Jowett, cryptk@gmail.com
```
