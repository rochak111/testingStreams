#!/usr/bin/bash


pip install -r requirements.txt

chmod +x migrate.sh
./migrate.sh

rm Dockerfile
rm .dockerignore
rm README.md
rm .gitignore