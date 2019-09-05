#!/bin/bash

# autodetection. If the incorrect one shows, it is possible that you have a program on your system that has the same name as a package manager.
echo "Hello, which language would you like to use?
Hallo, welche Sprache möchten Sie verwenden?"
echo "1. English"
echo "2. Deutsch"

read lang

#English installation
if [ "$1" != "--no-detection" ] && [ "$lang" == "1" ]; then
	if [[ $(which brew 2> /dev/null) ]]; then
		echo -n "Why do you torture yourself with using macOS? Fine, homebrew will be used. Is this correct? [y/n] "
		pm=homebrew
	elif [[ $(which xbps-install 2> /dev/null) ]]; then
		echo -n "A Void or Void-based system has been detected. xbps will be used. Is this correct? [y/n] "
		pm=xbps
	elif [[ $(which dnf 2> /dev/null) ]]; then
		echo -n "A Fedora or Fedora-based system has been detected. dnf will be used. Is this correct? [y/n] "
		pm=dnf
	elif [[ $(which yum 2> /dev/null) ]]; then
		echo -n "An RHEL or RHEL-based system has been detected. yum will be used. Is this correct? [y/n] "
		pm=yum
	elif [[ $(which zypper 2> /dev/null) ]]; then
		echo -n "An openSUSE or openSUSE-based system has been detected. zypper will be used. Is this correct? [y/n] "
		pm=zypper
	elif [[ $(which eopkg 2> /dev/null) ]]; then
		echo -n "A Solus or Solus-based system has been detected. eopkg will be used. Is this correct? [y/n] "
		pm=eopkg
	elif [[ $(which crew 2> /dev/null) ]]; then
		echo -n "chromebrew (an unoffical Chrome/Chromium OS package manager) has been detected. Is this correct? [y/n] "
		pm=chromebrew
	elif [[ $(which emerge 2> /dev/null) ]]; then
		echo -n "A Gentoo or Gentoo-based system has been detected. emerge will be used. Is this correct? [y/n] "
		pm=emerge
		echo "Good thing you don't have to compile this"
	elif [[ $(which pkg 2> /dev/null) ]]; then
		echo -n "You're one of those weird FreeBSD users, aren't you? If so, pkg will be used. Is this correct? [y/n] "
		pm=pkg
	elif [[ $(which pacman 2> /dev/null) ]]; then
		echo -n "An Arch or Arch-based system has been detected. pacman will be used. Is this correct? [y/n] "
		pm=pacman
	elif [[ $(which apt 2> /dev/null) ]]; then
		echo -n "A Debian or Debian-based system has been detected. apt will be used. Is this correct? [y/n] "
		pm=apt
	elif [[ $(which nix 2> /dev/null) ]]; then
		echo -n "A NixOS or NixOS-based system has been detected. nix will be used. Is this correct? [y/n] "
		pm=nix
	else
		echo -n "A package manager has failed to be detected. If you proceed to install the program, termget will ask
	you to set a package manager manually on first launch. Proceed to install? [y/n] "
	fi

	read answer
	if [ $answer != "y" ] && [ -z $pm ]; then
		echo "Installation aborted."
		exit
	elif [ $answer != "y" ] && [ -n $pm ]; then
		echo -n "A package manager has failed to be detected. If you proceed to install the program, termget will ask
	you to set a package manager manually on first launch. Proceed to install? [y/n] "
		read answer2
		if [ $answer2 != "y" ]; then
			echo "Installation aborted."
			exit
		else
			pm=
		fi
	fi


