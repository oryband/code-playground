#!/usr/bin/env bash
# run client dos application
set -e
set -x

# set up python environment
pipenv sync

echo 'Starting client...'
pipenv run python app.py
