#!/bin/bash
echo "Executing Pyinstaller Windows..."
pip install pyinstaller
cd .\hexonet\ispapicli\
pyinstaller ispapicli.spec
Compress-Archive -Path .\dist -DestinationPath ..\..\win-binary-latest.zip