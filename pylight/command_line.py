#!/usr/bin/env python
from pylight import QLight
from collections import OrderedDict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def main():
    parser = ArgumentParser(description="control a Q-Light warning tower.  "
                            "All lamps should have red, yellow and green "
                            "lights available.  Blue and white lights may or "
                            "may not be available depending on exact model.",
                            epilog="Written by Chris Jowett, cryptk@gmail.com",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    lights = parser.add_argument_group('Light Controls', 'Valid states are '
                                       '"off", "on", "blink", "pass"')
    light_choices = ['off','on','blink','pass']
    lights.add_argument("-r", "--red", help="Desired state of red lamp.",
                        type=str, nargs='?', default='pass', metavar='STATE',
                        choices=light_choices)
    lights.add_argument("-y", "--yellow", help="Desired state of yellow lamp.",
                        type=str, nargs='?', default='pass', metavar='STATE',
                        choices=light_choices)
    lights.add_argument("-g", "--green", help="Desired state of green lamp.",
                        type=str, nargs='?', default='pass', metavar='STATE',
                        choices=light_choices)
    lights.add_argument("-b", "--blue", help="Desired state of blue lamp.",
                        type=str, nargs='?', default='pass', metavar='STATE',
                        choices=light_choices)
    lights.add_argument("-w", "--white", help="Desired state of white lamp.",
                        type=str, nargs='?', default='pass', metavar='STATE',
                        choices=light_choices)
    lights.add_argument("-a", "--all-lights", help="State of all lamps.",
                        type=str, nargs='?', metavar='STATE',
                        choices=light_choices)
    tone = parser.add_argument_group('Tone Controls', 'valid tone options are '
                                     '"off", "tone_1", "tone_2", "tone_3", '
                                     '"tone_4", "tone_5", "pass"')
    tone.add_argument("-t", "--tone", help="Desired tone to play.",
                        type=str, nargs='?', metavar='TONE', default='pass',
                        choices=['off',
                                 'tone_1',
                                 'tone_2',
                                 'tone_3',
                                 'tone_4',
                                 'tone_5',
                                 'pass'])
    tone.add_argument("-d", "--duration",
                        help="Duration to play tone (in ms).",
                        type=int, nargs='?', default=0)
    args = parser.parse_args()
    ql = QLight()
    if args.all_lights is not None:
        ql.set_all_lights(args.all_lights)
    else:
        ql.lights = OrderedDict([
            ('red', args.red),
            ('yellow', args.yellow),
            ('green', args.green),
            ('blue', args.blue),
            ('white', args.white)
            ])
        ql.update_lamp()
    if args.tone:
        ql.set_sound(args.tone, args.duration)
