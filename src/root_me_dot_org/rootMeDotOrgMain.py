#!/usr/bin/env python
#
# root-me.org Writeups
# Written by Timothy Loftus
#

challengeScore = 115

def rootMeDotOrgMenu():
    """Menu for the root-me.org challenge writeups"""

    title = "\nRoot-me.org Challenge - Writeups\n"
    title += "Written by Timothy Loftus (baffoon)\n\n"
    title += "This section will contain all of the writeups for the various challenges\n"
    title += "at root-me.org. There are many different types of challenges, but I will\n"
    title += "only show the ones that I have touched. I will also show my current score for\n"
    title += "the overall challange below:\n\n"

    score = "Current Score: {} pts".format(str(challengeScore))

    intro = "\n\nBelow is the index of challenge categories:\n\n"

    challengeCategoriesLst = [
    "1. App - Script",
    "2. Cryptanalysis",
    "3. Forensic",
    "4. Network",
    "5. Web - Client",
    "6. Web - Server",
    ]

    print (title)
    print (score)
    print (intro)
    for challCat in challengeCategoriesLst:
        print (challCat)

def rootMeDotOrgMain():
    """Main for the root-me.org challenge categories."""
    while True:
        rootMeDotOrgMenu()
        rootMeDotOrgCatInput = input("\n[ ctf-journal ][ root-me.org ] > ")
        if str(rootMeDotOrgCatInput) == "1":
            break
        elif str(rootMeDotOrgCatInput) == "2":
            break
        elif str(rootMeDotOrgCatInput) == "3":
            break
        elif str(rootMeDotOrgCatInput) == "4":
            break
        elif str(rootMeDotOrgCatInput) == "5":
            break
        elif str(rootMeDotOrgCatInput) == "6":
            break
        elif str(rootMeDotOrgCatInput) == "quit" or "exit" or "":
            break
