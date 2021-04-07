#!/bin/bash
echo "Executing download script on linux..."
file=linux-binary-latest.zip
if pkill ispapicli;
then
    if rm ispapicli;
    then
        cp dist/ispapicli .
        sudo chmod +x ispapicli
        sudo ./ispapicli &
        echo "Cleaning..."
        rm $file
        rm -r dist
        echo "Cleaning finished"
    else
        echo FAIL
    fi
else
    echo FAIL
fi