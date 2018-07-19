#!/bin/bash

# autodetection. If the incorrect one shows, it is possible that you have a program on your system that has the same name as a package manager.
echo "Hello, can you tell what language do you want to use ?"
echo "1. English"
echo "2. Deutsch"

read lang

if [ "$1" != "--no-detection" ]; then
	if [[ $(which brew 2> /dev/null) ]]; then
		echo -n "Why do you torture yourself with using Mac OS? Fine, homebrew will be used. Is this correct? [y/n] "
		pm=homebrew
	elif [[ $(which xbps-install 2> /dev/null) ]]; then
		echo -n "A Void or Void-based system has been detected. XBPS will be used. Is this correct? [y/n] "
		pm=xbps
	elif [[ $(which dnf 2> /dev/null) ]]; then
		echo -n "A Fedora or Fedora-based system has been detected. DNF will be used. Is this correct? [y/n] "
		pm=dnf
	elif [[ $(which zypper 2> /dev/null) ]]; then
		echo -n "An openSUSE or openSUSE-based system has been detected. Zypper will be used. Is this correct? [y/n] "
		pm=zypper
	elif [[ $(which eopkg 2> /dev/null) ]]; then
		echo -n "A Solus or Solus-based system has been detected. Eopkg will be used. Is this correct? [y/n] "
		pm=eopkg
	elif [[ $(which crew 2> /dev/null) ]]; then
		echo -n "Chromebrew (an unoffical Chrome/Chromium OS package manager) has been detected. Is this correct? [y/n] "
		pm=chromebrew
	elif [[ $(which emerge 2> /dev/null) ]]; then
		echo -n "A Gentoo or Gentoo-based system has been detected. Emerge will be used. Is this correct? [y/n] "
		pm=emerge
		echo "Good thing you don't have to compile this"
	elif [[ $(which pkg 2> /dev/null) ]]; then
		echo -n "You're one of those weird FreeBSD users, aren't you? If so, pkg will be used. Is this correct? [y/n] "
		pm=pkg
	elif [[ $(which pacman 2> /dev/null) ]]; then
		echo -n "An Arch or Arch-based system has been detected. Pacman will be used. Is this correct? [y/n] "
		pm=pacman
	elif [[ $(which apt-get 2> /dev/null) ]]; then
		echo -n "A Debian or Debian-based system has been detected. Apt-get will be used. Is this correct? [y/n] "
		pm=apt-get
	elif [[ $(which nix 2> /dev/null) ]]; then
		echo -n "A NixOS or NixOS-based system has been detected. Nix will be used. Is this correct? [y/n] "
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
fi

echo "setting up directories"

# some operating systems don't have a /usr/local/, so it will create it & child directories if necessary
sudo bash -c "mkdir /usr/local 2> /dev/null"
sudo bash -c "mkdir /usr/local/bin 2> /dev/null"
sudo bash -c "mkdir /usr/local/share 2> /dev/null"

sudo bash -c "mkdir /usr/local/share/termget 2> /dev/null" # create new config directory if one doesn't exist

if [ "$lang" == "1" ]; then
	echo "... installing program to /usr/local/bin"
	chmod +x termget.py
	sudo cp termget.py /usr/local/bin/termget # copy program to PATH

elif [ "$lang" == "2" ]; then
	echo "... installing program to /usr/local/bin"
	chmod +x termget-deutsch.py
	sudo cp termget-deutsch.py /usr/local/bin/termget # copy program to PATH
fi

if [ "$1" != "--no-detection" ]; then
	echo "... generating package file"
	sudo bash -c "echo -n $pm > /usr/local/share/termget/termget-package-manager" # copy package file to config directory
fi

echo -e "\nSuccessfully Installed! If it's not working, try logging out and logging back in again to reset the PATH."
