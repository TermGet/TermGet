import os
import time
import webbrowser
#Imports Libraries

def clear():
    os.system("clear")
#defines clear

clear()
print("Welcome to TermGet\n\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. pacman (For Arch, and Arch based systems)\n3. xbps (For Void Linux, and Void Linux based systems)\n4. dnf (For Fedora, and Fedora based systems)\n5. zypper (For OpenSUSE, and OpenSUSE based systems)\n6. ecopkg (For Solus, and Solus based systems)")
setup = "True" #sets the var setup to true
#Asks user which package manager to use

while setup == "True": #Repeats until setup is not true
    user = input() #Asks for user input

    if user == "1":
        setup = "false"
        package = "apt-get"
    elif user == "2":
        setup = "false"
        package = "pacman"
    elif user == "3":
        setup = "false"
        package = "xbps"
    elif user == "4":
        setup = "false"
        package = "dnf"
    elif user == "5":
        setup = "false"
        package = "zypper"
    elif user == "6":
        setup = "false"
        package = "eopkg"
    else:
        clear()
        print("Error. Invaild package manager")
        time.sleep(1)
        print("\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. pacman (For Arch, and Arch based systems)\n3. xbps (For Void Linux, and Void Linux based systems)\n4. dnf (For Fedora, and Fedora based systems)\n5. zypper (For OpenSUSE, and OpenSUSE based systems)\n6. ecopkg (For Solus, and Solus based systems)")
#Sets up the package manager

while True: #Starts a loop
    clear()
    print("Please choose an action\n\n1. Show featured packages\n2. Search for packages\n3. Install an application\n4. Remove an application\n5. Update all packages, and distro\n6. Clean\n7. Exit")
    user = input() #Asks for user input

    if user == "1":
        print("Opening Featured")
        print("Warning: Not all applications displayed work 100%")
        webbrowser.open("https://github.com/kohimiruku/Awesome-Linux-Software/blob/master/README.md" autoraise=True)
