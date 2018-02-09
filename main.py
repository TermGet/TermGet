import os
import time
#Imports Libraries

def clear():
    os.system("clear")
#defines clear

clear()
print("\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. zypper (For OpenSUSE, and OpenSUSE based systems)\n5. ecopkg (For Solus, and Solus based systems)/n/npacman has been temporarily removed, sorry for the inconvenience")
setup = "True" #sets the var setup to true
#Asks user which package manager to use

while setup == "True": #Repeats until setup is not true
    user = input() #Asks for user input

    if user == "1":
        setup = "false"
        package = "apt-get"
    elif user == "2":
        setup = "false"
        package = "xbps"
    elif user == "3":
        setup = "false"
        package = "dnf"
    elif user == "4":
        setup = "false"
        package = "zypper"
    elif user == "5":
        setup = "false"
        package = "eopkg"
    else:
        clear()
        print("Error. Invaild package manager")
        time.sleep(1)
        print("\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. zypper (For OpenSUSE, and OpenSUSE based systems)\n5. ecopkg (For Solus, and Solus based systems)/n/npacman has been temporarily removed, sorry for the inconvenience")
#Sets up the package manager

    clear()

    if package == "apt-get":
        os.system("sudo apt-get update")
    elif package == "pacman":
        print("Sorry")
        #os.system("sudo pacman -Syy")
    elif package == "xbps":
        os.system("sudo xbps-install -S")
    elif package == "dnf":
        os.system("sudo dnf clean expire-cache && dnf check-update")
    elif package == "zypper":
        os.system("sudo zypper refresh zypper ref")
    elif package == "eopkg":
        os.system("sudo eopkg ur")

#Updates the system's repositories

while True: #Starts a loop
    clear()
    print("Please choose an action\n\n1. Search for packages\n2. Install an application\n3. Remove an application\n4. Update all packages\n5. Clean\n6. Exit")
    user = input() #Asks for user input

    if user == "1":
        clear()
        user = input("Please enter search query: ")
        print(" ")

        if package == "apt-get":
            os.system("apt-cache search " + user)
        elif package == "pacman":
            os.system("pacman -Sy " + user)
        elif package == "xbps":
            os.system("xbps-query -Rs " + user)
        elif package == "dnf":
            os.system("dnf search " + user)
        elif package == "zypper":
            os.system("zypper search " + user)
        elif package == "eopkg":
            os.system("eopkg search " + user)
        input("\nPress enter to continue")

    if user == "2":
        clear()
        user = input("Please enter which package(s) to install: ")
        print("")

        if package == "apt-get":
            os.system("sudo apt-get install " + user)
        if package == "pacman":
            os.system("sudo pacman -S " + user)
        if package == "xbps":
            os.system("sudo xbps-install " + user)
        if package == "dnf":
            os.system("sudo dnf install " + user)
        if package == "zypper":
            os.system("sudo zypper install " + user)
        if package == "eopkg":
            os.system("sudo eopkg install " + user)
        input("\nPress enter to continue")

    if user == "3":
        clear()
        user = input("Please enter which package(s) to remove: ")
        print("")

        if package == "apt-get":
            os.system("sudo apt-get remove " + user)
        if package == "pacman":
            os.system("sudo pacman -Rs " + user)
        if package == "xbps":
            os.system("sudo xbps-remove " + user)
        if package == "dnf":
            os.system("sudo dnf remove " + user)
        if package == "zypper":
            os.system("sudo zypper remove " + user)
        if package == "eopkg":
            os.system("sudo eopkg remove " + user)
        input("\nPress enter to continue")

    if user == "4":
        clear()
        print("\n")

        if package == "apt-get":
            os.system("sudo apt-get upgrade")
            os.system("sudo apt-get dist-upgrade")
        if package == "pacman":
            os.system("sudo pacman -Syu")
        if package == "xbps":
            os.system("sudo xbps-install -Su")
        if package == "dnf":
            os.system("sudo dnf upgrade")
            os.system("sudo dnf distro-sync")
        if package == "zypper":
            os.system("sudo zypper update zypper up")
            os.system("sudo zypper dup")
        if package == "eopkg":
            os.system("sudo eopkg upgrade")
        input("\nPress enter to continue")
