#!/usr/bin/env python3
import webbrowser, os, time, sys, getpass, urllib.request, hashlib, requests
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
__________                                ____
MMMMMMMMMM                               6MMMMb
    MM                                  8P    YM           _
    MM  ______  __ ___  __ ____  ____  6M      Y   ____    M
    MM  6MMMMb `MM 6MM `MM 6MMb  6MMb  MM         6MMMMb MMMMMM
    MM 6M'  `Mb MM69 "  MM69 `MM69 `Mb MM        6M'  `Mb  MM
    MM MM    MM MM'     MM'   MM'   MM MM   MMMY MM    MM  MM
    MM MMMMMMMM MM      MM    MM    MM MM     `M'MMMMMMMM  MM
    MM MM       MM      MM    MM    MM YM      M MM        MM
    MM YM    d9 MM      MM    MM    MM  8b    d9 YM    d9  YM.
    MM  YMMMM9  MM      MM    MM    MM   YMMMM9   YMMMM9    YMMM9
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
            print(yellow + "Warnung: Einstellundsdatei nicht gefunden...")

    version = "3.1.2" # version number

    credit = magenta + (
        "TermGet wurde erstellt von:\n"
	"- PizzaLovingNerd (Maintainer)\n"
        "- Emil Engler (Maintainer)\n"
	"- Quint Burkley (Maintainer)\n"
        "- NekoBit\n"
        "- TechBizmo"
        )


    def setpack(var):
        f = open("/usr/local/share/termget/termget-package-manager", "w+")
        f.write(var)
        f.close()

    def askreturn(): input(reset + yellow + "\nDrücke enter to um fortzufahren")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nBitte wähle einen Paketmanager:\n"
            "\n1. apt (Für Debian, und Debian basierte Systeme)"
            "\n2. xbps (Für Void Linux, and Void Linux based Systeme)"
            "\n3. dnf (Für Fedora, und Fedora basierte Systeme)"
            "\n4. yum (Für alte Versionen von Fedora, und ältere Fedora basierte Systeme)"
            "\n5. zypper (Für OpenSUSE, und OpenSUSE basierte Systeme)"
            "\n6. eopkg (Für Solus, und Solus basierte Systeme)"
            "\n7. pacman (Für Arch, PacBSD, und Arch basierte Systeme)"
            "\n8. emerge(Für Gentoo, und Gentoo basierte Systeme)"
            "\n9. pkg (für FreeBSD, und FreeBSD basierte Systeme.)"
            "\n10. chromebrew (für Chrome OS, Chromium OS, CloudReady, und NayuOS)"
            "\n11. homebrew (für macOS/Mac OS X)"
            "\n12. nix (Für NixOS, and NixOS basierte systeme.)"
        )

    if getpass.getuser() == "chronos":
        os.system("clear")
        setup = "True"
        while setup == "True":
            user = input(multichoicePrompt(
                "TermGet hat erkannt, dass es sich um ChromeOS handelt, stimmt das ?\n"
                "\n1. Ja"
                "\n2. Nein"))

            if user == "1":
                setup = "False"
                package = "chromebrew"
            elif user == "2":
                setup = "False"
            else:
                print(red + "Fehler, ungültige Antwort")
                # Checks for Chromebook

    if package == " " and len(sys.argv) == 2:
        if sys.argv[1] == "apt" or sys.argv[1] == "apt": package = "apt"
        if sys.argv[1] == "pacman" or sys.argv[1] == "yay": package = "pacman"
        if sys.argv[1] == "xbps": package = "xbps"
        if sys.argv[1] == "dnf": package = "dnf"
        if sys.argv[1] == "yum": package = "yum"
        if sys.argv[1] == "zypper": package = "zypper"
        if sys.argv[1] == "eopkg": package = "eopkg"
        if sys.argv[1] == "pip3": package = "pip3"
        if sys.argv[1] == "pip2": package = "pip2"
        if sys.argv[1] == "pip": package = "pip"
        if sys.argv[1] == "apm": package = "apm"
        if sys.argv[1] == "emerge": package = "emerge"
        if sys.argv[1] == "pkg": package = "pkg"
        if sys.argv[1] == "chromebrew": package = "chromebrew"
        if sys.argv[1] == "homebrew": package = "homebrew"
        if sys.argv[1] == "nix": package = "nix"
        if sys.argv[1] == "npm": package = "npm"
        if sys.argv[1] == "snap": package = "snap"
        if sys.argv[1] == "flatpak": package = "flatpak"
        if sys.argv[1] == "yarn": package = "yarn"
        if sys.argv[1] == "bower": package = "bower"
        if sys.argv[1] == "gem": package = "gem"

    try:
        if package == " ":
            if package_file_read == "apt": package = "apt"
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
        print(bold + yellow + "Warnung: Fehlende Paketmanager Datei...")
        if package == " ": package = "null"
        print(reset + yellow + "Packagemanager gesetzt auf " + package)
    # Checks for command line argument


    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nDas ist Version: " + version)

    if package == " " or package == "null":  # Checks for command line argument
        user = input(pickManager())
        setup = "True"
    else:
        time.sleep(1)
        clear()
        setup = "False"
        # Sets the variable 'setup' to False

    # Asks user which package manager to use

    # We should do this with lists instead of a long if/else chain ~ Emil

    while setup == "True":  # Repeats until setup is not true
        if user == "1":
            setup = "false"
            package = "apt"  # Sets package manager to apt
            setpack("apt")
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
            print(red + "Fehler. Ungültiger Paketmanager")
            time.sleep(1)
            clear()
            user = input(pickManager())
            # Sets package manager

    if package != "pacman":
        if os.geteuid() != 0:
            print(bold + yellow + "Warnung: bitte führe TermGet als root aus")
            askreturn()

    if package != "pip" and package != "pip2" and package != "pip3" and package != "apm" and package != "npm" and package != "snap" and package != "flatpak":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Bitte wähle eine Aktion\n"
                "\n1. Suche ein Paket"
                "\n2. Installiere ein Paket"
                "\n3. Entferne ein Paket"
                "\n4. Aktualisiere alle Pakete"
                "\n5. Aktualisiere die Datenbank"
                "\n6. Aufräumen"
                "\n7. Credits"
                "\n8. Beenden"
                "\n9. Bash öffnen"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                print(reset + " ")
                if package == "apt": os.system("apt search " + user + " | grep " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paketmanager möchten Sie verwenden?\n"
                        "\n1. pacman"
                        "\n2. yay"))
                    if user1 == "1": os.system("pacman -Ss " + user + " | grep " + user)
                    if user1 == "2": os.system("yay -Ss " + user + " | grep " + user)
                elif package == "xbps": os.system("xbps-query -Rs " + user + " | grep " + user)
                elif package == "dnf": os.system("dnf search " + user + " | grep " + user)
                elif package == "yum": os.system("yum search " + user + " | grep " + user)
                elif package == "zypper": os.system("zypper search " + user + " | grep " + user)
                elif package == "eopkg": os.system("eopkg search " + user + " | grep " + user)
                elif package == "emerge": os.system("emerge -S " + user + " | grep " + user)
                elif package == "pkg": os.system("pkg search " + user + " | grep " + user)
                elif package == "chromebrew": os.system("crew search " + user + " | grep " + user)
                elif package == "homebrew": os.system("brew search " + user + " | grep " + user)
                elif package == "nix": os.system("nix search " + user + " | grep " + user)

                user = input(yellow + "\nHast du es gefunden? (y/n) " + reset)

                if user == "y" or user == "Y":

                    user = input(reset + "Bitte gib den Namen des zu installierenden Paketes ein: ")
                    print(reset + "")

                    if package == "apt": os.system("apt install " + user)
                    elif package == "pacman":
                        user1 = input(multichoicePrompt(
                            "Welchen Paketmanager möchten Sie verwenden ??\n"
                            "\n1. pacman"
                            "\n2. yay" + reset))
                        if user1 == "1":
                            if os.geteuid() != 0:
                                print(bold + red + "Bitte führe TermGet als root aus")
                            else: os.system("pacman -S " + user)
                        if user1 == "2":
                            if os.geteuid() == 0:
                                print(bold + red + "TermGet kann nicht als root ausgeführt werden, wenn yay benutzt wird")
                            else: os.system("yay -S " + user)
                    elif package == "xbps": os.system("xbps-install " + user)
                    elif package == "dnf": os.system("dnf install " + user)
                    elif package == "yum": os.system("yum install " + user)
                    elif package == "zypper": os.system("zypper install " + user)
                    elif package == "eopkg": os.system("eopkg install " + user)
                    elif package == "emerge": os.system("emerge " + user)
                    elif package == "pkg": os.system("pkg install " + user)
                    elif package == "chromebrew": os.system("crew install " + user)
                    elif package == "homebrew": os.system("brew install " + user)
                    elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib die zu installierenden Pakete an: ")
                print(reset + "")

                if package == "apt": os.system("apt install " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paketmanager möchten sie verwenden?\n"
                        "\n1. pacman"
                        "\n2. yay" + reset))
                    if user1 == "1":
                        if os.geteuid() != 0:
                            print(bold + red + "Bitte führen sie TermGet als root aus")
                        else: os.system("pacman -S " + user)
                    if user1 == "2":
                        if os.geteuid() == 0:
                            print(bold + red + "TermGet kann nicht als root ausgeführt werden, wenn sie yay benutzen")
                        else: os.system("yay -S " + user)
                elif package == "xbps": os.system("xbps-install " + user)
                elif package == "dnf": os.system("dnf install " + user)
                elif package == "yum": os.system("yum install " + user)
                elif package == "zypper": os.system("zypper install " + user)
                elif package == "eopkg": os.system("eopkg install " + user)
                elif package == "emerge": os.system("emerge " + user)
                elif package == "pkg": os.system("pkg install " + user)
                elif package == "chromebrew": os.system("crew install " + user)
                elif package == "homebrew": os.system("brew install " + user)
                elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "3":  # Remove MEOW
                clear()
                user = input(reset + "Bitte geben Sie die zu entfernenden Pakete an: ")
                print(reset + "")
                if package == "apt":
                    user1 = input(multichoicePrompt(
                        "Wie möchten sie das Paket entfernen ?\n"
                        "\n1. Remove, nur das Paket entfernen (schneller)"
                        "\n2. Purge, alles entfernen (räumt Speicher frei)" + reset))
                    clear()
                    if user1 == "1": os.system("apt remove " + user)
                    if user1 == "2": os.system("apt purge " + user)
                elif package == "pacman":
                    if os.geteuid() != 0:
                        print(bold + red + "Bitte führen sie TermGet als root aus")
                    else: os.system("pacman -Rs + user")
                elif package == "xbps": os.system("xbps-remove " + user)
                elif package == "dnf": os.system("dnf erase " + user)
                elif package == "yum": os.system("yum remove " + user)
                elif package == "zypper": os.system("zypper remove " + user)
                elif package == "eopkg": os.system("eopkg remove " + user)
                elif package == "emerge": os.system("emerge -C " + user)
                elif package == "pkg": os.system("pkg delete " + user)
                elif package == "chromebrew": os.system("crew remove " + user)
                elif package == "homebrew": os.system("brew uninstall " + user)
                elif package == "nix": os.system("nix-env -e " + user)
                askreturn()

            if user == "4":  # Updates Packages
                clear()
                if package == "apt":
                    user1 = input(multichoicePrompt(
                    "Möchten Sie auch die Datenbank neuladen ?\n"
                    "\n1. Ja"
                    "\n2. Nein" + reset))
                    if user1 == "1": os.system("apt update")
                    os.system("apt upgrade")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paketmanager möchten Sie verwenden?\n"
                        "\n1. pacman"
                        "\n2. yay" + reset))
                    if user1 == "1":
                        if os.geteuid() != 0:
                            print(bold + red + "Bitte führen sie TermGet als root aus")
                        else: os.system("pacman -Syu + user")
                    if user1 == "2":
                        if os.geteuid() == 0:
                            print(bold + red + "TermGet kann nicht als root ausgeführt werden, wenn sie yay benutzen")
                    else: os.system("yay -Syu --aur")
                elif package == "xbps": os.system("xbps-install -Su")
                elif package == "dnf":
                    os.system("dnf upgrade")
                    os.system("dnf distro-sync")
                elif package == "yum": os.system("yum update")
                elif package == "zypper":
                    os.system("zypper update && zypper up")
                    os.system("zypper dup")
                elif package == "eopkg": os.system("eopkg upgrade")
                elif package == "emerge":
                    os.system("emerge -u world")
                    os.system("emerge -uDN world")
                elif package == "pkg": os.system("pkg upgrade")
                elif package == "chromebrew": os.system("crew upgrade")
                elif package == "homebrew": os.system("brew upgrade")
                elif package == "nix": os.system("nix-env -u '*'")
                askreturn()

            if user == "5":  # Updates Database MEOW
                clear()
                if package == "apt": os.system("apt update")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Welchen Paketmanager möchten Sie verwenden?\n"
                        "\n1. pacman"
                        "\n2. yay"))
                    if user1 == "1":
                        if os.geteuid() != 0:
                            print(bold + red + "Bitte führen Sie TermGet als root aus")
                        else: os.system("pacman -Syy")
                    if user1 == "2":
                        if os.geteuid() == 0:
                            print(bold + red + "TermGet kann nicht als root ausgeführt werden, wenn sie yay benutzen")
                        else: os.system("yay -Syy")
                elif package == "xbps": os.system("xbps-install -S")
                elif package == "dnf": os.system("dnf clean expire-cache && dnf check-update")
                elif package == "zypper": os.system("zypper refresh zypper ref")
                elif package == "eopkg": os.system("eopkg ur")
                elif package == "emerge": os.system("layman -f")
                elif package == "yum": os.system("yum check-update")
                elif package == "pkg": os.system("pkg update")
                elif package == "chromebrew": print(bold+ yellow + "This feature is unavailable for chromebrew\n")
                elif package == "homebrew": os.system("brew update")
                elif package == "nix": os.system("nix-channel --update nixpkgs")
                askreturn()

            if user == "6":  # Cleans

                clear()

                if package == "apt":
                    os.system("apt purge --autoremove")
                    os.system("apt autoclean")
                    os.system("apt clean")
                elif package == "pacman":
                    os.system("pacman -Qdtq | pacman -Rs -")
                    os.system("pacman -Sc")
                elif package == "xbps":
                    os.system("xbps-remove -o")
                    os.system("xbps-remove -O")
                elif package == "dnf":
                    os.system("dnf autoremove")
                    os.system("dnf clean all")
                elif package == "yum":
                    os.system("yum clean all")
                    os.system("yum autoremove")
                elif package == "zypper":
                    os.system("zypper rm -u")
                    os.system("zypper clean")
                elif package == "eopkg":
                    os.system("eopkg delete-cache")
                    os.system("eopkg remove-orphans")
                elif package == "emerge":
                    os.system("emerge --depclean")
                    os.system("eclean distfiles")
                elif package == "pkg":
                    os.system("pkg clean")
                    os.system("pkg autoremove")
                elif package == "chromebrew": print(reset + "Dieses Feature existiert nicht unter chromebrew\n")
                elif package == "homebrew": print(reset + "Homebrew macht das automatisch :)\n")
                elif package == "nix": os.system("nix-collect-garbage -d")
                askreturn()

            if user == "7":  # Credits

                clear()
                print(credit + "\n")
                askreturn()

            if user == "8":
                print(reset)
                clear()
                quit()

            if user == "9":
                clear()
                print(reset + "Betrete Bash...")
                print(reset + "Drück CTRL+D oder gib \"exit\" ein um zurückzukehren.")
                os.system("bash")
                print(reset + "Rückkehr nach termget...")
                clear()


    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Bitte wählen sie eine Aktion\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Aktualisiere ein Paket"
                "\n4. Entferne ein Paket"
                "\n5. Zeige all pip-pakete an"
                "\n6. Credits"
                "\n7. Beenden"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte geben sie einen Suchbegriff ein: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"" + " | grep " + user)

                user = input(yellow + "\nHast du gefunden, nach was du gesucht hast? (y/n) " + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Bitte gib an, welches Paket Sie installieren möchten: ")
                    print(reset + "")

                    clear()
                    user = input(reset + "Bitte gib an, welches Paket Sie installieren möchten: ")
                    print(reset + "")
                    os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie installieren möchten: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie aktualisieren möchten: ")
                print(reset + "")
                os.system(package + " install --upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie entfernen möchten: ")
                print(reset + "")
                os.system(package + " uninstall \"" + user + "\"")
                askreturn()

            if user == "5":  # List
                clear()
                print(reset + "")
                user = input(multichoicePrompt(
                    "Bitte wählen Sie eine Aktion:\n"
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
                "Bitte wähle eine Aktion\n"
                "\n1. Suche nach Paketen"
                "\n2. Installiere ein Paket"
                "\n3. Aktualisiere ein Paket"
                "\n4. Entferne ein Paket"
                "\n5. Zeige alle installierten Pakete"
                "\n6. Credits"
                "\n7. Beenden"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Bitte geben sie einen Suchbegriff ein: ")
                print("")
                os.system("apm search " + user + " | grep " + user)

                user = input(yellow + "\nHast du gefunden, nach was du gesucht hast? (y/n) " + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Bitte gib an, welches Paket Sie installieren möchten: ")
                    print(reset + "")
                    os.system("apm install " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie installieren möchten: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie aktualisieren möchten: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Bitte gib an, welches Paket Sie entfernen möchten: ")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Bitte wählen sie eine Aktion:\n"
                    "\n1. Zeige alle Pakete"
                    "\n2. Zeige alle veralteten Pakete"))
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
            "Bitte wähle eine Aktion:\n"
            "\n1. Suche nach einem Snap"
            "\n2. Installiere einen Snaü"
            "\n3. Entferne einen Snap"
            "\n4. Zeige alle installieren Snaps"
            "\n5. Credits"
            "\n6. Beenden"))

            if user == "1":
                clear()
                user = input(reset + "Bitte geben Sie einen Suchbegriff ein: ")
                print("")
                os.system("snap find " + user + " | grep " + user)

                user = input(yellow + "\nHast du gefunden, wonach du gesucht hast? (y/n) " + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Geben sie das zu installierende Paket an: ")
                    print("")
                    os.system("snap install " + user)

                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Geben sie das zu installierende Paket an: ")
                print("")
                os.system("snap install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Geben sie das zu entfernede Paket an: ")
                print("")
                os.system("snap remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("Die aktuell installierten snaps sind: ")
                os.system("snap list")
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
            "Bitte wähle eine Aktion:\n"
            "\n1. Suche nach einem Snap"
            "\n2. Installiere einen Snaü"
            "\n3. Entferne einen Snap"
            "\n4. Zeige alle installieren Snaps"
            "\n5. Credits"
            "\n6. Beenden"))

            if user == "1":
                clear()
                user = input(reset + "Bitte geben Sie einen Suchbegriff ein: ")
                print("")
                os.system("flatpak search " + user + " | grep " + user)

                user = input(yellow + "\nHast du gefunden, wonach du gesucht hast? (y/n) " + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Geben sie das zu installierende Paket an: ")
                    print("")
                    os.system("flatpak install flathub " + user)
                    askreturn()


                askreturn()
            if user == "2":
                clear()
                user = input(reset + "Geben sie das zu installierende Paket an: ")
                print("")
                os.system("flatpak install flathub " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Geben sie das zu entfernende Paket an: ")
                print("")
                os.system("flatpak remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("Die aktuell installierten flatpaks sind: ")
                os.system("flatpak list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()


    if package == "yarn" or package == "npm":
        pkg_dir = input(reset + "Pfad zu deinem Projekt: ")
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "\n1. Suche nach einem Paket"
            "\n2. Installiere ein Paket"
            "\n3. Entferne ein Paket"
            "\n4. Zeige alle installierten Pakete an"
            "\n5. Update alle installieren Pakete"
            "\n5. Credits"
            "\n6. Beenden"))

            if user == "1":
                clear()
                print("")
                if package == "npm":
                    user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                    os.system("npm search " + user + " | grep " + user)
                    user = input(yellow + "\nHast du was gefunden? (y/n)" + reset)

                    if user == "y" or user == "Y":
                        os.system("npm install " + user)
                        askreturn()

                elif package == "yarn":
                    print("Yarn hat keine Suchfunktion. Möchtest du auf der Yarn Website mit deinem Browser suchen? (y/n) ")
                    if user == "y" or "Y":
                        user = input(reset + "Bitte gib einen Suchbegriff ein: ")
                        webbrowser.open_new("https://yarnpkg.com/en/packages?q=" + user + "&p=1")
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gib das zu installierende Paket an: ")
                print("")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm install " + user)
                if package == "yarn": os.system("yarn install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gib das zu entfernende Paket an:")
                print("")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm uninstall " + user)
                elif package == "yarn": os.system("yarn remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("Die installierten Pakete sind: ")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm ls")
                elif package == "yarn": os.system("yarn list")
                askreturn()

            if user == "5":
                clear()
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm update")
                if package == "yarn": os.system("yarn update")
                askreturn()

            if user == "6":
                clear()
                credits()

            if user == "7":
                print(reset)
                quit()

    if package == "bower":
        while True:
            clear()
            user = input(multichoicePrompt(
                "Bitte wähle eine Aktion:\n"
                "1. Suche nach einem Paket\n"
                "2. Installiere ein Paket\n"
                "3. Entferne ein Paket\n"
                "4. Update ein Paket\n"
                "5. Zeige alle installieren Pakete an\n"
                "6. Credits\n"
                "7. Beenden"))

            if user == "1":
                clear()
                user = input(reset + "Gib einen Suchbegriff ein: ")
                print("")
                os.system("bower search " + user)
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gib das zu installierende Paket an: ")
                print("")
                os.system("bower install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gib das zu entfernende Paket an: ")
                print("")
                os.system("bower uninstall " + user)
                askreturn()

            if user == "4":
                clear()
                os.system("bower update")
                askreturn()

            if user == "5":
                clear()
                os.system("bower list")
                askreturn()

            if user == "6":
                clear()
                credits()

            if user == "7":
                print(reset)
                quit()

    if package == "gem":
        while True:
            clear()
            user = input(multichoicePrompt(
                "Bitte wähle eine Aktion:\n"
                "1. Suche einen Gem\n"
                "2. Installiere einen Gem\n"
                "3. Entferne einen Gem\n"
                "4. Zeige alle installierten Gems\n"
                "5. Credits"
                "6. Beenden"))

            if user == "1":
                clear()
                user = input(reset + "Gib einen Suchbegriff ein: ")
                print("")
                os.system("gem search " + user)
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Gib den zu installierenden Gem an: ")
                print("")
                os.system("gem install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Gib den zu entfernenden Gem an: ")
                print("")
                os.system("gem uninstall " + user)
                askreturn()

            if user == "4":
                clear()
                os.system("gem list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()

except KeyboardInterrupt:
        clear()
        print(red + "Fehler: Tastaturabbruch. Verlassen" + reset) # moo
        quit()
