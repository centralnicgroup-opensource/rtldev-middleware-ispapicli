#!/bin/bash
echo "Executing download script on linux..."
version=$1
file=linux-binary-latest.zip
if wget https://github.com/hexonet/ispapicli/releases/download/"$version"/"$file";
then
    echo "Download finished"
    echo "Unzipping new file"
    if unzip -o $file;
    then
        pkill ispapicli
        cp -r dist/ispapicli .
        ./ispapicli &
        echo "Cleaning..."
        rm $file
        rm -r dist
        echo "Cleaning finished"
    else
        echo FAIL Unzipping
    fi
else
    echo FAIL Downloading
fi


