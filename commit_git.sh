#!/bin/bash

sudo apt update
sudo apt -y install tree
tree -a > estrutura_diretorio.txt

git add .
git commit -m "$1"
git push -u origin main