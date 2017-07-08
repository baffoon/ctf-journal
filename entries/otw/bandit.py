#!/usr/bin/env python3
#
# otw-bandit.py
# Author: Timothy Loftus (baffoon)
# Date Created: 06/04/2017
#
# Note: Code will be cleaned up in due time. Just attempting to make things
#       work for now.
#

import paramiko
#import ../../core.bcolors

user = [
        'bandit0','bandit1','bandit2',
        ]
passwd = [
        'bandit0',
        '',
        ]
host = "bandit.labs.overthewire.org"
port = 2220

class bcolors:
    GREEN = '\033[1;92m'
    RED = '\033[1;91m'
    ENDC = '\033[0m'

    def disable(self):
        self.GREEN = ''
        self.RED = ''
        self.ENDC = ''

# Create something for testing the connection.
def banditConnectionTest():
    """
    This function is used to test the connection for bandit. Will use the
    bandit0 user to connect to connect to the server over a custom port
    (2220).
    """
    fqdn = "bandit.labs.overthewire.org"
    port = 2220

    client = paramiko.SSHClient() # Creating the ssh client.

    # Making ssh obtain the host key automatically via AutoAddPolicy.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Attempting connection to bandit, return 1 if success.
        client.connect(
                fqdn,
                port=port,
                username=user[0],
                password=passwd[0])

        return 1

    # Return 0 for bad host key.
    except paramiko.BadHostKeyException as BadHostKey:
        return 0

    # Return 0 for ssh error.
    except paramiko.SSHException as SSHErr:
        return 0

    # Return 0 for bad internet connection.
    except paramiko.socket.error as BadSocket:
        return 0

    client.close() # Closing the connection.

