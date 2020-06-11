ECHO OFF
CLS

echo  ____                       __
echo /\  __`\          __        /\ \__
echo \ \ \/\ \  __  __/\_\     __\ \ ,_\
echo  \ \ \ \ \/\ \/\ \/\ \  /'__`\ \ \/
echo   \ \ \\'\\ \ \_\ \ \ \/\  __/\ \ \_
echo    \ \___\_\ \____/\ \_\ \____\\ \__\
echo     \/__//_/\/___/  \/_/\/____/ \/__/
echo.
echo.
echo  __                                   __
echo /\ \                      __         /\ \__  __
echo \ \ \        ___      __ /\_\    ____\ \ ,_\/\_\    ___    ____
echo  \ \ \  __  / __`\  /'_ `\/\ \  /',__\\ \ \/\/\ \  /'___\ /',__\
echo   \ \ \L\ \/\ \L\ \/\ \L\ \ \ \/\__, `\\ \ \_\ \ \/\ \__//\__, `\
echo    \ \____/\ \____/\ \____ \ \_\/\____/ \ \__\\ \_\ \____\/\____/
echo     \/___/  \/___/  \/___L\ \/_/\/___/   \/__/ \/_/\/____/\/___/
echo                       /\____/
echo                       \_/__/
echo.
echo.
echo.
echo Please wait for update, thank you.

set path=%cd%
C:\Windows\py.exe -m pip install -U pip
C:\Windows\py.exe -m pip install pyinquirer paramiko
cls
C:\Windows\py.exe %path%\py\main.py

pause
