from termcolor import colored
import os
import subprocess
import re
import time

def monitor_specific_bssid():
    print("*************************")
    print("*  Scan Wi-Fi Networks  *")
    print("*************************")
    ifconfig_outp = subprocess.getoutput("iwconfig")
    interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chifasso = re.search(r"unassociated", str(ifconfig_outp))
    if interfs and chwlannn:
        interfaceadapter = input(colored("## Enter name of Wireless Adapter:-", 'yellow'))
        AP_mac_address = input(colored("## Enter access point's MAC address:-", 'yellow'))
        channel_number = input(colored("## Enter channel number of the target MAC :-", 'yellow'))
        file_to_write = input(colored("## Enter name of handshake file:-", 'yellow'))
        try:
            if interfaceadapter == 'wlan0':
                os.system("sudo airodump-ng --bssid " + AP_mac_address + " --channel " + channel_number +" --write " + file_to_write + "\t" + interfaceadapter)
                monitor_specific_bssid_again()
            elif interfaceadapter == '':
                print("\n")
                print(colored("\tNull Value Detected!!!", 'blue'))
                print("\n")
                monitor_specific_bssid()
            else:
                print("Enter from available WLAN interfaces")

        except KeyboardInterrupt:
            print("Process Aborted!!!!")
            monitor_specific_bssid_again()

    elif interfs and chwlan :
        print("\nTP-Link adapter is in Managed Mode")
        print("\n Enable Monitor Mode TO sniff wifi networks")
        time.sleep(3)
        exit()
    elif interfs and chwlann :
        print("\nTP-Link adapter is in Auto Mode")
        print("\n Enable Monitor Mode TO sniff wifi networks")
        time.sleep(3)
        exit()
    elif interfs:
        print("\n Please enable Monitor Mode")
        time.sleep(3)
        exit()
    else:
        print("\n Didn't detect any WLAN adapter")
        print("\n\n Please Connect your WLAN adapter for WI-FI Sniffing.")
        exit()

def monitor_specific_bssid_again():
    choice = input("Need Another Scan(y/n):- ")
    if choice == 'y':
        airodump()
    elif choice == 'n':
        print("Sniffing Terminated.......")
        time.sleep(2)
        exit(

        )
    else:
        print("Enter y or n:--")
        monitor_specific_bssid_again()


monitor_specific_bssid()