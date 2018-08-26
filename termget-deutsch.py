#!/usr/bin/env python3
import os
import time
import sys
import getpass
import urllib.request
import hashlib
from urllib import parse
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
            returnstr = returnstr + bold + magenta + line + reset + "\n"
            mag = False
        else:
            returnstr = returnstr + bold + blue + line + reset + "\n"
            mag = True
    return returnstr + "\n" # final return (with extra newline) for function

try:
    try:
        package_file_read = open("/usr/local/share/termget/termget-package-manager", "r").read() # read package manager file
        # package_file_read = "" # debug feature
    except Exception:
        try:
            package_file_read = open("/usr/share/termget/termget-package-manager", "r").read() # read package manager file
        except Exception:
            print(yellow + "Warnung: Fehlende Paket Datei")
    version = "Alpha 3.0.1" # version number
    version_number = "1301"    # For each version number remove Beta or Alpha. alpha=1 beta=0 and remove all the dots for example: Alpha 1.1.0 would be 1110 Or Beta 1.1.1 would be 0111       **** !THIS IS USED FOR UPDATE SYSTEM! ****
    credit = magenta + (
        "TermGet wurde erstellt von:\n"
        "- PizzaLovingNerd (Hauptentwickler)\n"
        "- SadError256\n"
        "- Linux /usr/\n"
        "- Dylan Cruz\n"
        "- Emil Engler"
        )


    def setpack(var):
        os.system('sudo bash -c "echo -n ' + var + ' > /usr/local/share/termget/termget-package-manager"')

    def askreturn(): input(reset + yellow + "\nDrücke eine beliebige Taste um fortzufahren...")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nBitte wähle einen Paket-Manager:\n"
            "\n1. apt-get (Für Debian, und Debian basierte Systeme.)"
            "\n2. xbps (Für Void Linux, und Void Linux basierte Systeme)"
            "\n3. dnf (Für Fedora, und Fedora basierte Systeme)"
            "\n4. yum (Für ältere versionen von Fedora, und ältere Fedora basierte Systeme)"
            "\n5. zypper (Für OpenSUSE, und OpenSUSE basierte Systeme)"
            "\n6. eopkg (Für Solus, und Solus basierte Systeme)"
            "\n7. pacman (Für Arch, und Arch basierte Systeme)"
            "\n8. emerge(Für Gentoo, und Gentoo basierte Systeme)"
            "\n9. pkg (Für FreeBSD, und FreeBSD basierte Systeme.)"
            "\n10. chromebrew (for Chrome OS, Chromium OS, CloudReady, und ZayuOS)"
            "\n11. homebrew (for macOS/Mac OS X)"
            "\n12. nix (Für NixOS, und NixOS basierte Systeme)"
        )

    if getpass.getuser() == "chronos":
        os.system("clear")
        setup = "True"
        while setup == "True":
            user = input(multichoicePrompt(
                "TermGet hat erkannt das du Chrome OS, Chromium OS, CloudReady, oder Nayu OS... verwendest ist das korrekt\n"
                "\n1. Ja"
                "\n2. Nein"))

            if user == "1":
                setup = "False"
                package = "chromebrew"
            elif user == "2":
                setup = "False"
            else:
                print(red + "Falsche Antwort")
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
        elif sys.argv[1] == "nix": package = "nix"
        elif sys.argv[1] == "npm": package = "npm"
        elif sys.argv[1] == "snap": package = "snap"
        elif sys.argv[1] == "flatpak": package = "flatpak"
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
            elif package_file_read == "nix": package = "nix"
            print(reset + "package manager gesetzt auf " + package)
    except Exception:
        print(yellow + "Fehlende Paket Datei...")
        if package == " ": package = "null"
        print(reset + yellow + "package manager gesetzt auf " + package)
    # Checks for command line argument


    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nDas ist Version " + version)

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
        elif user == "4":
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
        elif user == "12":
            setup = "false"
            package = "nix"
            setpack("nix")
        elif user == "13":
            setup = "false"
            package = "npm"
            setpack("npm")
        else:
            clear()
            print(red + "Fehler. Falscher Paket Manager")
            time.sleep(1)
            clear()
            user = input(pickManager())
            # Sets package manager lolz

    # MEOW!

    if package != "pip" and package != "pip2" and package != "pip3" and package != "apm" and package != "npm" and package != "snap" and package != "flatpak":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Wähle eine Aktion\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Entferne ein Paket"
                "\n4. Update alle Pakete"
                "\n5. Update Datenbank"
                "\n6. Clean"
                "\n7. Überprüfe auf TermGet Updates"
                "\n8. Credits"
                "\n9. Verlassen"
                "\n10. Shell öffnen")

            if user == "1":  # Search-meow
                clear()
                user = input(reset + "Gib einen Suchbegriff: ")
                print(reset + " ")
                if package == "apt-get": os.system("apt-cache search " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paket-Manager möchtest du benutzen?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("pacman -Ss " + user)
                    if user1 == "2": os.system("yaourt -Ss " + user)
                elif package == "xbps": os.system("xbps-query -Rs " + user)
                elif package == "dnf": os.system("dnf search " + user)
                elif package == "yum": os.system("yum search " + user)
                elif package == "zypper": os.system("zypper search " + user)
                elif package == "eopkg": os.system("eopkg search " + user)
                elif package == "emerge": os.system("emerge -S " + user)
                elif package == "pkg": os.system("pkg search " + user)
                elif package == "chromebrew": os.system("crew search " + user)
                elif package == "homebrew": os.system("brew search " + user)
                elif package == "nix": os.system("nix search " + user)

                user = input(yellow + "\nHast du gefunden nach was du gesucht hast? (y/n)" + reset)

                if user == "y":
                    clear()
                    user = input(reset + "Gib ein welche Pakete du installieren willst: ")
                    print(reset + "")

                    if package == "apt-get": os.system("sudo apt-get install " + user)
                    elif package == "pacman":
                        user1 = input(multichoicePrompt(
                            "Which package manager would you like to use?\n"
                            "\n1. pacman"
                            "\n2. yaourt" + reset))
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
                    elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Gib ein welche Pakete du installieren willst: ")
                print(reset + "")

                if package == "apt-get": os.system("sudo apt-get install " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt" + reset))
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
                elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "3":  # Remove MEOW
                clear()
                user = input(reset + "Gib ein welche Pakete du entfernen willst: ")
                print(reset + "")
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                        "Wie möchtest du es entfernen?\n"
                        "\n1. Remove, entfernt nur das Paket (schnell)"
                        "\n2. Purge, entfernt das Paket und alle Konfigurationen (mehr freier Speicher)" + reset))
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
                elif package == "nix": os.system("nix-env -e " + user)
                askreturn()

            if user == "4":  # Updates Packages
                clear()
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                    "Möchtest du auch die Datenbank neuladen ?\n"
                    "\n1. Ja"
                    "\n2. Nein" + reset))
                    if user1 == "1": os.system("sudo apt-get update")
                    os.system("sudo apt-get upgrade")
                    os.system("sudo apt-get dist-upgrade")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt" + reset))
                    if user1 == "1": os.system("sudo pacman -Syu")
                    if user1 == "2": os.system("yaourt -Syu --aur")
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
                elif package == "nix": os.system("nix-env -u '*'")
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
                    if user1 == "2": os.system("yaourt -Syy" + reset)
                elif package == "xbps": os.system("sudo xbps-install -S")
                elif package == "dnf": os.system("sudo dnf clean expire-cache && sudo dnf check-update")
                elif package == "zypper": os.system("sudo zypper refresh zypper ref")
                elif package == "eopkg": os.system("sudo eopkg ur")
                elif package == "emerge": os.system("sudo layman -f")
                elif package == "yum": os.system("sudo yum check-update")
                elif package == "pkg": os.system("sudo pkg update")
                elif package == "chromebrew": print(reset + "Das geht nicht auf Chromebooks\n")
                elif package == "homebrew": os.system("brew update")
                elif package == "nix": os.system("nix-channel --update nixpkgs")
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
                elif package == "chromebrew": print(reset + "Das geht nicht auf Chromebooks\n")
                elif package == "homebrew": print(reset + "Homebrew macht das automatisch. :)\n")
                elif package == "nix": os.system("nix-collect-garbage -d")
                askreturn()
                         
            if user == "7":  # Credits

                clear()
                print(credit)
                time.sleep(3)

            if user == "8":
                print(reset)
                clear()
                quit()

            if user == "9":
                clear()
                print(reset + "Öffne shell...")
                print(reset + "Drück STRG+D oder gib ein \"exit\" um zu TermGet zurückzugelangen.")
                os.system("bash")
                print(reset + "Rückkehr zu TermGet...")
                clear()
               
               
    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Wähle eine Aktion:\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Update ein Paket"
                "\n4. Entferne ein Paket"
                "\n5. Zeige alle installierten Pakete an"
                "\n6. Credits"
                "\n7. Verlassen"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du entfernen möchtest: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du updaten möchtest: ")
                print(reset + "")
                os.system(package + " install --upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du entfernen möchtest: ")
                print(reset + "")
                os.system(package + " uninstall \"" + user + "\"")
                askreturn()

            if user == "5":  # List
                clear()
                print(reset + "")
                user = input(multichoicePrompt(
                    "Bitte wähle eine Aktion:\n"
                    "\n1. Zeige alle Pakete an"
                    "\n2. Zeige alle veralteten Pakete an"))
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
                "Wähle eine Aktion:\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Update ein Paket"
                "\n4. Entferne ein Paket"
                "\n5. Zeige alle installierten Pakete an"
                "\n6. Credits"
                "\n7. Verlassen"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                print("")
                os.system("apm search " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du installieren möchtest: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du updaten möchtest: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du entfernen möchtest: ")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Bitte wähle eine Aktion:\n"
                    "\n1. Zeige alle Pakete an"
                    "\n2. Zeige alle veralteten Pakete an"))
                if user == "1": os.system("apm list")
                if user == "2": os.system("apm outdated")
                askreturn()

            if user == "6":  # Credits - Meooow
                clear()
                print(credit)

                askreturn()

            if user == "7":
                print(reset)
                quit()

    if package == "snap":
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
                "Wähle eine Aktion:\n"
                "\n1. Suche nach snaps"
                "\n2. Installiere ein snap"
                "\n3. Entferne ein snap"
                "\n4. Zeige alle installierten snaps an"
                "\n5. Credits"
                "\n6. Verlassen"))

            if user == "1":
                clear()
                user = input(reset + "Gib einen Suchbegriff ein: ")
                print("")
                os.system(reset + "snap search" + user)
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gib den Namen des snaps ein: ")
                print("")
                os.system(reset + "sudo snap install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gib den Namen des snaps ein: ")
                print("")
                os.system(reset +  "sudo snap remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("Aktuell sind folgende Snaps installiert: ")
                os.system(reset + "sudo snap list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()



    if package == "flatpak":
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "Wähle eine Aktion:\n"
            "\n1. Suche nach flatpaks (flathub)"
            "\n2. Installiere flatpak (flathub)"
            "\n3. Entferne ein flatpak (flathub)"
            "\n4. Zeige alle installierten flatpaks an"
            "\n5. Credits"
            "\n6. Verlassen"))

            if user == "1":
                clear()
                user = input(reset + "Gib einen Suchbegriff ein: ")
                print("")
                os.system(reset + "flatpak search")
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gib den Namen des flatpaks ein: ")
                print("")
                os.system(reset + "sudo flatpak install flathub" + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gib den Namen des flatpaks ein: ")
                print("")
                os.system(reset +  "sudo flatpak remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("Die aktuell installieren flatpaks sind: ")
                os.system(reset + "sudo flatpak list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()


except KeyboardInterrupt:
        clear()
        print(red + "Error: Keyboard Interuption. Quitting" + reset) # moo
        quit()
