@echo off
setlocal

:: ==== CONFIGURATION ====
set INPUT=canvas_output.ps
set OUTPUT=output.pdf

:: Try to locate Ghostscript
set "GSPATH="
for %%G in (gswin64c.exe gswin32c.exe) do (
    where %%G >nul 2>&1
    if not errorlevel 1 (
        set "GSPATH=%%G"
        goto :found
    )
)

:manual
echo Ghostscript was NOT found on this system.
echo --------------------------------------------
echo Please open "%INPUT%" manually.
echo Then choose "Microsoft Print to PDF" in the Print dialog.
echo This is available by default on most Windows 10/11 systems.
echo.
pause
goto :eof

:found
echo Ghostscript found: %GSPATH%
echo Converting "%INPUT%" to "%OUTPUT%"...
%GSPATH% -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=%OUTPUT% %INPUT%
if %errorlevel% neq 0 (
    echo ❌ Conversion failed.
) else (
    echo ✅ Successfully created "%OUTPUT%"
)
pause