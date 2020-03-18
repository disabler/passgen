@echo off

rem *** Clean dist folder
rmdir dist /S /Q

rem *** Generate new icon file
cd icons
del PassGen.ico
..\png2ico.exe PassGen.ico PassGen128.png PassGen64.png PassGen48.png PassGen32.png PassGen16.png
cd ..

rem *** Build executable file
python build.py py2exe

rem *** Remove unused files
del dist\w9xpopen.exe

rem *** Wait and remove temporary folders
ping -n 3 127.0.0.1 > nul
rmdir build /S /Q
ping -n 3 127.0.0.1 > nul
rmdir build /S /Q

rem *** Sleep before ends
rem echo Finished!
rem pause

rem *** The end is near!
