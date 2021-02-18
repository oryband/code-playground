#!/usr/bin/env bash
# start cache and main server app,
# wait for any key press, then graefully shutdown both (by priority)
set -e
set -x

# set up python environment
pipenv sync

echo 'Starting storage service...'
cd cache && pipenv run gunicorn app:app &

echo 'Starting main app server...'
cd app && pipenv run gunicorn app:app &

# catch any key press, then gracefully shutdown both services
read 
trap 'Shutting down...' INT

kill -s TERM $(ps -fade | grep gunicorn | grep cache | awk '{print $2}' | head -n 1)
kill -s TERM $(ps -fade | ag gunicorn | grep server | awk '{print $2}' | head -n 1)
