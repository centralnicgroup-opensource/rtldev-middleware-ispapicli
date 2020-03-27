#!/bin/bash
pycodestyle --first --show-source --show-pep8 setup.py hexonet/ispapicli/*.py hexonet/ispapicli/modules/*.py  tests/*.py
