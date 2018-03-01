import os
import time
import sys
import getpass

package = " "
package_file_read = open("/home/" + getpass.getuser() + "/.termget/termget-package-manager","r").read()
#Imports libraries and sets variables

version = "2.0"
credit = "TermGet was created by:\n- PizzaLovingNerd (main developer)\n- SudoLinux\n- Dylan Cruz"

if len(sys.argv) == 2:
    if sys.argv[1] == "apt-get": package = "apt-get"
    elif sys.argv[1] == "pacman": package = "pacman"
    elif sys.argv[1] == "xbps": package = "xbps"
    elif sys.argv[1] == "dnf": package = "dnf"
    elif sys.argv[1] == "yum": package = "yum"
    elif sys.argv[1] == "zypper": package = "zypper"
    elif sys.argv[1] == "eopkg": package = "eopkg"
    elif sys.argv[1] == "pip": package = "pip"
    elif sys.argv[1] == "emerge": package = "emerge"
    elif sys.argv[1] == "pkg": package = "pkg"

if package == " ":
    if package_file_read == "apt-get": package = "apt-get"
    elif package_file_read == "pacman": package = "pacman"
    elif package_file_read == "xbps": package = "xbps"
    elif package_file_read == "dnf": package = "dnf"
    elif package_file_read == "yum": package = "yum"
    elif package_file_read == "zypper": package = "zypper"
    elif package_file_read == "eopkg": package = "eopkg"
    elif package_file_read == "emerge": package = "emerge"
    elif package_file_read == "pkg": package = "pkg"

print("package manager set to " + package)

#Checks for command line argument

def clear(): os.system("clear")
    #Runs 'clear' over shell to clear the screen.

clear()

if package == " ": #Checks for command line argument
    print("Welcome to TermGet. This is version " + version + "\n\nFirst Time Setup:\n\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. yum (For older versions of Fedora, and older Fedora based systems)\n5. zypper (For OpenSUSE, and OpenSUSE based systems)\n6. eopkg (For Solus, and Solus based systems)\n7. pacman (For Arch, and Arch based systems)\n8. emerge(For Gentoo, and Gentoo based systems)\n9. pkg (for FreeBSD, and FreeBSD based systems.)")
    setup = "True"
else:
    print("Welcome to TermGet. This is version " + version)
    time.sleep(1)
    clear()
    setup = "False"
    #Sets the variable 'setup' to False

#Asks user which package manager to use

while setup == "True": #Repeats until setup is not true
    package_file_write = open("/home/" + getpass.getuser() + "/.termget/termget-package-manager","a")
    user = input() #Asks for user input
    if user == "1":
        setup = "false"
        package = "apt-get" #Sets package manager to apt-get
        package_file_write.write("apt-get")
    elif user == "2":
        setup = "false"
        package = "xbps" #Sets package manager to xbps
        package_file_write.write("xbps")
    elif user == "3":
        setup = "false"
        package = "dnf" #Sets package manager to dnf
        package_file_write.write("dnf")
    elif user == "4":
        setup = "false"
        package = "yum" #Sets package manager to yum
        package_file_write.write("yum")
    elif user == "5":
        setup = "false"
        package = "zypper" #Sets package manager to zypper
        package_file_write.write("zypper")
    elif user == "6":
        setup = "false"
        package = "eopkg" #Sets package manager to eopkg
        package_file_write.write("eopkg")
    elif user == "7":
        setup = "false"
        package = "pacman" #Sets package manager to pacman
        package_file_write.write("pacman")
    elif user == "8":
        setup = "false"
        package = "emerge" #Sets package manager to emerge
        package_file_write.write("emerge")
    elif user == "9":
        setup = "false"
        package = "pkg" #Sets package manager to emerge
        package_file_write.write("emerge")
    else:
        clear()
        print("Error. Invaild package manager")
        time.sleep(1)
        clear()
        print("\nPlease choose a package manager\n\n1. apt-get (For Debian, and Debian based systems.)\n2. xbps (For Void Linux, and Void Linux based systems)\n3. dnf (For Fedora, and Fedora based systems)\n4. yum (For older versions of Fedora, and older Fedora based systems)\n5. zypper (For OpenSUSE, and OpenSUSE based systems)\n6. eopkg (For Solus, and Solus based systems)\n7. pacman (For Arch, and Arch based systems)\n8. emerge(For Gentoo, and Gentoo based systems)9. pkg (for FreeBSD, and FreeBSD based systems.)")
        #Sets up the package manager

