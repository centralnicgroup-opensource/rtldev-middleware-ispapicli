#!/bin/bash
echo "Executing Pyinstaller Windows..."
pip install pyinstaller
cd .\hexonet\ispapicli\
pyinstaller --onefile ispapicli.py --add-data 'icons;data/icons'
Compress-Archive -Path .\dist -DestinationPath ..\..\win-binary-latest.zip