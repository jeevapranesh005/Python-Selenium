@echo off
REM Run the exception handling scripts under PythonHandsOn-1\ExceptionHandling with example stdin
REM Usage: double-click or call from Jenkins workspace root

cd /d "%~dp0..\PythonHandsOn-1\ExceptionHandling"
echo Running Python exception handling programs...

echo Running DivByZero.py
python DivByZero.py

echo Running IndexOutOfBound.py
python IndexOutOfBound.py

echo Running Keynotfound.py
python Keynotfound.py

echo Running Calculator.py (example invalid multiplication)
(
  echo *
  echo 0
  echo 5
) | python Calculator.py

echo Running Password.py (example valid credentials)
(
  echo testuser
  echo Test1234!
) | python Password.py

echo All exception handling scripts finished.
