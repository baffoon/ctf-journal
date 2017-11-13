#!/usr/bin/env python
#
# SANS Holiday Hack Challenge 2016 Writeup
# File: sanshh2016.py
# Written by Timothy Loftus (baffoon)
#



def sansHolidayHack2016Menu():
    """Menu for SANs Holiday Hack Challenge 2016 writeup menu."""
    title = "\nSANS Holiday Hack Challenge 2016 - Writeup:\n\n"
    title += "Anything that I can write up in a Python script will be in this portion\n"
    title += "of the CTF Journal. As time goes on, more will be added. Full write up\n"
    title += "can be found in the docs/ directory. If automation can't be used, description\n"
    title += "will be provided.\n"

    sansHolidayHack2016Lst = [
    "1. Part 1: A Most Curious Business Card",
    "2. Part 2: Awesome Package Konveyance",
    "3. Part 3: A Fresh Baked Holiday Pi",
    "4. Part 4: My Gosh... It's full of Holes!",
    "5. Part 5: Discombobulated Audio"
    ]

    print (title)
    for chall in sansHolidayHack2016Lst:
        print (chall)

def sansHolidayHack2016Main():
    """Main handler for for SANs Holiday Hack Challenge 2016 Menu"""
    while 1:
        sansHolidayHack2016Menu()
        sansHolidayHack2016MainInput = input("\n[ ctf-journal ][ SANS_Holiday_Hack_Chall_2016 ] > ")
        if str(sansHolidayHack2016MainInput) == "1":
            break
        elif str(sansHolidayHack2016MainInput) == "2":
            break
        elif str(sansHolidayHack2016MainInput) == "3":
            break
        elif str(sansHolidayHack2016MainInput) == "4":
            break
        elif str(sansHolidayHack2016MainInput) == "5":
            break
        elif str(sansHolidayHack2016MainInput) == "quit" or "exit" or "":
            break
