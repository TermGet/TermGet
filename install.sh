#!/bin/sh

#Install Script made by SudoLinux
#If you want to update your program if you made changes. Please run:
# root@localhost ~ $ chmod +x install.sh
# root@localhost ~ $ ./install.sh
echo "Getting ready to install in 5 seconds"
echo ""
echo "Press CTRL+X to abort if this was an accident"
echo ""
sleep 5
echo ">>> setting up directories"
rm -rf ~/.termget/
mkdir ~/.termget/
echo ">>> copying program to ~/.termget"
cp termget.py ~/.termget/termget.py
echo ">>> creating alias into .bashrc"
echo 'alias termget="python3 ~/.termget/termget.py"' >> ~/.bashrc
alias termget="python3 ~/.termget/termget.py"
echo ""
echo "Note: From now on, any changes made to the code"
echo "must be ran under ./update.sh"
echo ""
echo ">>> Done!"
