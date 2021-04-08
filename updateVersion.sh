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

mv artifacts/macos-binary/macos-binary-latest.zip "artifacts/macos-binary/macos-binary-${newversion}.zip"
mv artifacts/linux-binary/linux-binary-latest.zip "artifacts/linux-binary/linux-binary-${newversion}.zip"
mv artifacts/win-binary/win-binary-latest.zip "artifacts/win-binary/win-binary-${newversion}.zip"
