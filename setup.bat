@echo off
echo ===========================================
echo       Setup for Osinys
echo ===========================================

echo.
echo Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

echo Python is installed. Proceeding with the setup...
echo.

echo Checking for pip...
pip --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
    if %ERRORLEVEL% neq 0 (
        echo Failed to install pip. Please install pip manually.
        pause
        exit /b
    )
)

echo pip is installed. Proceeding with dependency installation...
echo.

echo Installing required dependencies...
pip install customtkinter pillow requests colorama pystyle discord
pip3 install customtkinter pillow requests colorama pystyle discord

if %ERRORLEVEL% neq 0 (
    echo There was an error during the installation. Please check the error message above and try again.
    pause
    exit /b
)

echo.
echo Dependencies installed successfully.
echo.
echo To run your project, navigate to the project directory and run your Python script:
echo     python your_script_name.py
echo.
echo Thank you for using this setup script!



python Osinys.py


pause>nul
