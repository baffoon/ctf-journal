#!/usr/bin/python
#
# CTF Journal
# Author: Timothy Loftus (baffoon)
# Date Created: 06/04/2017
#

def menu():
    """Menu for the program"""
    title = "\nThe CTF Journal\n"
    title += "By Timothy Loftus (baffoon)\n\n"
    title += "The CTF Journal is a repository of all of the CTFs that I part take in. If\n"
    title += "write any scripts for a challenge they can be found in the entries, with\n"
    title += "details on how the challenge was finished. If not, the details will still be\n"
    title += "present.\n\n"
    title += "Choose a CTF by entering its coresponding number in the list. To quit, press\n"
    title += "ENTER or type 'quit' or 'exit'.\n"

    ctfLst = [
    "1. OverTheWire",
    "2. SANS Holiday Hack Challenge 2016",
    "3. Defense Point Security CTF"
    "4. root-me.org",
    "5. Vulnhub",
    "0. Misc."
    ]
    print (title)
    for ctf in ctfLst:
        print (ctf)

def main():
    """Main for the program"""
    while 1:
        menu()
        ctfInput = input("\n[ ctf-journal ] > ")
        if str(ctfInput) == 'quit' or "exit" or "":
            break


main()
