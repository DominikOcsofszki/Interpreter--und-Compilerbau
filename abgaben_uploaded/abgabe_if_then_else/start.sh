#!bin/sh
#
.venv/bin/pip install -r requirements.txt
cd src 
.venv/bin/pip install -e .
cd ..
python3 RUN.py

