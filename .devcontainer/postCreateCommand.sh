#!/bin/sh

set -e # Add pipe fail command to exit on error

printf "=====< \033[1;34m:: Setting Up Developer Tools ::\033[0m >=====\n"
echo ""
echo " :: Adding permissions for developer to access .cache :: "
sudo chown developer:developer ~/.cache
echo ""
pip install -r requirements.txt
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
printf "=====< \033[1;34m:: Exiting ::\033[0m >=====\n"