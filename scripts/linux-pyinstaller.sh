#!/bin/bash
echo "Executing Pyinstaller Ubuntu..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py --add-data 'icons:data/icons'
cd dist
sudo chmod +x ispapicli
cd ..
zip -r linux-binary-latest.zip dist
mv linux-binary-latest.zip ../../