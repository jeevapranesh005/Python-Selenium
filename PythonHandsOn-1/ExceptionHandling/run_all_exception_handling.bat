@echo off
REM Run all exception handling examples from this folder.
cd /d "%~dp0"
echo Running DivByZero.py
python DivByZero.py
echo.
echo Running IndexOutOfBound.py
python IndexOutOfBound.py
echo.
echo Running Keynotfound.py
python Keynotfound.py
echo.
echo Running Bank.py
(
  echo 35000
) | python Bank.py
echo.
echo Running CitizenInput.py
(
  echo 123456789012
  echo John Doe
  echo Mumbai
  echo Maharashtra
  echo India
) | python CitizenInput.py
echo.
echo Running Calculator.py
(
  echo *
  echo 0
  echo 5
) | python Calculator.py
echo.
echo Running IntToSquare.py
(
  echo 7
) | python IntToSquare.py
echo.
echo Running MarksEligible.py
(
  echo 65
  echo 55
  echo 50
) | python MarksEligible.py
echo.
echo Running Palindrome.py
(
  echo 121
) | python Palindrome.py
echo.
echo Running Password.py
(
  echo testuser
  echo Test1234!
) | python Password.py
echo.
echo Running Runningsum.py
(
  echo 5
) | python Runningsum.py
echo.
echo Running Sumofseries.py
(
  echo 3
) | python Sumofseries.py
echo.
echo All exception handling scripts finished.
