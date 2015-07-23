#!/usr/bin/env python
from pylight import QLight
from collections import OrderedDict
from argparse import ArgumentParser

if __name__ == '__main__' and __package__ is None:

    PARSER = ArgumentParser(description="control a Q-Light warning tower.  "
                            "All lamps should have red, yellow and green "
                            "lights available.  Blue and white lights may or "
                            "may not be available depending on exact model.",
                            epilog="Written by Chris Jowett, cryptk@gmail.com")
    PARSER.add_argument("-r", "--red", help="Desired state of red lamp.",
                        type=str, nargs='?', default='pass')
    PARSER.add_argument("-y", "--yellow", help="Desired state of yellow lamp.",
                        type=str, nargs='?', default='pass')
    PARSER.add_argument("-g", "--green", help="Desired state of green lamp.",
                        type=str, nargs='?', default='pass')
    PARSER.add_argument("-b", "--blue", help="Desired state of blue lamp.",
                        type=str, nargs='?', default='pass')
    PARSER.add_argument("-w", "--white", help="Desired state of white lamp.",
                        type=str, nargs='?', default='pass')
    PARSER.add_argument("-a", "--all-lights", help="State of all lamps.",
                        type=str, nargs='?')
    PARSER.add_argument("-t", "--tone", help="Desired tone to play.",
                        type=str, nargs='?', default='pass',
                        choices=['off',
                                 'tone_1',
                                 'tone_2',
                                 'tone_3',
                                 'tone_4',
                                 'tone_5',
                                 'pass'])
    PARSER.add_argument("-d", "--duration",
                        help="Duration to play tone (in ms).",
                        type=int, nargs='?')
    ARGS = PARSER.parse_args()
    QL = QLight()
    if ARGS.all_lights is not None:
        QL.set_all_lights(ARGS.all_lights)
    else:
        QL.lights = OrderedDict([
            ('red', ARGS.red),
            ('yellow', ARGS.yellow),
            ('green', ARGS.green),
            ('blue', ARGS.blue),
            ('white', ARGS.white)
            ])
        QL.update_lamp()
    if ARGS.duration is not None:
        QL.set_sound(ARGS.tone, ARGS.duration)
    else:
        QL.set_sound(ARGS.tone)
