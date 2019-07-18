import os
import sys
import time
#-*- coding:utf-8 -*-

def slowprinting(s, t):
    for elt in s + "\n":
        sys.stdout.write(elt)
        sys.stdout.flush()
        time.sleep(t)
if __name__ == "__main__":
    os.system('clear')
    print("\n \n \n \n \n ")
    slowprinting("\033[91m [!]  S T A R T I N G ... \033[93m", 0.05)
    time.sleep(1)
    slowprinting('''
               ||\\      //||
               || \\    // ||
               ||  \\  //  ||
               ||   \\//   ||
               ||         ||acChanger. (Version 0.1 by Z0lof47)
    ''', 0.0001)
    print("                \033[91m  [1] \033[97m  Show @MAC")
    print("                \033[91m  [2] \033[97m  Change @MAC Randomly")
    print("                \033[91m  [3] \033[97m  Change @MAC Custumly ")
    print("                \033[91m  [99] \033[97m  EXIT")
    print(" ")
    choice = str(input(" \033[91m  [?] \033[97m >>> Make your choice : "))
    if choice == "1":
        print("eth0's MAC @is ")
        os.system('macchanger -s eth0')
        # os.system('macchanger -s wlan0')
        input("Press any key to continue")
        os.system('python3 myMacChanger.py')
    elif choice == "2":
        print("Changing  Randomly your @MAC ")
        os.system('ifconfig eth0 down|macchanger -r eth0')
        print(" ")
        os.system('ifconfig eth0 up')
        os.system('macchanger -s eth0')
    elif choice == "3":
        print("Changing Customly your @MAC ")
        newMac = str(input("Enter the new @MAC using the format : XX:XX:XX:XX:XX:XX \n"))
        os.system('macchanger -m newMac')




    else:
        print("GOOD BYE MY LITTLE HACKER ")











