#!/bin/bash
echo "Executing Pyinstaller Ubuntu..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
sudo chmod +x dist/ispapicli
cp -r ../../scripts dist
zip -r linux-binary-latest.zip dist
mv linux-binary-latest.zip ../../