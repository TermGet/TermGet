#!/bin/bash

if [ -e /usr/local/bin/termget ];
then
  echo "Old build of TermGet found. Removing it ..."
  sudo rm -rf /usr/local/bin/termget
fi

if [[ $(which apt-get 2> /dev/null) ]]; then
	echo -n "A Debian or Debian-based system has been detected. Apt-get will be used. Is this correct? [y/n] "
	pm=apt-get
elif [[ $(which brew 2> /dev/null) ]]; then
        echo -n "Why do you torture yourself with using Mac OS? Fine, homebrew will be used. Is this correct? [y/n] "
        pm=homebrew
elif [[ $(which pacman 2> /dev/null) ]]; then
	echo -n "An Arch or Arch-based system has been detected. Pacman will be used. Is this correct? [y/n] "
	pm=pacman
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
elif [[ $(which pkg 2> /dev/null) ]]; then
        echo -n "You're one of those weird FreeBSD users, aren't you? If so, pkg will be used. Is this correct? [y/n] "
        pm=pkg
else
	echo -n "A package manager has failed to be detected. If you proceed to install the program, termget will ask 
you to set a package manager manually on first launch. Proceed to install? [y/n] "
fi

read answer
if [ $answer != "n" ] && [ -z $pm ]; then
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

echo ">>> setting up directories"
rm -rf ~/.termget/
sudo mkdir /usr/local/share/termget
echo ">>> copying program to ~/.termget"
sudo cp termget.py /usr/local/bin/
echo ">>> generating package file"
sudo bash -c "echo -n $pm > ~/.termget/termget-package-manager"
echo ">>> installing"
chmod +x termget
sudo cp termget /usr/local/bin/
echo ""
echo ">>> Done!"
