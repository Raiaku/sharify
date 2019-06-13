#!/usr/bin/env fish
pyenv local sharify project
set -x FLASK_APP sharify.py
set -x FLASK_ENV development
flask run --host=0.0.0.0 --port=5001
