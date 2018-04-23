#!/bin/bash

if [ -e /usr/bin/termget ];
then
  echo "Old termget build found, please remove /usr/bin/termget."
  echo "I won't remove it for you..."
  echo "Try removing with: sudo rm -rf /usr/bin/termget"
  exit
fi

echo ">>> setting up directories"
rm -rf ~/.termget/
mkdir ~/.termget/
echo ">>> copying program to ~/.termget"
cp termget.py ~/.termget/termget.py
echo ">>> generating empty file"
> ~/.termget/termget-package-manager
echo ">>> installing"
echo "#!/bin/bash
python3 ~/.termget/termget.py \$1 \$2 \$3 \$4" >> ~/.termget/termget.sh
chmod +x ~/.termget/termget.sh
sudo cp ~/.termget/termget.sh /usr/local/bin/termget
echo ""
echo ">>> Done!"
