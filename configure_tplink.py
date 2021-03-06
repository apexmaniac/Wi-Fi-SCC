#! /usr/bin/env python3
import subprocess
import os
import re
import scapy.all as sc
def Checkroot():
    who = subprocess.check_output('whoami')
    chuser = re.search(r"root", str(who))
    if chuser:
        verifywus = input("\n [Verifying] --> The XEye-tp tool needs to run with root user not only running with \"sudo\". Are you running your shell as root? [yes / no] " )
        if verifywus.lower() == 'y' or verifywus.lower() == 'yes':
            Start()
        elif verifywus.lower() == 'n' or verifywus.lower() == 'no':
            print(" [Instruction] --> Please run \"sudo su\" command, enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
        else:
            invalid()
    else:
        print("\n\n [Warning] --> You are not root - Please read and follow the instructions below: \n ")
        print("\n [Instruction] --> 1- Please run the XEye-tp tool with root user not only with \"sudo\" to configure your adapter with no issues. ")
        print(" [Instruction] --> 2- Run \"sudo su\" command then enter the password for the current user to change to root with the pwd, then run the tool again :) \n")
def Start():
    print("\n **********************************************************************************************************************************************************")
    print("\n [Welcoming] --> Welcome to XEye-tp tool :):):) \n\n")
    print(" [Info] --> With XEye-tp tool, you can do the following: \n")
    print(" \t[*] --> 1) Change your WiFi USB adapter TP-Link model WN722N v2 and v3 to Monitor and Injection mode easily and in few minutes or even seconds :) ")
    print(" \t[*] --> 2) You can easily change the Mac address after your TP-Link WiFi USB is set to monitor mode :) ")
    print(" \t[*] --> 3) Scan the network and get all the devices Mac addresses easily if the Adapter is connected to that network  :) ")
    print(" \t[*] --> 4) Make sure to clone the tool again once each week as I am updating the tool and adding more features regularly :):)\n")
    Intf = getinterf()
    print("[Info] --> A TP-Link USB WIFI adapter is detected ")
    ifconfig_outp = subprocess.getoutput("iwconfig "+Intf)
    chwlan = re.search(r"Mode:Managed", str(ifconfig_outp))
    chwlann = re.search(r"Mode:Auto", str(ifconfig_outp))
    chwlannn = re.search(r"Mode:Monitor", str(ifconfig_outp))
    chifasso = re.search(r"unassociated", str(ifconfig_outp))
    if chwlannn:
        lines()
        print("\n [Info] --> Your WiFi TP-Link USB adapter is already set to Monitor mode ")
        Asking = input("\n [Asking] --> Would like to change your adapter Mac address? [yes / no] ")
        lines()
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            print("\n [*] --> Thanks for using XEye-tp tool, Your Adapter is just set to Monitor mode - Bye bye .....\n")
            TheEnd()
        else:
            invalid()
    elif chwlann:
        lines()
        print("\n [Info] --> Your WiFi USB adapter is already set to Auto mode ")
        asking = input(" [Permission] --> Would you like to set your WiFi USB adapter to \"Monitor mode now\" or \"reconfigure\"?  [set / reconf] ")
        lines()
        if asking.lower() == 'set':
           tp_set()
        elif asking.lower() == 'reconf':
           tp_conf()
        else:
           lines()
           print(" [Warning] --> Invalid Entry. [Your interface is just set to Auto mode]   Exiting .....")
           lines()
           exit()
    elif chifasso is None:
        print( " [Info] --> Your adapter \""+Intf+"\" is connected to a network ")
        asking = input("\n [Permission] --> Would you like to grab the mac addresses of the devices on the network? [yes/no] ")
        if asking.lower() == 'y' or asking.lower() == 'yes':
            interct()
        elif asking.lower() == 'n' or asking.lower() == 'no':
           print(" [Required] --> Please disconnect from the WiFi network then run the tool again to configure your adapter - Bye bye :)  ")
        else:
          invalid()
    elif chwlan:
        usermd()
def usermd():
    lines()
    sque= input("\n [Permission] --> Would you like to proceed? [yes / no] ")
    lines()
    if sque.lower() == 'y' or sque.lower() == 'yes':
        tp_conf()
    elif sque.lower() == 'n' or sque.lower() == 'no':
        lines()
        print("\n [*] --> Thanks for using XEye-tp tool, Exiting .....\n")
        TheEnd()
    else:
        invalid()

def tp_conf():
    print("\n [*] --> Updating your system, please wait ....  \n")
    lines()
    subprocess.call(['apt', 'update', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing build-essentials, Please wait ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'build-essential', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing bc, Won't take too long :) ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'bc', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing libelf-dev, Please wait ....  \n")
    lines()
    subprocess.call(['apt', 'install', 'libelf-dev', '-y'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing the required linux-headers, Please wait .....  \n")
    lines()
    subprocess.call("apt install linux-headers-$(uname -r)", shell=True)
    lines()
    print("\n [*] --> Removing \"r8188eu.ko module\"  \n")
    subprocess.call(['rmmod', 'r8188eu.ko'], stdout=subprocess.DEVNULL)
    print("\n [*] --> Git cloning \"rtl8188eus\"  \n")
    lines()
    unamer = subprocess.check_output(['uname','-r'])
    unamerr = re.search(r"\d.\d\d", str(unamer))
    if unamerr is None:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
    elif unamerr.group(0) >= "5.15":
        subprocess.call(['git', 'clone', 'https://github.com/drygdryg/rtl8188eus.git'], stdout=subprocess.DEVNULL)
    else:
        subprocess.call(['git', 'clone', 'https://github.com/aircrack-ng/rtl8188eus'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Installing dkms, please wait ..... ")
    print(" [Info] --> If dkms installation timed out after 90 seconds, the tool would exit with error and you need to upgrade your Kali with the \"sudo apt upgrade -y\" CL \n")
    subprocess.call(['apt', 'install', 'dkms'], stdout=subprocess.DEVNULL, timeout=90)
    lines()
    print("\n [*] --> Done installing dkms. proceeding further ....  \n")
    os.chdir("rtl8188eus")
    lines()
    print("\n [*] --> Echoing \"blacklist r8188eu.ko\" to \"realtek.conf\"  \n")
    subprocess.call("echo \"blacklist r8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    subprocess.call("echo \"blacklist 8188eu.ko\" > \"/etc/modprobe.d/realtek.conf\"", shell=True)
    lines()
    print("\n [*] --> Running Make command, Will take few minutes, please wait and ignore the upcoming errors and warnings ......  \n")
    lines()
    subprocess.call(['make'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running Make Install command  \n")
    lines()
    subprocess.call(['make', 'install'], stdout=subprocess.DEVNULL)
    lines()
    print("\n [*] --> Running \"modprobe 8188eu\"  \n")
    lines()
    subprocess.call("modprobe 8188eu", shell=True)
    iwco = subprocess.check_output(['iwconfig'])
    Auto_check = re.search(r"Mode:Auto", str(iwco))
    if not Auto_check:
        lines()
        print("\n [Warning] --> The WiFi adapter mode is not Auto or it is just missing. ")
        print(" [Instruction] --> UnPlug and plug in your WiFi USB adapter, wait for few seconds then run the tool again with root - Bye bye :)   \n")
        lines()
        exit()
    if Auto_check is not None:
        lines()
        print("\n [Congrats] --> The WiFi USB adapter is successfully configured \n")
        asking = input("\n [Permission] --> Would you like to set your WiFi USB adapter to Monitor mode now?  [yes / no] ")
        lines()
        if asking.lower() == 'y' or asking.lower() == 'yes':
            tp_set()
        elif asking.lower() == 'n' or asking.lower() == 'no':
            lines()
            print("\n [Info] --> Now your adapter is just set to Auto mode - Bye Bye :) \n")
            TheEnd()
        else:
            lines()
            print("\n [Warning] --> Invalid Entry. [Your interface is just set to Auto mode] - Exiting .....\n")
            exit()
def tp_set():
    interf = getinterf()
    subprocess.call(['ifconfig', interf, 'down'])
    subprocess.call("airmon-ng check kill", shell=True)
    subprocess.call(['iwconfig', interf, 'mode', 'monitor'])
    subprocess.call(['ifconfig', interf, 'up'])
    tp_check()
def tp_check():
    interff = getinterf()
    iwcon = subprocess.getoutput("iwconfig"+interff)
    iwcon_Mcheck = re.search(r"Monitor",str(iwcon))
    if iwcon_Mcheck is not None:
        lines()
        print("\n [Congrats] --> You WiFi USB adapter has been set to monitor mode :) :) \n")
        Asking = input("\n [Asking] --> Would like to change your WiFi adapter Mac address? [yes / no] ")
        if Asking.lower() == 'y' or Asking.lower() == 'yes':
            Usermd()
        elif Asking.lower() == 'n' or Asking.lower() == 'no':
            lines()
            print("\n [*] --> Thanks for using XEye-tp tool, Your WiFi Adapter \""+interff+"\" is just set to Monitor mode - Bye bye :) .....\n")
            TheEnd()
        else:
            invalid()
    else:
        lines()
        print("\n [Failure] --> Sorry :( , your WiFi USB could not be changed to monitor mode ")
        print("\n [Instruction] --> 1) Run the tool again because it might be a technical issue was on your system. ")
        print("\n [Instruction] --> 2) If the issue persists, simply upgrade and restart your system then run the tool again :) ")
        print("\n [Instruction] --> 3) To upgrade your system, just run this command \"sudo apt upgrade -y\" \n ")
        exit()
def Usermd():
    Interface = getinterf()
    lines()
    Mac = input("\n        [Required] --> Enter the required Mac address: ")
    if not Mac:
        print(" \n [Warning] --> No Mac address specified. ")
        print(" \n [Info] Now your adapter is just set to monitor mode - Bye bye .....")
        TheEnd()
    Macc1 = getmac(Interface)
    if Macc1 == Mac:
        print(" \n [Info] --> You just entered the same Mac address for " + Interface + ", please enter a different Mac address - Exiting ...... ")
        exit()
    ChMac(Interface, Mac)
    Macc2 = getmac(Interface)
    if (Macc2 == Mac) or (Macc1 != Macc2):
        print(" [Done] --> The Mac address is changed successfully to " + Mac)
        TheEnd()
    else:
        print(" [Warning] --> Something Went wrong, The Mac address couldn't change to "+Mac)
        print("\n [Instruction] --> Enter a valid Mac address, or unplug then plug in you adapter, wait for few seconds then run the tool again - Bye bye :) ")
        exit()

def ChMac(Interface,Mac):
    lines()
    print("\n [Info] --> XEye-tp is setting your " + Interface + " Mac address to " + Mac)
    lines()
    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["iwconfig", Interface, "mode", "Auto"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", Mac])
    subprocess.call(["iwconfig", Interface, "mode", "Monitor"])
    subprocess.call(["ifconfig", Interface, "up"])

def getinterf():
    interfs = subprocess.getoutput('iwconfig |grep WIFI@REALTEK')
    interf = re.search(r"\w\w\w\w\d", str(interfs))
    interff = re.search(r"\w\w\w\d", str(interfs))
    enforc = re.search(r"WIFI@REALTEK", str(interfs))
    if interf and enforc:
        #print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return interf.group(0)
    elif interff and enforc:
        #print("[Info] --> A TP-Link USB WIFI adapter is detected ")
        return interff.group(0)
    else:
        lines()
        print(" [Warning] --> Couldn't detect your TP-Link adapter, please make sure that your adapter is plugged in - Exiting .......")
        exit()
def getmac(interface):
    ifconfgi_re = subprocess.check_output(["ifconfig", interface])
    testing1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfgi_re))
    testing2 = re.search(r"\w\w-\w\w-\w\w-\w\w-\w\w-\w\w", str(ifconfgi_re))
    if testing1:
        return testing1.group(0)
    elif testing2:
        mvalue = testing2.group(0)
        Mvalue = re.sub('-',':',mvalue)
        return Mvalue
    else:
        lines()
        print("\n [Warning] --> Please make sure that your adapter is plugged in, then run the tool again and use the set option. - Exiting ..... ")
        exit()
def interct():
    ipp = subprocess.getoutput("ip r |grep "+getinterf())
    ipr = subprocess.getoutput(ipp+" | grep proto | cut -d\" \" -f1")
    ip = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?", str(ipr))
    if ip is not None:
        print(" [Info] --> Scanning your network \"" + ip.group(0) + "\", please wait ......")
        scanning(ip.group(0))
    else:
        print(" [Warning] --> The adapter might be disconnected from the network. Please try again - Exiting ..... ")
        exit()
def scanning(ip):
    target = sc.ARP(pdst=ip)
    destmac = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    comb = destmac/target
    gotten = sc.srp(comb,timeout=7,verbose=False)[0]
    ips = []
    for el in gotten:
        gottenips = {"ips":el[1].psrc,"mac":el[1].hwsrc}
        ips.append(gottenips)
        #print("---------------------------------------------------------")
    printr(ips)
def printr(ipss):
    print("\n The IP \t\t The Mac Address\n ---------------------------------------------------------")
    for nn in ipss:
        print(nn["ips"]+"\t\t"+nn["mac"])
    TheEnd()
def invalid():
    lines()
    print(" [warning] --> Invalid entry, please use a yes or no answer, Exiting .....")
    lines()
    exit()
def lines():
    print("-------------------------------------------------------------------------------------------------------")
def TheEnd():
    lines()
    print("\n [Recommendation] --> Run the \"exit\" command to exit the root shell, and stay secure :) ")
    print("\n\n\t\t\t\t[*] Thanks for using XEye-tp. Below are recommended courses for you :) [*]")
    print("\n [***] --> The complete Facebook OSINT Hacking course: https://www.udemy.com/course/facebook-osint-hacking/?referralCode=1FEF1A87D703B6DAE484")
    print(" [***] --> The complete Twitter OSINT Hacking course: https://www.udemy.com/course/twitter-osint-hacking/?referralCode=989553134FB1D1CA1D36")
    print(" [***] --> The Introduction to Ethical Hacking course: https://www.udemy.com/course/introduction-to-hacking-n/?referralCode=727E3851BC9C7EBB4314")
    print(" [***] --> The Linux cmd course: https://www.udemy.com/course/linux-command-lines-from-a-hackers-perspective/?referralCode=62A07A01780C21117592")
    print("\n [Recommendation] --> Make sure to clone the tool once a week as I am updating the tool and adding more features regularly :) ")
    lines()
    print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
    exit()
Checkroot()
