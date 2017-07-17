#!/usr/bin/python
#
# An attempt to clean up the code for bandit.py
# As you can tell, this code looks poorly written. This will be
# merged into the new bandit.py.

#import paramiko

host = "bandit.labs.overthewire.org"
port = 2220

users = [
        'bandit0',
        'bandit1',
        'bandit2',
        'bandit3',
        'bandit4',
        'bandit5',
        'bandit6',
        'bandit7',
        'bandit8',
        'bandit9',
        'bandit10',
        ]

passwds = [
        'bandit0',
        'boJ9jbbUNNfktd78OOpsqOltutMc3MY1',
        'CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9',
        'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK',
        'pIwrPrtPN36QITSp3EQaw936yaFoFgAB',
        'koReBOKuIDDepwhWk7jZC0RTdopnAYKh',
        ]

otwBanditMenu = """
OverTheWire - Bandit Entries:

This is the menu for the WarGame Bandit, provided by OverTheWire. Below
you may navite through the entiries:

0. Level 0
1. Level 0 --> Level 1
2. Level 1 --> Level 2
3. Level 2 --> Level 3
4. Level 3 --> Level 4
5. Level 4 --> Level 5
"""

