#!/usr/bin/env python

def defensePointSecurityMenu():
    """
    The menu for the Defense Point Security CTF.

    Note: These Challenges no longer exist. So only descriptions will be provided.
          Not to mention, I haven't finished all of the challenges.
    """

    title = "\nDefense Point Security CTF - Writeups\n"
    title += "Written by Timothy Loftus (baffoon)\n\n"
    title += "These writeups will contain descriptions on how I solved the Defense\n"
    title += "Point Security CTF challenges. The full writeup can be found in the docs/\n"
    title += "directory. As of the last time that I've looked for this, Nov. 13, 2017,\n"
    title += "these challenges no longer exist. Hope they come back at some point.\n\n"

    defensePointSecurityMenuCatLst = [
    "1. Memory Challenges",
    "2. Security Policy",
    ]

    print (title)
    for category in defensePointSecurityMenuCatLst:
        print (category)

def defensePointSecurityMain():
    """Man handler for the Defense Point Security CTF writeups."""
    while True:
        defensePointSecurityMenu()
        defensePointSecurityCTFInput = input("[ ctf-journal ][ dps-ctf ] > ")
        if str(defensePointSecurityCTFInput) == "1":
            break
        elif str(defensePointSecurityCTFInput) == "2":
            break
        elif str(defensePointSecurityCTFInput) == "quit" or "exit" or "":
            break
