@echo off
REM Example: run a few iteration scripts using sample inputs in this folder
set BASEDIR=%~dp0
echo Running iteration examples...

echo EQuestion4 (n -> sample 5)
python "%BASEDIR%..\PythonHandsOn-1\Iteration\EQuestion4.py" < "%BASEDIR%inputs\EQuestion4_input.txt"

echo MQuestion1 (n -> sample 4)
python "%BASEDIR%..\PythonHandsOn-1\Iteration\MQuestion1.py" < "%BASEDIR%inputs\MQuestion1_input.txt"

echo Done.
