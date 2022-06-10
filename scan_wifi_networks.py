import re
import subprocess
import os
from termcolor import colored

ifconfig_outp = subprocess.getoutput("iwconfig")
interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
chifasso = re.search(r"unassociated", str(ifconfig_outp))

def airodump():
    print("*************************")
    print("*  Scan Wi-Fi Networks  *")
    print("*************************")
    if interfs:
        if chwlannn:
            interfaceadapter = input(colored("## Enter your choice:-", 'yellow'))
            try:
                if interfaceadapter == 'wlan0':
                    os.system("sudo airodump-ng" + "\t" + interfaceadapter)

                    choice = input("Need Another Scan(y/n):- ")
                    if choice == 'y':
                        airodump()
                    elif choice == 'n':
                        print("Sniffing Terminated.......")
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
            print("\n Enable Monitor Mode TO sniff wifi networks")
            exit()
        elif chwlann:
            print("\nTP-Link adapter is in Auto Mode")
            print("\n Enable Monitor Mode TO sniff wifi networks")
            exit()
        else:
            print("\n Print enable Monitor Mode")
            exit()

    else:
        print("\n Didn't detect any WLAN adapter")
        print("\n\n Please Connect your WLAN adapter for WI-FI Sniffing.")

def lines():
    print("***************************************************************************")
    print("\n")

airodump()
