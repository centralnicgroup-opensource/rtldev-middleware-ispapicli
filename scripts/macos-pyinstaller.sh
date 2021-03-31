#!/bin/bash
echo "Executing Pyinstaller MacOS..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
cd dist
sudo chmod +x ispapicli
cd ..
zip -r macos-binary-latest.zip dist
mv macos-binary-latest.zip ../../