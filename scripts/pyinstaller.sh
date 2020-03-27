#!/bin/bash
echo "Executing pyinstaller..."
cd hexonet/isapicli || exit
pyinstaller --onefile isapicli.py