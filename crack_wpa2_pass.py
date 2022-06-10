import re
import subprocess
import os
import time
from termcolor import colored

def aircrack():
    print("***********************************")
    print("*   Crack Passwords (WPA/WPA2)    *")
    print("***********************************")
    wpawpa2()

def wpawpa2():
    wordlist_for_cracking = input("Enter The path of wordlist:-\t ")
    capture_handshake_file = input("Enter the path of captured handshake file:-\t")
    checkfile = subprocess.getoutput('ls |grep' + capture_handshake_file)
    time.sleep(2)
    print("Sequencing the values.....")
    time.sleep(2)
    try:
        if checkfile:
            os.system("sudo aircrack-ng " + "\t" + "-w" + "\t" + wordlist_for_cracking + "\t" + capture_handshake_file)
            wpa_scan_again()
        else:
            print("Given handshake file not exist!! Check again")
            wpa()

    except KeyboardInterrupt:
        print("Ctrl + C pressed.....")
        exit()
def wpa_scan_again():
    choice = input("Need Another crack session(y/n):- ")
    if choice == 'y':
        wpawpa2()
    elif choice == 'n':
        print("Sniffing Terminated.......")
        exit()
    else:
        print("Enter y or n:--")
        wpa_scan_again()

aircrack()
