#!/usr/bin/python3
import os
import time
import sys
import getpass

# Colors (Thanks to Linux /usr/ for this code)
bold = "\033[1m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"

print(reset) # disable all color on start

package = " "

# The TermGet SPLASHSCREEN
termgetBig = """
_________  _______   _______   _______   _______   _______  _________
\__   __/ (  ____ \ (  ____ ) (       ) (  ____ \ (  ____ \ \__   __/
   ) (    | (    \/ | (    )| | () () | | (    \/ | (    \/    ) (
   | |    | (__     | (____)| | || || | | |       | (__        | |
   | |    |  __)    |     __) | |(_)| | | | ____  |  __)       | |
   | |    | (       | (\ (    | |   | | | | \_  ) | (          | |
   | |    | (____/\ | ) \ \__ | )   ( | | (___) | | (____/\    | |
   )_(    (_______/ |/   \__/ |/     \| (_______) (_______/    )_(


"""

def multichoicePrompt(string):
    breakdoublereturn = string.split("\n\n") # top part is white bold, so split by double return will separate
    returnstr = reset + bold + breakdoublereturn[0] + "\n\n" # put top part in return
    mag = True # magenta? boolean

    for line in breakdoublereturn[1].split("\n"): # interlace the colors for each line
        if mag == True:
            returnstr = returnstr + bold + magenta + line + "\n"
            mag = False
        else:
            returnstr = returnstr + bold +  cyan + line + "\n"
            mag = True
    return returnstr + "\n" # final return (with extra newline) for function

