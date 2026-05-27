@echo off
REM Example: run a few controlflow scripts using sample inputs in this folder
set BASEDIR=%~dp0
echo Running controlflow examples...

echo MQuestion (age -> sample 15)
python "%BASEDIR%..\PythonHandsOn-1\controlflow\MQuestion.py" < "%BASEDIR%inputs\MQuestion_input.txt"

echo EQuestion4 (age example)
python "%BASEDIR%..\PythonHandsOn-1\controlflow\EQuestion4.py" < "%BASEDIR%inputs\EQuestion4_input.txt"

echo Done.