#German installation
elif [ "$1" != "--no-detection" ] && [ "$lang" == "2" ]; then
	if [[ $(which brew 2> /dev/null) ]]; then
		echo -n "Warum schadest du dir selbst mit macOS? Ok, homebrew wird benutzt. Ist das korrekt? [y/n] "
		pm=homebrew
	elif [[ $(which xbps-install 2> /dev/null) ]]; then
		echo -n "Void oder ein Void-basiertes System wurde erkannt. xbps wird benutzt. Ist das korrekt? [y/n] "
		pm=xbps
	elif [[ $(which dnf 2> /dev/null) ]]; then
		echo -n "Fedora oder ein Fedora-basiertes System wurde erkannt. dnf wird benutzt. Ist das korrekt? [y/n] "
		pm=dnf
	elif [[ $(which zypper 2> /dev/null) ]]; then
		echo -n "Ein openSUSE oder openSUSE-basiertes System wurde erkannt. zypper wird benutzt. Ist das korrekt? [y/n] "
		pm=zypper
	elif [[ $(which eopkg 2> /dev/null) ]]; then
		echo -n "Ein Solus oder SOlus-basiertes System wurde erkannt. eopkg wird benutzt. Ist das korrekt? [y/n] "
		pm=eopkg
	elif [[ $(which crew 2> /dev/null) ]]; then
		echo -n "chromebrew (ein inoffizieller Chrome/Chromium OS paket manager) wurde erkannt. Ist das korrekt? [y/n] "
		pm=chromebrew
	elif [[ $(which emerge 2> /dev/null) ]]; then
		echo -n "Ein Gentoo oder Gentoo-based System wurde erkannt. emerge wird benutzt. Ist das korrekt? [y/n] "
		pm=emerge
		echo "Zum Glück muss das nicht kompiliert werden"
	elif [[ $(which pkg 2> /dev/null) ]]; then
		echo -n "Du bist ein der seltsamen FreeBSD Benutzer oder? Nun denn, pkg wird benutzt. Ist das korrekt? [y/n] "
		pm=pkg
	elif [[ $(which pacman 2> /dev/null) ]]; then
		echo -n "Ein Arch oder Arch-basiertes System wurde erkannt. pacman wird benutzt. Ist das korrekt? [y/n] "
		pm=pacman
	elif [[ $(which apt 2> /dev/null) ]]; then
		echo -n "Ein Debian oder Debian-basiertes System wurde erkannt. apt wird benutzt. Ist das korrekt? [y/n] "
		pm=apt
	elif [[ $(which nix 2> /dev/null) ]]; then
		echo -n "Ein Nix-OS oder Nix-OS-basiertes System wurde erkannt. 'nix' wird benutzt (Also der Paket-Manager 'nix'). Ist das korrekt? [y/n] "
		pm=nix
	else
		echo -n "Fehler bei der Erkennung des Paket-Managers. Fährst du fort fragt Termget dich beim ersten start nach dem Paket-Manager. Weitermachen mit der Installation? [y/n] "
	fi

	read answer
	if [ $answer != "y" ] && [ -z $pm ]; then
		echo "Installation abgebrochen."
		exit
	elif [ $answer != "y" ] && [ -n $pm ]; then
		echo -n "Fehler bei der Erkennung des Paket-Managers. Fährst du fort fragt Termget dich beim ersten start nach dem Paket-Manager. Weitermachen mit der Installation? "
		read answer2
		if [ $answer2 != "y" ]; then
			echo "Installation abgebrochen."
			exit
		else
			pm=
		fi
	fi
fi

echo "setting up directories"

# some operating systems don't have a /usr/local/, so it will create it & child directories if necessary
sudo bash -c "mkdir /usr/local 2> /dev/null"
sudo bash -c "mkdir /usr/local/bin 2> /dev/null"
sudo bash -c "mkdir /usr/local/share 2> /dev/null"

sudo bash -c "mkdir /usr/local/share/termget 2> /dev/null" # create new config directory if one doesn't exist

if [ "$lang" == "1" ]; then
	echo "... Installing TermGet to /usr/local/bin."
	chmod +x termget.py
	sudo cp termget.py /usr/local/bin/termget # copy program to PATH

elif [ "$lang" == "2" ]; then
	echo "... Installiere TermGet nach /usr/local/bin."
	chmod +x termget-deutsch.py
	sudo cp termget-deutsch.py /usr/local/bin/termget # copy program to PATH
fi

if [ "$1" != "--no-detection" ]; then
	echo "... Generating package file."
	sudo bash -c "echo -n $pm > /usr/local/share/termget/termget-package-manager" # copy package file to config directory
fi

if [ "$lang" == "1" ]; then
	echo -e "\nSuccessfully Installed! If TermGet is not launching, restart your session to reset the PATH."

elif [ "$lang" == "2" ]; then
	echo -e "\nErfolgreich installiert! Falls es nicht funktioniert starte deine Sitzung neu damit der PATH zurückgesetzt wird."
fi
