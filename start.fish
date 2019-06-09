#!/usr/bin/env fish
set -x FLASK_APP sharify.py
set -x FLASK_ENV development
flask run --host=0.0.0.0 --port=5001
