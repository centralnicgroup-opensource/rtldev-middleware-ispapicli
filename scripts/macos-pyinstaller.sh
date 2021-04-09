#!/bin/bash
echo "Executing Pyinstaller MacOS..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
cd dist || exit
sudo chmod +x ispapicli
zip -r macos-binary-latest.zip ispapicli
mv macos-binary-latest.zip ../../../