def banditLvl0Solution(user, hostname, port, passwd):
    """
    Solution:
    Wargame: OverTheWire - Bandit
    Level 0

    This is the initiation level. All you have to do in this challenge is
    login as the bandit0 user via ssh. This is like the connection test. It
    just has explainations
    """

    print("\n{}[*]{} Wargame: OverTheWire - Bandit - Level 0".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Author: Timothy Loftus (baffoon)".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Entry Date: June 27, 2017".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Edit Date: July 6, 2017".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Introduction: ".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Introduction goes here.".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Commands used for this level: ".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Commands for nlvl go here.".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Write-up - Level 0: ".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Testing connection to bandit...".format(bcolors.GREEN, bcolors.ENDC))

    if banditConnectionTest() == 1:
        print("{}[*]{} Sufficient data has been acquired... Test was successful.".format(bcolors.GREEN, bcolors.ENDC))

        print("{}[*]{} Preparing ssh client...".format(bcolors.GREEN, bcolors.ENDC))

        client = paramiko.SSHClient()

        print("{}[*]{} Adding host_key via AutoAddPolicy()...".format(bcolors.GREEN, bcolors.ENDC))

        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            print("\n{}[*]{} Attempting connection to...".format(bcolors.GREEN, bcolors.ENDC))
            print("{}[*]{} Username: {}".format(bcolors.GREEN, bcolors.ENDC, user))
            print("{}[*]{} Hostname (FQDN): {}".format(bcolors.GREEN, bcolors.ENDC, host))
            print("{}[*]{} Port: {}".format(bcolors.GREEN, bcolors.ENDC, str(port)))

            client.connect(hostname, port=port, username=user, password=passwd)

        except paramiko.client.BadHostKeyException as BadHostKey:
            print("{}[!] Host key doens't exist... Or unable to add it to known_hosts...{}".format(bcolors.RED, bcolors.ENDC))

        except paramiko.client.socket.err as SocketErr:
            print("{}[!] Error: Bad connection to socket...{}".format(bcolors.RED, bcolors.ENDC))
            print("{}[!] Check your internet connection and try again...{}".format(bcolors.RED, bcolors.ENDC))

        print("{}[*]{} Connction to bandit was successful...".format(bcolors.GREEN, bcolors.ENDC))

        stdin, stdout, stderr = client.exec_command("pwd")
        type(stdin)

        pwdCheck =  stdout.readlines()

        print("{}[*]{} Current directory is: ".format(bcolors.GREEN, bcolors.ENDC) + pwdCheck[0])

        print("{}[*]{} Level completion was a success...".format(bcolors.GREEN, bcolors.ENDC))

        print("{}[*]{} Closing connection to bandit...".format(bcolors.GREEN, bcolors.ENDC))

        client.close()

    else:
        print("{}[!] Error! Error! Connection failed...{}".format(bcolors.RED, bcolors.ENDC))

def banditLvl0ToLvl1Solution(user, hostname, port, passwd):
    """
    Solution
    Wargame: OverTheWire - Bandit
    Level 0 --> Level 1

    This is the first level for OverTheWire - Bandit. Level 0 through Level 1
    is a test to make sure that you understand how to initiate an ssh
    connection. This function will act as a walkthrough on how to do it. It
    will also show the password to Level 1 by connecting to bandit using
    the bandit0 user then listing showing the current directory, listing the
    contents of that directory and later reading the contents of a file to
    obtain the password to Level 1.
    """

    print("\n{}[*]{} Wargame: OverTheWire - Bandit - Level 0 --> Level 1:".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Author: Timothy Loftus (baffoon)".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Entry Date: June 29, 2017".format(bcolors.GREEN, bcolors.ENDC))
    print("{}[*]{} Last Edit: July 5, 2017\n".format(bcolors.GREEN, bcolors.ENDC))

    print("{}[*]{} Introduction: \n".format(bcolors.GREEN, bcolors.ENDC))

    lvl0_to_lvl1_intro = "\n{}[*]{} The password for the next level is stored in a file called readme,\n".format(bcolors.GREEN, bcolors.ENDC)
    lvl0_to_lvl1_intro += "{}[*]{} located in the home directory. Use this password to login to bandit1\n".format(bcolors.GREEN, bcolors.ENDC)
    lvl0_to_lvl1_intro += "{}[*]{} using SSH. Whenever you find a password for a level, use SSH (on port\n".format(bcolors.GREEN, bcolors.ENDC)
    lvl0_to_lvl1_intro += "{}[*]{} 2220) to login to that level and continue the game.".format(bcolors.GREEN, bcolors.ENDC)

    print(lvl0_to_lvl1_intro)

    print("\n{}[*]{} Commands needed for this next level:".format(bcolors.GREEN, bcolors.ENDC))

    print("\n{}[*]{} ls, cd, cat, file, du, find".format(bcolors.GREEN, bcolors.ENDC))

    print("\n{}[*]{} Write-up - Level 0 --> Level 1: ".format(bcolors.GREEN, bcolors.ENDC))

    print("\n{}[*]{} Testing connection to bandit...".format(bcolors.GREEN, bcolors.ENDC))

    if banditConnectionTest() == 1:
        print("{}[*]{} Sufficient data was found... Test was successsful...".format(bcolors.GREEN, bcolors.ENDC))
        print("{}[*]{} Initializing SSH client...".format(bcolors.GREEN, bcolors.ENDC))
    else:
        print("{}[!]{} Error! Error! Test came back with error!".format(bcolors.RED, bcolors.ENDC))

    client = paramiko.SSHClient() # Client prep

    print("{}[*]{} Adding host_key to known_hosts automatically via AutoAddPolicy...".format(bcolors.GREEN, bcolors.ENDC))

    # This part of the functionality will eventually need to be changed.
    # The method used to add the host_key isn't a fully trusted method of doing so.

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Attempting connection to bandit.
    try:
        print("\n{}[*]{} Attempting ssh connection to...".format(bcolors.GREEN, bcolors.ENDC))
        print("{}[*]{} Username: {}".format(bcolors.GREEN, bcolors.ENDC, user))
        print("{}[*]{} Hostname (FQDN): {}".format(bcolors.GREEN, bcolors.ENDC, host))
        print("{}[*]{} Port Number: {}\n".format(bcolors.GREEN, bcolors.ENDC, str(port)))

        client.connect(hostname, port=port, username=user, password=passwd)

    # But what if the host key doesn't exist in the file.
    # Well, it wont because I'm not that for in it's development.
    except paramiko.client.BadHostKeyException as ValidHostKeyErr:

        print("{}[!] Failure to validate hostkey...{}".format(bcolors.RED, bcolors.ENDC))

    # What if there is no internet connection?
    except paramiko.client.socket.err as SshSocketErr:

        print("{}[!] Failure to connect to server... Bad socket...{}".format(bcolors.RED, bcolors.ENDC))
        print("{}[!] I recommend that you check your internet connection...{}".format(bcolors.RED, bcolors.ENDC))

    print("{}[*]{} Connection successful. Results can be found below...".format(bcolors.GREEN, bcolors.ENDC))

    stdin, stdout, stderr = client.exec_command('pwd')
    type(stdin)

    currentDIR = stdout.readlines()

    print("{}[*]{} Displaying Current Directory: ".format(bcolors.GREEN, bcolors.ENDC) + str(currentDIR[0]))

    stdin, stdout, stderr = client.exec_command('ls -l')
    type (stdin)

    print("{}[*]{} Listing directory contents: ".format(bcolors.GREEN, bcolors.ENDC))

    dirContents = stdout.readlines()

    for listedFiles in dirContents:
        print("{}[*]{} ".format(bcolors.GREEN, bcolors.ENDC) + "".join(listedFiles.splitlines()))

    print("\n{}[*]{} Reading the readme file\'s contents...\n".format(bcolors.GREEN, bcolors.ENDC))

    stdin, stdout, stderr = client.exec_command('cat readme')
    type(stdin)

    lvl1Password = stdout.readlines()

    print("{}[*]{} Password to Level 1: ".format(bcolors.GREEN, bcolors.ENDC) + lvl1Password[0])
    print("{}[*]{} Closing connection to bandit...\n".format(bcolors.GREEN, bcolors.ENDC))

    client.close() # Closing the ssh session.

