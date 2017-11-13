#!/usr/bin/env python

def miscMenu():
    """
    Menu for Misc nick nacks of things that I have found useful in various situations.
    Anything can be included in this section that I feel like. Just a place for me to
    put random tools and what not.
    """
    title = "\nMisc aka Random Stuff\n"
    title += "Note: Writters will be included in the script's headers.\n"
    title += "This section of The CTF Journal contains little scripts that may prove\n"
    title += "useful in other CTFs/Wargames. User input is a requirement in these scripts.\n"
    title += "The usefulness of the script must be determined in order for it to be implemented.\n\n"
    title += "If improvements can be made, submit an issue to GitHub. This section is intended\n"
    title += "to be the for the community. Have fun!\n\n"

    miscMenuLst = [
    "1. Encoders",
    "2. Decoders",
    ]

    print (title)
    for lstitem in miscMenuLst:
        print (lstitem)

def miscMain():
    """Main handler for the Misc menu."""
    while 1:
        miscMenu()
        miscMenuInput = input("\n[ ctf-journal ][ misc ] > ")
        if str(miscMenuInput) == "1":
            break
        elif str(miscMenuInput) == "2":
            break
        elif str(miscMenuInput) == "quit" or "exit" or "":
            break
