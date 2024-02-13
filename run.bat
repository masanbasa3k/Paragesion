@echo off

REM Install dependencies
pip install -r requirements.txt

REM Set Flask app
set FLASK_APP=app.py

REM Run Flask app
flask run

pause