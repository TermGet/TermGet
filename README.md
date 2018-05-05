# What is TermGet?
TermGet is a project made by PizzaLovingNerd, several others.

TermGet is a frontend for:

 - apt-get
 - xbps
 - dnf
 - eopkg
 - zypper
 - pacman
 - yaourt
 - homebrew
 - apm
 - pkg
 - chromebrew
 - emerge
 - pip
 - sol  (Coming Soon)
 - chocolatey (Coming Soon)

## GUI Mode!

GUI should show up! if not, it will tell you how to install the TK toolkit, which is required to show the window.

    termget gui

Termget also has a GUI! Run the GUI with the following command:

## What are some of it's features

 - Simple, easy to use interface
 - Works in the command line
 - Has a GUI optionally
 - Supports a lot of package managers
 - Feature rich
 - Works on any Linux/ChromeOS/Mac distribution (and soon Windows)
 - Great for introducing package management to new users
 - Code is easy to modify.

## How do I install TermGet on Linux, BSD, and MacOS.

### Installing Python3

To install TermGet, we need to install python3. To check ot see if it's already installed type:

    python3 --version

Install off your operating system's respository.
If you on MacOS, download it from https://python.org

After you install python3, download TermGet.

Before you run the install TermGet there are some OS specific dependencies.

### Arch Linux Dependencies

If you are on Arch Linux, you need to install yaourt in order to use the AUR. To do this, open a terminal and type:

    git clone https://aur.archlinux.org/package-query.git
    cd package-query
    makepkg -si
    cd ..
    git clone https://aur.archlinux.org/yaourt.git
    cd yaourt
    makepkg -si
    cd ..

### Mac OS Dependencies

If you are on Mac OS, you need to install Homebrew. To do this open a terminal and type:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


### Downloading and Installing TermGet

Now we need to download TermGet

