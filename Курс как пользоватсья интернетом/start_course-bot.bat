@echo off

call %~dp0CourseInternerBot\venv\Scripts\activate

cd %~dp0CourseInternerBot


python course-bot.py

pause