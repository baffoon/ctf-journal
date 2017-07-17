#!/usr/bin/python
#
# Script Name: cj-core.py
# Author: Timothy Loftus (baffoon)
# Date Created: 07/04/2017
#
# Currently this file is mostly for colors.

import os

# OS check, currently for colors.

def is_windows():
    return os.name() == 'nt'

def is_nix():
    return os.name() == 'posix'
#
# Some pretty colors.
#

class bcolors:
    GREEN = '\033[1;92m'
    RED = '\033[1;91m'
    CYAN = '\033[1;36m'
    MAGENTA = '\033[1;36m'
    ENDC = '\033[0m'

    def disable(self):
        self.GREEN = ''
        self.RED = ''
        self.CYAN = ''
        self.MAGENTA = ''
        self.ENDC = ''

# The banner
# For the banners and menus used during user navigation.
banner = (bcolors.GREEN) + r"""
    _______________________________
    \_   ___ \__    ___/\_   _____/
    /    \  \/ |    |    |    __)
    \     \____|    |    |     \
     \______  /|____|    \___  /
            \/               \/
         ____.                                 .__
        |    | ____  __ _________  ____ _____  |  |
        |    |/  _ \|  |  \_  __ \/    \ \_  \ |  |
    /\__|    (  <_> )  |  /|  | \/   |  \/ __ \|  |__
    \________|\____/|____/ |__|  |___|  (____  /____/
                                       \/     \/
    """ + (bcolors.ENDC)
banner += "\n\t{}CTF Journal{}\n".format(bcolors.RED, bcolors.ENDC)
banner += "\n{}Author:{} {}Timothy Loftus (baffoon){}".format(bcolors.RED, bcolors.ENDC, bcolors.GREEN, bcolors.ENDC)
banner += """
\n{}The CTF Journal has two purposes:{}

1. To act as a reason for teaching myself how to code in Python.
2. Document CTFs that I've finished with that code.

I started this project a while ago. It's intended to act as an excuse to
learn automation and exploit development. As one looks through the entries,
they will notice documentation for CTFs, Intentionally Vulnerable Machines,
exploits, and misc. (Random crap) that I've done. Navigate to where you want
to go and read as you may.

To navigate throughout the CTF Journal, enter the number.

[If you wish to quit either type \'q\', \'quit\', or \'Ctr-C\'.]
""".format(bcolors.GREEN, bcolors.ENDC)

# Main menu
menuMain = """
{}Choose your poison from the menu:{}

1. Capture the Flag (CTFs) and Wargames
2. Intentiionally Vulnerable Machines (IVMs)
""".format(bcolors.GREEN, bcolors.ENDC)

# Secondary menus
menuCTFsWargames = """
\nCTFs and Wargames:

This is where you'll fiind my write-ups for CTFs and Wargames that I've completed.
These are either automated scripts (for proof of concept) or just simple text explaining
the process of completing the challenge.

Press enter to go back to the main menu.

CTFs and Wargames are listed below:

1. OverTheWire - Bandit (WG)
"""

menuIVMs = """
\nIntentionally Vulnerable Machiness:

These moduless are write-ups for Intentionally Vulnerable Machines (IVMs) that I've finished.
These will either be in the form of an automated scripte, for proof of concept along with
explaination of the process behind completing the challenge.

To go back to main menu just press enter with nothing at the prompt.

Note: Content is lacking due to poor and slow development. Bear with me.
"""

def reportStatus(message):
    print ((bcolors.GREEN) + ("[*]") + (bcolors.ENDC) + str(message))

def reportErr(errorMess):
    print ((bcolors.RED) + ("[!]") + (bcolors.ENDC) + str(errorMess))

def mainMenu(banner, menu):
    print banner
    print menu

def secondaryMenu(menu):
    print menu

def thirdMenu(menu):
    print menu
