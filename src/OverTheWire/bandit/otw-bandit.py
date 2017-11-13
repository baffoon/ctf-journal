#!/usr/bin/env python
#
# Over The Wire - Bandit Writeup
# File Name: otw-bandit.py
# Written by Timothy Loftus (baffoon)
#

def otwBanditMenu():
    """Over the Wire - Bandit Menu"""

    title = "\nOver The Wire - Bandit\n"
    title += "Written By Timothy Loftus (baffoon)\n\n"
    title += "These are the challenges for the Bandit. Below are the challenges,\n"
    title += "a majority of the automation is done by using a variety of commands\n"
    title += "through an SSH session. The output will explain the concepts used,\n"
    title += "documentation will also be provided in the docs/ directory.\n\n"
    title += "Over The Wire - Bandit - Solutions:\n\n"

    otwBanditCallLst = [
    "0. Bandit - Level 0",
    "1. Bandit - Level 0 --> Level 1",
    "2. Bandit - Level 1 --> Level 2",
    "3. Bandit - Level 2 --> Level 3",
    "4. Bandit - Level 3 --> Level 4",
    "5. Bandit - Level 4 --> Level 5",
    ]

    print (title)
    for challenge in otwBanditChallLst:
        print (challenge)
