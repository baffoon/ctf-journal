#!/usr/bin/env python
#
# Over The Wire - Writeups
# File Name: over-the-wire.py
# Written by Timothy Loftus (baffoon)
#

def overTheWireMenu():
    """The over the wire menu."""
    title = "\nOver The Wire Writeups\n\n"
    title += "Here are all of the automation scripts and descriptions for the\n"
    title += "Over The Wire war games. Full writeups can be found in the docs/\n"
    title += "directory.\n\n"
    title += "The Over The Wire Wargames:\n\n"

    overTheWireWargames = [
    "1. Over The Wire - Bandit",
    ]

    print (title)
    for wargame in overTheWireWargames:
        print (wargame)
