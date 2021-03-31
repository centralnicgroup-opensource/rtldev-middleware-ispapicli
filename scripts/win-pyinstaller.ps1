echo "Executing Pyinstaller Windows..."
pip install pyinstaller
cd .\hexonet\ispapicli\
pyinstaller --onefile ispapicli.py --add-data 'icons;data/icons'
mkdir dist\scripts
move ..\..\scripts\linux-download.sh, ..\..\scripts\win-download.ps1 .\dist\scripts\
Compress-Archive -Path .\dist -DestinationPath ..\..\win-binary-latest.zip