To get an alpha build, please clone the [TermGet GitHub repository](https://github.com/TermGet/TermGet)

To get a beta or release build, please go to the releases tab, of the [TermGet GitHub repository](https://github.com/TermGet/TermGet/releases)

Extract TermGet somewhere and open a terminal window.

Now set your current directory in the terminal to the extracted TermGet folder, (example: ```cd ~/Downloads/TermGet-2.1.3```)

Now type:
    
    sudo bash install.sh

## First Time Setup On Linux, BSD, and MacOS.

After installing, run TermGet using

    termget

you should get a message that sort of looks like this:

    Please choose a package manager

    1. apt-get (For Debian, and Debian based systems.)
    2. xbps (For Void Linux, and Void Linux based systems)
    3. dnf (For Fedora, and Fedora based systems)
    4. zypper (For OpenSUSE, and OpenSUSE based systems)
    5. eopkg (For Solus, and Solus based systems)
    6. pacman (For Arch, and Arch based systems)
    .....list goes on

Choose your distribution's package manager using the number. My package manager is eopkg, so I would type "5" and press enter. 

If you are on MacOS type ```11``` for homebrew.

## How do I install TermGet on ChromeOS
### Warning: TermGet on ChromeOS is not offically supported. TermGet on ChromeOS is also super buggy.

First put your Chromebook in [developer mode](https://www.howtogeek.com/210817/how-to-enable-developer-mode-on-your-chromebook/ "developer mode").

Now, Open Crosh, and type ```shell```. Check if Python3 is already installed on your system. Do so by typing

    python3 --version

If it is your good to go to the next step.

If not, then [watch this video](https://www.youtube.com/watch?v=X7Y8b2S3nEA)

If you would rather read instead of a video, [click here](https://wsvincent.com/install-python3-chromebook/)

Once you have installed python, we need to install Chromebrew. To do this type:

    wget -q -O - https://raw.github.com/skycocker/chromebrew/master/install.sh | bash

    -- or --

    curl -Ls git.io/vddgY | bash

Now download TermGet and cd into it, then run

    bash install.sh

and it will install, if you get errors report it to the github issues.

That's it, type "termget" into the prompt and you should be good.

## How do I use TermGet on Linux, BSD, MacOS, and ChromeOS

This section gets updated with every release, if you are using an alpha or beta build, there might be extra features that aren't on this section of the README file.

TermGet is really easy to use. To run it, all you have to do is open a terminal, and type:

    termget


Just select using the number (for example if my package manager was apt-get, I would type the number 1, and press enter).

Once your package manager has been chosen, you will get a message like this:

    Please choose an action

    1. Search for packages
    2. Install an application
    3. Remove an application
    4. Update all packages
    5. Update Database
    6. Clean
    7. Credits
    8. Exit
    9. Enter shell

*We will be using "eopkg" in the examples below.*
*Results may vary for other package managers*

### Searching for Packages

Search searches for packages. This is what it looks like when I search Minetest:

    Please enter search query: minetest

    minetest         - Minetest, an open source infinite-world block sandbox game with survival and crafting.
    minetest-dbginfo - Debug symbols for minetest

    Press enter to continue

### Installing a package

Installing a package downloads and installs a package. This is what it looks like if I install Minetest:

    Total size of package(s): 6.73 MB
    Downloading 1 / 1
    Package minetest found in repository Solus
    minetest-0.4.16-4-1-x86_64.eopkg [cached]
    Installing 1 / 1
    minetest-0.4.16-4-1-x86_64.eopkg [cached]
    Installing minetest, version 0.4.16, release 4
    Extracting the files of minetest
    Installed minetest
	    [✓] Syncing filesystems                                                 success
	    [✓] Updating icon theme cache: hicolor                                  success
	    [✓] Updating desktop database                                           success
	    [✓] Updating manpages database                                          success

    Press enter to continue

### Removing a package

  Removing a package uninstalls a package. This is what it looks like if I install Minetest:

      The following list of packages will be removed
      in the respective order to satisfy dependencies:
	  minetest
	  Removing package minetest
	  Removed minetest
	     [✓] Syncing filesystems                                                success
	     [✓] Updating icon theme cache: hicolor                                 success
	     [✓] Updating desktop database                                          success
	     [✓] Updating manpages database                                    	    success

	  Press enter to continue

### Updating all packages

Updating all packages updates EVERYTHING ON THE SYSTEM. Here's what it looks like when you have nothing to upgrade:

	  Updating repositories
	  Updating repository: Solus

	  eopkg-index.xml.xz.sha1sum     (40.0  B)100%    289.47 KB/s [00:00:00] [complete]
	  Solus repository information is up-to-date.
	  No packages to upgrade.

	  Press enter to continue

### Updating the repository

Updating the repository, checks the repository for new versions of packages. It is recommended to do this before updating. Here it looks like when the repository is up-to-date:

	  Updating repository: Solus
	  eopkg-index.xml.xz.sha1sum     (40.0  B)100%    394.80 KB/s [00:00:00] [complete]

	  Solus repository information is up-to-date.

	  Press enter to continue

### Cleaning

Cleaning helps save hard drive space. It does this by deleting cache, and deleting unneeded dependencies. Here is what it looks like:

	  Cleaning package cache /var/cache/eopkg/packages...
	  Cleaning source archive cache /var/cache/eopkg/archives...
	  Cleaning temporary directory /var/eopkg...
	  Removing cache file /var/cache/eopkg/installdb.cache...
	  Removing cache file /var/cache/eopkg/componentdb.cache...
	  The following list of packages will be removed
	  in the respective order to satisfy dependencies:
	  irrlicht
	  Do you want to continue? (yes/no)yes
	  Removing package irrlicht
	  Removed irrlicht
	     [✓] Syncing filesystems    			                                      success
	     [✓] Updating dynamic library cache                                     success

	  Press enter to continue

### Entering the Shell
If you want to run a shell command like to add a PPA or something like that, you can open the shell and run the command, then type ```exit``` or press CTRL-D to leave the shell.

## Changing the package manager

### Temporarily (On Linux, BSD, and macOS.)

To Temporarily change the package manager used, use an argument. For example, if I wanted to temporally change it to apt-get, I would type

    sudo termget apt-get

### Permanently (On Linux, BSD, and macOS)
Run the following command in a terminal, then the first setup script will start next time you run termget.

If you are rnuning a version of TermGet after 2.0.1 run:

    sudo rf /usr/local/share/termget/termget-package-manager && > /usr/local/share/termget/termget-package-manager

If you are running a version of TermGet before 2.1.0 run:

    rf ~/.termget/termget-package-manager && > ~/.termget/termget-package-manager


## Installing TermGet on Windows
TermGet isn't out for Windows yet.

## Using PIP

To run TermGet with PIP, just run:

```termget pip```

---or---

```termget pip2```

---or---

```termget pip3```

## Using APM

To run TermGet with APM, just run:

```termget apm```

## License

Licensed under LGPLv3

The license is stated in the LICENSE document on the root directory
