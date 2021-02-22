#!/bin/bash
echo "Executing pyinstaller..."
pip install pyinstaller
cd hexonet/ispapicli || exit
pyinstaller --onefile ispapicli.py
cd dist
sudo chmod +x ispapicli
mkdir bin
mv ispapicli bin
cp -r ../commands .
cp -r ../icons .
cp -r ../config .
cd ..
zip -r linux-binary.zip dist
mv linux-binary.zip ../../