#!/bin/sh

#Install Script made by SudoLinux
#If you want to update your program if you made changes. Please run:
# root@localhost ~ $ chmod +x install.sh
# root@localhost ~ $ ./install.sh
echo "Getting ready to install in 5 seconds"
echo ""
echo "Press CTRL+C to abort if this was an accident"
echo ""
sleep 5
echo ">>> setting up directories"
rm -rf ~/.termget/
mkdir ~/.termget/
echo ">>> copying program to ~/.termget"
cp termget.py ~/.termget/termget.py
echo ">>> generating empty file"
> ~/.termget/termget-package-manager
echo ">>> installing"
sudo cp ~/.termget/termget.py /usr/bin/termget
echo ""
echo ">>> Done!"
