#!/usr/bin/env python3
import os
import time
import sys
import getpass
import urllib.request

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
            print(yellow + "Warnung: Fehlende Paket-Datei...")
    version = "3.0.1" # version number

    credit = magenta + (
        "TermGet wurde erstellt von:\n"
        "- PizzaLovingNerd (Haupt-Entwickler)\n"
        "- SadError256\n"
        "- Linux /usr/\n"
        "- Emil Engler"
        )

    # sorry dylan! :3 youve had no contributions

    def setpack(var):
        os.system('sudo bash -c "echo -n ' + var + ' > /usr/local/share/termget/termget-package-manager"')

    def askreturn(): input(reset + yellow + "\nDrücke Enter um weiterzumachen")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nWähle einen Packet-Manager:\n"
            "\n1. apt-get (Für Debian, und Debian basierte systeme.)"
            "\n2. xbps (Für Void Linux, und Void Linux basierte systeme)"
            "\n3. dnf (Für Fedora, und Fedora basierte systeme)"
            "\n4. yum (Für alte Versionen von Fedora, und ältere Fedora basierte systeme)"
            "\n5. zypper (Für OpenSUSE, und OpenSUSE basierte systeme)"
            "\n6. eopkg (Für Solus, und Solus basierte systeme)"
            "\n7. pacman (Für Arch, und Arch basierte systeme)"
            "\n8. emerge(Für Gentoo, und Gentoo basierte system)"
            "\n9. pkg (Für FreeBSD, und FreeBSD basierte systeme.)"
            "\n10. chromebrew (Für Chrome OS, Chromium OS, CloudReady, und ZayuOS)"
            "\n11. homebrew (Für macOS/Mac OS X)"
            "\n12. nix (Für NixOS, und NixOS basierte systeme.)"
        )

    if getpass.getuser() == "chronos":
        os.system("clear")
        setup = "True"
        while setup == "True":
            user = input(multichoicePrompt(
                "TermGet hat erkannt das du Chrome OS, Chromium OS, CloudReady, oder Nayu OS benutzt ist das richtig?\n"
                "\n1. Ja"
                "\n2. Nein"))

            if user == "1":
                setup = "False"
                package = "chromebrew"
            elif user == "2":
                setup = "False"
            else:
                print(red + "Irgendwas lieft bei deiner Eingabe falsch")
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
            print(reset + "package manager set to " + package)
    except Exception:
        print(yellow + "Warning: Missing Package File...")
        if package == " ": package = "null"
        print(reset + yellow + "package manager set to " + package)
    # Checks for command line argument


    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nDu nutzt die Version " + version)

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
            print(red + "Falscher Paket-Manager")
            time.sleep(1)
            clear()
            user = input(pickManager())
            # Sets package manager lolz

    # MEOW!

    if package != "pip" and package != "pip2" and package != "pip3" and package != "apm" and package != "npm" and package != "snap":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Suche nach Pakete"
                "\n2. Installiere ein Paket"
                "\n3. Entferne ein Paket"
                "\n4. Update alle Pakete"
                "\n5. Update die Datenbank"
                "\n6. Leere den Cash"
                "\n7. Überprüfe nach TermGet aktualisierungen"
                "\n8. Credits"
                "\n9. Verlassen"
                "\n10. Betrete die shell\n\n"))  # Asks for user input

            if user == "1":  # Searc-meow
                clear()
                user = input(reset + "Bitte gebe einen Suchbegriff ein: ")
                print(reset + " ")
                if package == "apt-get": os.system("sudo apt-cache search " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paket-Manager möchtest du benutzen?\n"
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
                elif package == "nix": os.system("nix search " + user)
                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Sage mir was ich installieren soll: ")
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
                user = input(reset + "Sage mir welche Pakete ich entfernen soll: ")
                print(reset + "")
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                        "Wie willst du es entfernen?\n"
                        "\n1. Remove, entfernt nur das Paket (schneller)"
                        "\n2. Purge, entferne das Paket und alle Konfigurationen (mehr freier Speicher)" + reset))
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
                    "Möchtest du auch die Datenbank neu laden ? ?\n"
                    "\n1. Ja"
                    "\n2. Nein" + reset))
                    if user1 == "1": os.system("sudo apt-get update")
                    os.system("sudo apt-get upgrade")
                    os.system("sudo apt-get dist-upgrade")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paket-Manager möchtest du benutzen?\n"
                        "\n1. pacman"
                        "\n2. yaourt" + reset))
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
                elif package == "nix": os.system("nix-env -u '*'")
                askreturn()

            if user == "5":  # Updates Database MEOW
                clear()
                if package == "apt-get": os.system("sudo apt-get update")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paket-Manager möchtest du benutzen?\n"
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
                elif package == "chromebrew": print(reset + "This feature is unavailable for chromebrew\n")
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
                elif package == "chromebrew": print(reset + "Diese Funktion ist auf chromebooks nicht verfügbar\n")
                elif package == "homebrew": print(reset + "Homebrew macht das automatisch. :)\n")
                elif package == "nix": os.system("nix-collect-garbage -d")
                askreturn()


            if user == "7": #Update TermGet
                clear()
                urllib.request.urlretrieve("http://termget.gitlab.io/Downloads/version.txt", "version.txt")
                versiontxt = open("version.txt", "r")
                versiontxttag = versiontxt.read()
                if version == versiontxttag:
                    print(green + "Du hast die neuste Version" + reset)
                    os.remove("version.txt")
                    time.sleep(3)

                elif version != versiontxttag:
                    print(red + "Deine Version ist veraltet, bitte update" + reset)
                    os.remove("version.txt")
                    time.sleep(3)


            if user == "8":  # Credits

                clear()
                print(credit)
                time.sleep(3)

            if user == "9":
                print(reset)
                clear()
                quit()

            if user == "10":
                clear()
                print(reset + "Betrete bash...")
                print(reset + "Drücke CTRL+D oder gib ein \"exit\" um zu termget zurückzukehren.")
                os.system("bash")
                print(reset + "Rückkehr zu termget...")
                clear()

    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Wähle eine Funktion\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere Pakete"
                "\n3. Update Pakete"
                "\n4. Entferne Pakete"
                "\n5. Zeige alle pip pakete an"
                "\n6. Credits"
                "\n7. Beenden"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte gib die Suchanfrage ein: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib das zu installierende Paket ein: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib ein welche Pakete du updaten möchtest ")
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
                    "\n2. Zeige abgelaufene Pakete an"))
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
                "Wähle eine Aktion\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Update ein Paket"
                "\n4. Entferne ein Paket"
                "\n5. Zeige installierte Pakete an"
                "\n6. Credits"
                "\n7. Beenden"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                print("")
                os.system("apm search " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib an welches Paket du installieren willst: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib an welche Pakete du updaten möchtest: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Bitte gib an welche Pakete du entfernen möchtest")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Bitte wähle eine Aktion:\n"
                    "\n1. Zeige alle Pakete an"
                    "\n2. Zeige veraltete Pakete an"))
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
            "Wähle eine Aktion:\n"
            "\n1. Suche nach snaps"
            "\n2. Installiere snaps"
            "\n3. Entferne snaps"
            "\n4. Zeige installierte snaps an"
            "\n5. Credits"
            "\n6. Verlassen"))

            if user == "1":
                clear()
                user = input(reset + "Gebe einen Suchbegriff ein: ")
                print("")
                os.system(reset + "sudo snap search")
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gebe den Snap-Namen ein: ")
                print("")
                os.system(reset + "sudo snap install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gebe den zu entfernenden Snap-Namen ein: ")
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


except KeyboardInterrupt:
        clear()
        print(red + "Programm wird beendet..." + reset) # moo
        quit()
