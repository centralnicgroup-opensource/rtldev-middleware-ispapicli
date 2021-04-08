#!/bin/bash

# THIS SCRIPT UPDATES THE HARDCODED VERSION
# IT WILL BE EXECUTED IN STEP "prepare" OF
# semantic-release. SEE package.json

# version format: X.Y.Z
newversion="$1";
sed -i "s/[0-9]\+\.[0-9]\+\.[0-9]\+/${newversion}/g" VERSION
sed -i "s/__version__ = \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/__version__ = \"${newversion}\"/g" hexonet/ispapicli/__init__.py
sed -i "s/__version__ = \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/__version__ = \"${newversion}\"/g" hexonet/ispapicli/modules/core.py
sed -i "s/__version__ = \"[0-9]\+\.[0-9]\+\.[0-9]\+\"/__version__ = \"${newversion}\"/g" hexonet/ispapicli/gui/mainframe.py

mv artifacts/macos-binary-latest.zip mv "artifacts/macos-binary-${newversion}.zip"
mv artifacts/linux-binary-latest.zip mv "artifacts/linux-binary-${newversion}.zip"
mv artifacts/win-binary-latest.zip mv "artifacts/win-binary-${newversion}.zip"
