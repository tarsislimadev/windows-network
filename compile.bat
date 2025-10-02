@echo off
echo Windows Network Management Application - Compilation Script
echo ============================================================

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo Error: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

REM Create dist directory if it doesn't exist
if not exist "dist" mkdir dist

REM Clean previous builds
echo Cleaning previous builds...
if exist "build" rmdir /s /q build
if exist "dist\windows-network.exe" del "dist\windows-network.exe"
if exist "dist\windows-network" rmdir /s /q "dist\windows-network"

echo Compiling application...
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "windows-network" ^
    --add-data "src;src" ^
    --hidden-import "PyQt6.QtCore" ^
    --hidden-import "PyQt6.QtGui" ^
    --hidden-import "PyQt6.QtWidgets" ^
    --clean ^
    main.py

if %errorlevel% eq 0 (
    echo.
    echo ============================================================
    echo Compilation successful!
    echo Executable created at: dist\windows-network.exe
    echo ============================================================
    
    REM Optional: Open dist folder
    explorer dist
) else (
    echo.
    echo ============================================================
    echo Compilation failed! Check the output above for errors.
    echo ============================================================
)

pause