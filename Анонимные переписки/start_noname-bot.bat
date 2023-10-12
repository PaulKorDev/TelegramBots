@echo off

call %~dp0NoName\venv\Scripts\activate

cd %~dp0NoName

set TOKEN=6081848305:AAHMg_ZOe0jZCXZxYsiOCT3c4IOkfKkbll8

python noname-bot.py

pause