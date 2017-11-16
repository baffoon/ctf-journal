#!/usr/bin/env python
#
# Over The Wire - Bandit Writeup
# File Name: otw-bandit.py
# Written by Timothy Loftus (baffoon)
#

import paramiko

host = "bandit.labs.overthewire.org"
port = 2220
client = paramiko.SSHClient()
autoAddPolicySSH = paramiko.AutoAddPolicy()
sshPolicy = client.set_missing_host_key_policy(autoAddPolicySSH)

users = [
    "bandit0",
    "bandit1",
    "bandit2",
    "bandit3",
    "bandit4",
    "bandit5",
]

passwds = {
    "bandit0":"bandit0",
    "bandit1":"boJ9jbbUNNfktd78OOpsqOltutMc3MY1",
    "bandit2":"",
    "bandit3":"",
    "bandit4":"",
    "bandit5":"",
}

def otwBanditLevel0():
    """Solution for Level 0"""
    print ("\nOverTheWire - Bandit - Level 0")
    print ("Written by Timothy Loftus (baffoon)")
    print ("\nDescription:")
    print ("\nThis is the first challenge for OverTheWire Bandit. This is merely an initiation,")
    print ("to see if you are able to SSH into the wargame.\n")
    print ("Level Goal:\n")
    print ("The goal of this level is for you to log into the game using SSH. The host to which you")
    print ("need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and")
    print ("the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.\n")
    print ("Usefull Commands:\n")
    print ("ssh\n")

    print ("Initializing script now...")

    sshPolicy

    print ("\n[*] Configuring the SSH policy to the AutoAddPolicy.")

    print ("\n[*] Connecting with the following parameters:\n")
    print ("[*] Server: {}".format(host))
    print ("[*] Port: {}".format(str(port)))
    print ("[*] Username: {}".format(users[0]))

    client.connect(
        host,
        port=port,
        username=users[0],
        password=passwds[str(users[0])]
        )

    stdin, stdout, stderr = client.exec_command("ls -la")

    print ("[*] Using ls -la to read the directory contents.")

    print ("[*] Results from the command:\n")

    for band0Output in stdout:
        print ("[*] " + band0Output)

    print ("[*] Looks as though there is a file named 'readme'. Let's read what it says.")

    print ("[*] Executing cat command on the readme file.")

    stdin, stdout, stderr = client.exec_command("cat readme")

    print ("[*] Output of the 'readme' file's contents.")
    print ("[*] The password for the next level is:\n")

    for band0Output in stdout:
        print ("[*] " + band0Output)

    client.close()

def otwBanditLevel0ToLevel1():
    """Solution for Level 0 --> Level 1"""


def otwBanditMenu():
    """Over the Wire - Bandit Menu"""
    title = "\nOver The Wire - Bandit\n"
    title += "Written By Timothy Loftus (baffoon)\n\n"
    title += "These are the challenges for the Bandit. Below are the challenges,\n"
    title += "a majority of the automation is done by using a variety of commands\n"
    title += "through an SSH session. The output will explain the concepts used,\n"
    title += "documentation will also be provided in the docs/ directory.\n\n"
    title += "Over The Wire - Bandit - Solutions:\n\n"

    otwBanditChallLst = [
    "0. Bandit - Level 0",
    "1. Bandit - Level 0 --> Level 1",
    "2. Bandit - Level 1 --> Level 2",
    "3. Bandit - Level 2 --> Level 3",
    "4. Bandit - Level 3 --> Level 4",
    "5. Bandit - Level 4 --> Level 5",
    ]

    print (title)
    print ("Note: Currently unable to connect to bandit. Will continue writing when I can.\n\n")
    for challenge in otwBanditChallLst:
        print (challenge)

def otwBanditMain():
    """Main handler for Over The Wire - Bandit."""
    while True:
        otwBanditMenu()
        otwBanditMenuInput = input("\n[ ctf-journal ][ otw-bandit ] > ")
        if str(otwBanditMenuInput) == "0":
            otwBanditLevel0()
        elif str(otwBanditMenuInput) == "1":
            break
        elif str(otwBanditMenuInput) == "2":
            break
        elif str(otwBanditMenuInput) == "quit" or "exit" or "":
            break
