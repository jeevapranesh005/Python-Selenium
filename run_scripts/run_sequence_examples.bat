@echo off
REM Run the sequence scripts under PythonHandsOn-1\sequence with example stdin
REM Usage: double-click or call from Jenkins workspace root

cd /d "%~dp0..\PythonHandsOn-1\sequence"

echo Running Python Programs...

echo Running primeNumber.py
(
  echo 10
  echo 30
) | python primeNumber.py

echo Running Question1.py
python Question1.py

echo Running Question2.py
echo 5 | python Question2.py

echo Running Question3.py
(
  echo 4
  echo 6
) | python Question3.py

echo Running Question4.py
echo Jeeva | python Question4.py

echo Running Question5.py
echo 1995-08-15 | python Question5.py

echo Running Question6.py
(
  echo 70
  echo 1.75
) | python Question6.py

echo Running Question7.py
echo 85 | python Question7.py

echo Running Question8.py
echo 4.3 | python Question8.py

echo Running Question10.py
echo apple,banana,orange | python Question10.py

echo Running smartcliff.py
python smartcliff.py

echo Running while.py
(
  echo 3
  echo 5
  echo 7
  echo 9
) | python while.py

echo All sequence scripts finished.
