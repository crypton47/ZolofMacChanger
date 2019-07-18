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
    slowprinting("# S T  A  R  T  I  N  G ! ", 0.05)
    time.sleep(1)
    # os.system('clear')
    slowprinting('''
                                ||\\      //||
                                || \\    // ||
                                ||  \\  //  ||
                                ||   \\//   ||
                                ||         ||R.Z0lof_______________________________________ (Version 0.1)
    ''', 0.0001)
    print("[------------------------[1] Show my @MAC ----------------------------------------------]")
    print("[------------------------[2] Change your @MAC Randomly ---------------------------------]")
    print("[------------------------[3] Change your @MAC Custumly ---------------------------------]")
    print("[---- -------------------[99] EXIT -----------------------------------------------------]")
    choice = str(input("Make your choice : "))
    if choice == "1":
        print("Your  device eth0 MAC @ is ")
        os.system('macchanger -s eht0')
        os.system('macchanger -s wlan0')
        print(" ")
    elif choice == "2":
        print("Changing  Randomly your @MAC ")
        os.system('ifconfig eth0 down | macchanger -r eth0 | ifconfig eth0 up | macchanger -s eht0 ')
        print(" ")
    elif choice == "3":
        print("Changing Customly your @MAC ")
        newMac = str(input("Enter the new @MAC using the format : XX:XX:XX:XX:XX:XX \n"))
        os.system('macchanger -m newMac')




    else:
        print("GOOD BYE MY LITTLE HACKER ")











