#!/usr/bin/python
#
# CTF Journal
# Author: Timothy Loftus (baffoon)
# Date Created: 06/04/2017
#

from src.core import *
from src.entries.otw.bandit import *

while 1:
    mainMenu(str(banner), str(menuMain))
    mainMenuInput = raw_input((bcolors.GREEN) + "[ctf-journal:]> " + (bcolors.ENDC))
    if str(mainMenuInput) == '1':
        while 1:
            secondaryMenu(str(menuCTFsWargames))
            ctfWargameMenuInput = raw_input((bcolors.GREEN) + "[ctf-journal:ctf/wargames]> " + \
                (bcolors.ENDC))
            if str(ctfWargameMenuInput) == '1':
                while 1:
                    thirdMenu(str(otwBanditMenu))
                    otwBanitInput = raw_input((bcolors.GREEN) + "[ctf-journal:ctf/wargames:otw-bandit]> " + \
                        (bcolors.ENDC))
    elif str(mainMenuInput) == '2':
        while 1:
            secondaryMenu(str(menuIVMs))
            ivmMenuInput = raw_input((bcolors.GREEN) + "[ctf-journal:ivms]> " + (bcolors.ENDC))
    else:
        print ("Thank you for reading. Bye bye!")
