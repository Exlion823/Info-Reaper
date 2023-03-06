echo off
python -m venv .venv
python -m pip install -r requirements.txt

pip install -e . --no-deps
python setup.py develop