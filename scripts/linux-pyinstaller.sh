#!/bin/bash
echo "Executing Pyinstaller Ubuntu..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
mkdir dist/scripts
cp  ../../scripts/linux-download.sh dist/scripts
cp  ../../scripts/win-download.ps1 dist/scripts
sudo chmod +x dist/ispapicli
zip -r linux-binary-latest.zip dist
mv linux-binary-latest.zip ../../