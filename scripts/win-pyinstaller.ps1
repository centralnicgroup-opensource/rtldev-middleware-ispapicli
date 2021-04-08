echo "Executing Pyinstaller Windows..."
pip install pyinstaller
cd .\hexonet\ispapicli\
pyinstaller --onefile ispapicli.py --add-data 'icons;data/icons'
cd .\dist
Compress-Archive -Path ispapicli -DestinationPath ..\..\..\win-binary-latest.zip