#!/usr/bin/env python3
#
# CTF Journal
# Author: Timothy Loftus (baffoon)
# Date Created: 06/04/2017
#

from core.cjcore import *
from entries.otw.bandit import *

while True:
    try:
        print(banner)
        print(mainMenu)

        userInput = input("{}[ctf-journal] > {}".format(bcolors.GREEN, bcolors.ENDC))

        if str(userInput) == '1':

            while True:
                print(menuCTFsWargames)
                menuCTFWGsInput = input("{}[ctf-journal]:[CTFs/Wargames] > {}".format(bcolors.GREEN, bcolors.ENDC))

                if menuCTFWGsInput == '1':

                    while True:
                        print(menuOverTheWireBandit)
                        menuOTWBanditInput = input("{}[ctf-journal]:[Wargames]:[otw bandit] > {}".format(bcolors.GREEN, bcolors.ENDC))

                        if str(menuOTWBanditInput) == '0':

                            print("This is where Level 0 is supposed to go.")

                        elif str(menuOTWBanditInput) == '1':

                           banditLvl0ToLvl1Solution(user[0], host, port, passwd[0])

                        elif str(menuOTWBanditInput) == '2':

                            print("Hm. No entry for Level 1 --> Level 2 yet... It's a whitch!")

                        elif str(menuOTWBanditInput) == '3':

                            print("Well that's unfortunate. No Level 2 --> Level 3 yet. Sad face.")

                        elif str(menuOTWBanditInput) == '4':

                            print("No level 3 --> Level 4 yet. The haxor must have been captured.")

                        elif str(menuOTWBanditInput) == '5':

                            print("No Level 4 --> Level 5. As a wise man once said, \"Do better!\"")

                        elif str(menuOTWBanditInput) == '6':

                            print("No Level 5 --> Level 6. The Nobel Derp Prize goes to... The Dev!")

                        elif str(menuOTWBanditInput) == 'q' or 'quit':

                            print("Going back to previous menu...")
                            break

                elif menuCTFWGsInput == 'q' or 'quit':
                    print("\n\nThank you for reading... Bye bye!\n")
                    break

        elif str(userInput) == '2':

            while True:
                print(menuIVMs)
                menuIVMsInput = input("{}[ctf-journal]:[IVMs] > {}".format(bcolors.GREEN, bcolors.ENDC))

                if str(menuIVMsInput) == 'q' or 'quit':

                    print("\n\nThank you for reading... Bye bye!\n")
                    break
                else:
                    break

        elif str(userInput) == 'q' or 'exit':
            print("\n\nThank you for reading... Bye bye!\n")
            break

    except KeyboardInterrupt as KbInt:
        print("\n\nThank you for reading... Bye bye!\n")
        break
