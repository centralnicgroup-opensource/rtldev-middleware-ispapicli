#!/bin/bash
echo "Executing Pyinstaller Ubuntu..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
cd dist || exit
sudo chmod +x ispapicli
zip -r linux-binary-latest.zip ispapicli
mv linux-binary-latest.zip ../../../