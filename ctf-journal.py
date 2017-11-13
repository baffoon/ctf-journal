#!/usr/bin/python
#
# CTF Journal
# Author: Timothy Loftus (baffoon)
# Date Created: 06/04/2017
#

from src.OverTheWire.over_the_wire import overTheWireMain
from src.root_me_dot_org.rootMeDotOrgMain import rootMeDotOrgMain
from src.SANS_Holiday_Hack_2016.sansHolidayHackChallenge2016 import sansHolidayHack2016Main
from src.defense_point_security_ctf.defensePointSecurityCTF import defensePointSecurityMain
from src.Vulnhub.vulnhubWriteups import vulnhubMain
from src.Misc.miscMain import miscMain

def menu():
    """Menu for the program"""

    banner = """
   _____ _            _____ ___________     ___                              _
  |_   _| |          /  __ \_   _|  ___|   |_  |                            | |
    | | | |__   ___  | /  \/ | | | |_        | | ___  _   _ _ __ _ __   __ _| |
    | | | '_ \ / _ \ | |     | | |  _|       | |/ _ \| | | | '__| '_ \ / _` | |
    | | | | | |  __/ | \__/\ | | | |     /\__/ / (_) | |_| | |  | | | | (_| | |
    \_/ |_| |_|\___|  \____/ \_/ \_|     \____/ \___/ \__,_|_|  |_| |_|\__,_|_|
    """

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
    "3. Defense Point Security CTF",
    "4. root-me.org",
    "5. Vulnhub",
    "0. Misc."
    ]

    print (banner)
    print (title)
    for ctf in ctfLst:
        print (ctf)

def main():
    """Main for the program"""
    while 1:
        menu()
        ctfInput = input("\n[ ctf-journal ] > ")
        if str(ctfInput) == "1":
            overTheWireMain()
        if str(ctfInput) == "2":
            sansHolidayHack2016Main()
        if str(ctfInput) == "3":
            defensePointSecurityMain()
        if str(ctfInput) == "4":
            rootMeDotOrgMain()
        if str(ctfInput) == "5":
            vulnhubMain()
        if str(ctfInput) == "0":
            miscMain()
        if str(ctfInput) == "quit" or "exit" or "":
            break

main()
