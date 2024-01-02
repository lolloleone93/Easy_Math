@echo off

title python2exe
echo Start Conversion...




for %%a in (*.py) DO (pyinstaller --onefile %%a)
move "dist\*" "%~dp0"

rd /s /q "dist"
rd /s /q "build"
rem RMDIR /Q/S .\python2exe_converted

echo End Conversion
echo pause

