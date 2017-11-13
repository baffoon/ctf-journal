#!/usr/bin/env python
#
# SANS Holiday Hack Challenge 2016 Writeup
# File: sanshh2016.py
# Written by Timothy Loftus (baffoon)
#



def sanshh2016Menu():
    """Menu for SANs Holiday Hack Challenge 2016 writeup menu."""
    title = "\nSANS Holiday Hack Challenge 2016 - Writeup:\n\n"
    title += "Anything that I can write up in a Python script will be in this portion\n"
    title += "of the CTF Journal. As time goes on, more will be added. Full write up\n"
    title += "can be found in the docs/ directory. If automation can't be used, description\n"
    title += "will be provided.\n"

    sanshh2016Lst = [
    "1. Part 1: A Most Curious Business Card",
    "2. Part 2: Awesome Package Konveyance",
    "3. Part 3: A Fresh Baked Holiday Pi",
    "4. Part 4: My Gosh... It's full of Holes!",
    "5. Part 5: Discombobulated Audio"
    ]

    print (title)
    for chall in sanshh2016:
        print (chall)
