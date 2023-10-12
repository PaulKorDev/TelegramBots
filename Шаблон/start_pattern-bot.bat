@echo off

call %~dp0Pattern\venv\Scripts\activate

cd %~dp0Pattern

set TOKEN=

python pattern-bot.py

pause