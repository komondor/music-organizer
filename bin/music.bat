@echo OFF

:: %~dp0 return command bin path

SET CurrDir= %CD%
CD %~dp0
CD ..
python "%CD%/main.py" %* 

