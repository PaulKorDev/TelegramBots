@echo off

call %~dp0TraningOwnGrow\venv\Scripts\activate

cd %~dp0TraningOwnGrow


python traning-bot.py

pause