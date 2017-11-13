#!/usr/bin/env Python
#
# Vulnhub Writeups
# Written by Timtohy Loftus (baffoon)
#
# Synopsis:
# This will be the larger of all of the repositories. This contains automation and
# explaination for all of the Vulnhub VMs that I finish. Full documentation of these
# writeups will reside in the docs/ directory at the root of The CTF Journal.

def vulnhubMenu():
    """This is the menu containing the Vulnhub Virtual Machines that I've finished."""

    title = "\nVulnhub Virtual Machine - Writeups\n"
    title += "Written by Timothy Loftus (baffoon)\n\n"
    title += "This is the larger repository. Every Vulnhub machine that I finish will\n"
    title += "be here. If an automation script hasn't been written, then explaination\n"
    title += "will be given. Full documentation/writeups will be provided in the docs/\n"
    title += "directory.\n\n"
    title += "Vulnhub Virtual Machine Index:\n\n"

    vulnhubVMLst = [
    "1. Mr. Robot: 1",
    "2. Xerxes: 1",
    "3. Metasploitable: 2.0",
    "4. RickdiculouslyEasy: 1",
    "5. Ew_Skuzzy: 1",
    ]

    print (title)
    for vm in vulnhubVMLst:
        print (vm)

def vulnhubMain():
    """This will be used to handle the vulnub machine menu."""
    while 1:
        vulnhubMenu()
        vulnhubMenuInput = input ("\n[ ctf-journal ][ vulnhub-vms ] > ")
        if str(vulnhubMenuInput) == "1":
            break
        elif str(vulnhubMenuInput) == "2":
            break
        elif str(vulnhubMenuInput) == "3":
            break
        elif str(vulnhubMenuInput) == "4":
            break
        elif str(vulnhubMenuInput) == "5":
            break
        elif str(vulnhubMenuInput).lower() == "quit" or "exit" or "":
            break
