Run scripts with redirected input (Windows, Jenkins)

How to run locally from this folder:

 - Run a single script with an input file:

```
run_with_input.bat "..\PythonHandsOn-1\controlflow\MQuestion.py" "inputs\MQuestion_input.txt"
```

 - Or run provided examples:

```
run_controlflow_examples.bat
run_iteration_examples.bat
```

Jenkins (Windows agent) tips:

 - Use a Windows build step (Execute Windows batch command). From the Jenkins workspace root, run:

```
%WORKSPACE%\run_scripts\run_controlflow_examples.bat
```

 - Non-interactive: these scripts use stdin redirection (`<` or piping via `type`) so they work in Jenkins without a console.
