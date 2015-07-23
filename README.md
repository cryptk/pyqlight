pylight
=======

RTFM
====
```
A pure python method to interact with Q-Light warning light towers
usage: wrapper.py [-h] [-r [RED]] [-y [YELLOW]] [-g [GREEN]] [-b [BLUE]]
                  [-w [WHITE]] [-a [ALL_LIGHTS]]
                  [-t [{off,tone_1,tone_2,tone_3,tone_4,tone_5,pass}]]
                  [-d [DURATION]]

control a Q-Light warning tower. All lamps should have red, yellow and green
lights available. Blue and white lights may or may not be available depending
on exact model.

optional arguments:
  -h, --help            show this help message and exit
  -r [RED], --red [RED]
                        Desired state of red lamp.
  -y [YELLOW], --yellow [YELLOW]
                        Desired state of yellow lamp.
  -g [GREEN], --green [GREEN]
                        Desired state of green lamp.
  -b [BLUE], --blue [BLUE]
                        Desired state of blue lamp.
  -w [WHITE], --white [WHITE]
                        Desired state of white lamp.
  -a [ALL_LIGHTS], --all-lights [ALL_LIGHTS]
                        State of all lamps.
  -t [{off,tone_1,tone_2,tone_3,tone_4,tone_5,pass}], --tone [{off,tone_1,tone_2,tone_3,tone_4,tone_5,pass}]
                        Desired tone to play.
  -d [DURATION], --duration [DURATION]
                        Duration to play tone (in ms).

Written by Chris Jowett, cryptk@gmail.com
```