if package != "pip":
    while True: #Starts a loop
        clear()
        print("Please choose an action\n\n1. Search for packages\n2. Install an application\n3. Remove an application\n4. Update all packages\n5. Update Repo\n6. Clean\n7. Credits\n8. Exit")
        user = input() #Asks for user input
        if user == "1": #Search
            clear()
            user = input("Please enter search query: ")
            print(" ")
            if package == "apt-get": os.system("sudo apt-cache search " + user)
            elif package == "pacman":
                user1 = input("Which package manager would you like to use?\n\n1. pacman\n2. yaourt\n")
                if user1 == "1": os.system("sudo pacman -Ss " + user)
                if user1 == "2": os.system("yaourt -Ss " + user)
            elif package == "xbps": os.system("sudo xbps-query -Rs " + user)
            elif package == "dnf": os.system("sudo dnf search " + user)
            elif package == "yum": os.system("sudo yum search " + user)
            elif package == "zypper": os.system("sudo zypper search " + user)
            elif package == "eopkg": os.system("eopkg search " + user)
            elif package == "emerge": os.system("emerge -S " + user)
            elif package == "pkg": os.system("pkg search " + user)
            input("\nPress enter to continue")

        if user == "2": #Install
            clear()
            user = input("Please enter which package(s) to install: ")
            print("")

            if package == "apt-get": os.system("sudo apt-get install " + user)
            if package == "pacman":
                user1 = input("Which package manager would you like to use?\n\n1. pacman\n2. yaourt\n")
                if user1 == "1": os.system("sudo pacman -S " + user)
                if user1 == "2": os.system("yaourt -S " + user)
            elif package == "xbps": os.system("sudo xbps-install " + user)
            elif package == "dnf": os.system("sudo dnf install " + user)
            elif package == "yum": os.system("sudo yum install " + user)
            elif package == "zypper": os.system("sudo zypper install " + user)
            elif package == "eopkg": os.system("sudo eopkg install " + user)
            elif package == "emerge": os.system("emerge " + user)
            elif package == "pkg": os.system("sudo pkg install " + user)
            input("\nPress enter to continue")

        if user == "3": #Remove
            clear()
            user = input("Please enter which package(s) to remove: ")
            print("")
            elif package == "apt-get":
                user1 = input("How will you like to remove the package?\n\n1. remove, removes just the package (faster)\n2. purge, removes the package, and all it's configuration files (saves space)")
                clear()
                if user1 == "1": os.system("sudo apt-get remove " + user)
                if user1 == "2": os.system("sudo apt-get purge " + user)
            elif package == "pacman": os.system("sudo pacman -Rs " + user)
            elif package == "xbps": os.system("sudo xbps-remove " + user)
            elif package == "dnf": os.system("sudo dnf erase " + user)
            elif package == "yum": os.system("sudo yum remove " + user)
            elif package == "zypper": os.system("sudo zypper remove " + user)
            elif package == "eopkg": os.system("sudo eopkg remove " + user)
            elif package == "emerge": os.system("emerge -C" + user)
            elif package == "pkg": os.system("sudo pkg delete " + user)
            input("\nPress enter to continue")

        if user == "4": #Updates Packages
            clear()
            print("\n")
            elif package == "apt-get":
                os.system("sudo apt-get upgrade")
                os.system("sudo apt-get dist-upgrade")
            elif package == "pacman": os.system("sudo pacman -Syu")
            elif package == "xbps": os.system("sudo xbps-install -Su")
            elif package == "dnf":
                os.system("sudo dnf upgrade")
                os.system("sudo dnf distro-sync")
            elif package == "yum": os.system("sudo yum update")
            elif package == "zypper":
                os.system("sudo zypper update && zypper up")
                os.system("sudo zypper dup")
            elif package == "eopkg": os.system("sudo eopkg upgrade")
            elif package == "emerge":
                os.system("sudo emerge -u world")
                os.system("sudo emerge -uDN world")
            elif package == "pkg": os.system("sudo pkg upgrade " + user)
            input("\nPress enter to continue")

        if user == "5": #Updates Repo
            clear()
            print("\n")
            if package == "apt-get": os.system("sudo apt-get update")
            elif package == "pacman": os.system("sudo pacman -Sy")
            elif package == "xbps": os.system("sudo xbps-install -S")
            elif package == "dnf": os.system("sudo dnf clean expire-cache && sudo dnf check-update")
            elif package == "zypper": os.system("sudo zypper refresh zypper ref")
            elif package == "eopkg": os.system("sudo eopkg ur")
            elif package == "emerge": os.system("sudo layman -f")
            elif package == "yum": os.system("sudo yum yum check-update")
            elif package == "pkg": os.system("sudo pkg update)
            input("\nPress enter to continue")

        if user == "6": #Cleans

            clear()

            if package == "apt-get":
                os.system("sudo apt-get autoremove")
                os.system("sudo apt-get autoclean")
                os.system("sudo apt-get clean")
            elif package == "pacman":
                os.system("sudo pacman -Qdtq | pacman -Rs -")
                os.system("sudo pacman -Sc")
            elif package == "xbps":
                os.system("sudo xbps-remove -o")
                os.system("sudo xbps-remove -O")
            elif package == "dnf":
                os.system("sudo dnf autoremove")
                os.system("sudo dnf clean all")
            elif package == "yum":
                os.system("sudo yum clean all")
                os.system("sudo yum autoremove")
            elif package == "zypper":
                os.system("sudo zypper rm -u")
                os.system("sudo zypper clean")
            elif package == "eopkg":
                os.system("sudo eopkg delete-cache")
                os.system("sudo eopkg remove-orphans")
            elif package == "emerge":
                os.system("sudo emerge --depclean")
                os.system("sudo eclean distfiles")
            elif package == "pkg":
                os.system("sudo pkg clean")
                os.system("sudo pkg autoremove")

            input("\nPress enter to continue")

        if user == "7": #Credits
            print(credit)
            time.sleep(3)
            #If you contribute, please add your name.

        if user == "8": quit()


if package == "pip": #Starts a loop
    while True:
	    print("Please choose an action\n\n1. Search for packages\n2. Install an application\n3. Remove an application\n4. List packages installed with pip5. Credits\n6. Exit")

	    if user == "1": #Search
		    clear()
		    user = input("Please enter search query: ")
		    print(" ")
		    os.system("sudo pip install " + user)

		    input("\nPress enter to continue")

	    if user == "2": #Install
		    clear()
		    user = input("Please enter which package(s) to install: ")
		    print("")
		    os.system("sudo pip search \"" + user + "\"")

		    input("\nPress enter to continue")

	    if user == "3": #Remove
		    clear()
		    user = input("Please enter which package(s) to remove: ")
		    print("")
		    os.system("sudo pip uninstall " + user)

	    if user == "4": #List
		    clear()
		    print("")
		    user = input("Please choose an action:\n1. List all packages\n2. List outdated packages")
		    if user == "1":
			    os.system("sudo pip list ")
		    if user == "2":
			    os.system("sudo pip list --outdated")

	    if user == "5": #Credits
		    print(credit)
		    time.sleep(3)

	    if user == "6": quit()