try:
    try:
        package_file_read = open("/usr/local/share/termget/termget-package-manager", "r").read() # read package manager file
        # package_file_read = "" # debug feature
    except Exception:
        print(yellow + "Warning: Missing Package File...")
    version = "2.1.2" # version number

    credit = magenta + (
        "TermGet was created by:\n"
        "- PizzaLovingNerd (main developer)\n"
        "- SadError256\n"
        "- Dylan Cruz\n"
        "- Linux /usr/"
        )

    def setpack(var):
        os.system('sudo bash -c "echo -n ' + var + ' > /usr/local/share/termget/termget-package-manager"')

    def askreturn(): input(reset + "\nPress enter to continue")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nPlease choose a package manager:\n"
            "\n1. apt-get (For Debian, and Debian based systems.)"
            "\n2. xbps (For Void Linux, and Void Linux based systems)"
            "\n3. dnf (For Fedora, and Fedora based systems)"
            "\n4. yum (For older versions of Fedora, and older Fedora based systems)"
            "\n5. zypper (For OpenSUSE, and OpenSUSE based systems)"
            "\n6. eopkg (For Solus, and Solus based systems)"
            "\n7. pacman (For Arch, and Arch based systems)"
            "\n8. emerge(For Gentoo, and Gentoo based systems)"
            "\n9. pkg (for FreeBSD, and FreeBSD based systems.)"
            "\n10. chromebrew (for Chrome OS, Chromium OS, CloudReady, and ZayuOS)"
            "\n11. homebrew (for macOS/Mac OS X)")

    if getpass.getuser() == "chronos":
        os.system("clear")
        setup = "True"
        while setup == "True":
            user = input(multichoicePrompt(
                "TermGet has detected this is Chrome OS, Chromium OS, CloudReady, or Nayu OS... is this true?\n"
                "\n1. Yes"
                "\n2. No"))

            if user == "1":
                setup = "False"
                package = "chromebrew"
            elif user == "2":
                setup = "False"
            else:
                print(red + "Error. Invalid answer")
                # Checks for Chromebook

    if package == " " and len(sys.argv) == 2:
        if sys.argv[1] == "apt-get" or sys.argv[1] == "apt": package = "apt-get"
        elif sys.argv[1] == "pacman" or sys.argv[1] == "yaourt": package = "pacman"
        elif sys.argv[1] == "xbps": package = "xbps"
        elif sys.argv[1] == "dnf": package = "dnf"
        elif sys.argv[1] == "yum": package = "yum"
        elif sys.argv[1] == "zypper": package = "zypper"
        elif sys.argv[1] == "eopkg": package = "eopkg"
        elif sys.argv[1] == "pip3": package = "pip3"
        elif sys.argv[1] == "pip2": package = "pip2"
        elif sys.argv[1] == "pip": package = "pip"
        elif sys.argv[1] == "apm": package = "apm"
        elif sys.argv[1] == "emerge": package = "emerge"
        elif sys.argv[1] == "pkg": package = "pkg"
        elif sys.argv[1] == "chromebrew": package = "chromebrew"
        elif sys.argv[1] == "homebrew": package = "homebrew"

    try:
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
            elif package_file_read == "chromebrew": package = "chromebrew"
            elif package_file_read == "homebrew": package = "homebrew"
            print(reset + "package manager set to " + package)
    except Exception:
        print(yellow + "Warning: Missing Package File...")
        if package == " ": package = "null"
        print(reset + yellow + "package manager set to " + package)
    # Checks for command line argument


    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nThis is version " + version)

    if package == " " or package == "null":  # Checks for command line argument
        user = input(pickManager())
        setup = "True"
    else:
        time.sleep(1)
        clear()
        setup = "False"
        # Sets the variable 'setup' to False

    # Asks user which package manager to use

    while setup == "True":  # Repeats until setup is not true
        if user == "1":
            setup = "false"
            package = "apt-get"  # Sets package manager to apt-get
            setpack("apt-get")
        elif user == "2":
            setup = "false"
            package = "xbps"  # Sets package manager to xbps
            setpack("xbps")
        elif user == "3":
            setup = "false"
            package = "dnf"  # Sets package manager to dnf
            setpack("dnf")
        elif user == "4" or user == "yum":
            setup = "false"
            package = "yum"  # Sets package manager to yum
            setpack("yum")
        elif user == "5":
            setup = "false"
            package = "zypper"  # Sets package manager to zypper
            setpack("zypper")
        elif user == "6":
            setup = "false"
            package = "eopkg"  # Sets package manager to eopkg
            setpack("eopkg")
        elif user == "7":
            setup = "false"
            package = "pacman"  # Sets package manager to pacman
            setpack("pacman")
        elif user == "8":
            setup = "false"
            package = "emerge"  # Sets package manager to emerge
            setpack("emerge")
        elif user == "9":
            setup = "false"
            package = "pkg"  # Sets package manager to pkg
            setpack("pkg")
        elif user == "10":
            setup = "false"
            package = "chromebrew"  # Sets package manager to chromebrew
            setpack("chromebrew")
        elif user == "11":
            setup = "false"
            package = "homebrew"
            setpack("homebrew")
        else:
            clear()
            print(red + "Error. Invalid package manager")
            time.sleep(1)
            clear()
            user = input(pickManager())
            # Sets package manager lolz

    # MEOW!

    if package != "pip" and package != "pip2" and package != "pip3" and package != "apm":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Remove an application"
                "\n4. Update all packages"
                "\n5. Update Database"
                "\n6. Clean"
                "\n7. Credits"
                "\n8. Exit"
                "\n9. Enter shell"))  # Asks for user input

            if user == "1":  # Searc-meow
                clear()
                user = input(reset + "Please enter search query: ")
                print(reset + " ")
                if package == "apt-get": os.system("sudo apt-cache search " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("sudo pacman -Ss " + user)
                    if user1 == "2": os.system("yaourt -Ss " + user)
                elif package == "xbps": os.system("sudo xbps-query -Rs " + user)
                elif package == "dnf": os.system("sudo dnf search " + user)
                elif package == "yum": os.system("yum search " + user)
                elif package == "zypper": os.system("sudo zypper search " + user)
                elif package == "eopkg": os.system("eopkg search " + user)
                elif package == "emerge": os.system("emerge -S " + user)
                elif package == "pkg": os.system("pkg search " + user)
                elif package == "chromebrew": os.system("crew search " + user)
                elif package == "homebrew": os.system("brew search " + user)
                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")

                if package == "apt-get": os.system("sudo apt-get install " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("sudo pacman -S " + user)
                    if user1 == "2": os.system("yaourt -S " + user)
                elif package == "xbps": os.system("sudo xbps-install " + user)
                elif package == "dnf": os.system("sudo dnf install " + user)
                elif package == "yum": os.system("sudo yum install " + user)
                elif package == "zypper": os.system("sudo zypper install " + user)
                elif package == "eopkg": os.system("sudo eopkg install " + user)
                elif package == "emerge": os.system("emerge " + user)
                elif package == "pkg": os.system("sudo pkg install " + user)
                elif package == "chromebrew": os.system("crew install " + user)
                elif package == "homebrew": os.system("brew install " + user)
                askreturn()

            if user == "3":  # Remove MEOW
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                        "How will you like to remove the package?\n"
                        "\n1. Remove, removes just the package (faster)"
                        "\n2. Purge, removes the package, and all it's configuration files (saves space)"))
                    clear()
                    if user1 == "1": os.system("sudo apt-get remove " + user)
                    if user1 == "2": os.system("sudo apt-get purge " + user)
                elif package == "pacman": os.system("sudo pacman -Rs " + user)
                elif package == "xbps": os.system("sudo xbps-remove " + user)
                elif package == "dnf": os.system("sudo dnf erase " + user)
                elif package == "yum": os.system("sudo yum remove " + user)
                elif package == "zypper": os.system("sudo zypper remove " + user)
                elif package == "eopkg": os.system("sudo eopkg remove " + user)
                elif package == "emerge": os.system("emerge -C " + user)
                elif package == "pkg": os.system("sudo pkg delete " + user)
                elif package == "chromebrew": os.system("crew remove " + user)
                elif package == "homebrew": os.system("brew uninstall " + user)
                askreturn()

            if user == "4":  # Updates Packages
                clear()
                if package == "apt-get":
                    os.system("sudo apt-get upgrade")
                    os.system("sudo apt-get dist-upgrade")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("sudo pacman -Syu")
                    if user1 == "2": os.system("yaourt -Syu")
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
                elif package == "pkg": os.system("sudo pkg upgrade")
                elif package == "chromebrew": os.system("crew upgrade")
                elif package == "homebrew": os.system("brew upgrade")
                askreturn()

            if user == "5":  # Updates Database MEOW
                clear()
                if package == "apt-get": os.system("sudo apt-get update")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("sudo pacman -Syy")
                    if user1 == "2": os.system("yaourt -Syy")
                elif package == "xbps": os.system("sudo xbps-install -S")
                elif package == "dnf": os.system("sudo dnf clean expire-cache && sudo dnf check-update")
                elif package == "zypper": os.system("sudo zypper refresh zypper ref")
                elif package == "eopkg": os.system("sudo eopkg ur")
                elif package == "emerge": os.system("sudo layman -f")
                elif package == "yum": os.system("sudo yum check-update")
                elif package == "pkg": os.system("sudo pkg update")
                elif package == "chromebrew": print(reset + "This feature is unavailable for chromebrew\n")
                elif package == "homebrew": os.system("brew update")
                askreturn()

            if user == "6":  # Cleans

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
                elif package == "chromebrew": print(reset + "This feature is unavailable on chromebrew\n")
                elif package == "homebrew": print(reset + "Homebrew already does this automagically. :)\n")
                askreturn()

            if user == "7":  # Credits QUACK!!

                clear()
                print(credit)
                time.sleep(3)

            if user == "8":
                print(reset)
                quit()

            if user == "9":
                clear()
                print(reset+"Entering bash...")
                print(reset+"Press CTRL+D or type \"exit\" to return to termget.")
                os.system("bash")
                print(reset+"Returning to termget...")
                clear()

            if user == "42":
                clear()
                print(reset+"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                input(reset+"Press enter to leave this boring easter egg...")
                input("I SAID... PRESS ENTER!")
                print(reset+"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                input("this program is broken now")
                input("programprogramprogramress enter to continue")
                print("saderror wasnt involved with this easter egg")
                input("wonder if anyone will find it?")


    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed with pip"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print(reset + "")
                os.system(package + " install --upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                os.system(package + " uninstall \"" + user + "\"")
                askreturn()

            if user == "5":  # List
                clear()
                print(reset + "")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system(package + " list ")
                if user == "2": os.system(package + " list --outdated")
                askreturn()

            if user == "6":  # Credits
                clear()
                print(credit)
                time.sleep(3)
                clear()

            if user == "7":
                print(reset)
                quit()

    if package == "apm":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print("")
                os.system("apm search " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system("apm list")
                if user == "2": os.system("apm outdated")
                askreturn()

            if user == "6":  # Credits - Meooow
                clear()
                print(credit)
                time.sleep(3)
                clear()

            if user == "7":
                print(reset)
                quit()

except KeyboardInterrupt:
        clear()
        print(red + "Error: Keyboard Interuption. Quitting" + reset) # moo
        quit()
