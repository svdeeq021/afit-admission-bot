@echo off
echo ========================================
echo University Admission Bot - Setup
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit
)
echo ✓ Python found!
echo.

echo [2/3] Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install packages
    echo Try running: pip install streamlit groq python-dotenv
    pause
    exit
)
echo ✓ Packages installed!
echo.

echo [3/3] Setup complete!
echo.
echo ========================================
echo Next Steps:
echo 1. Get your free Groq API key from: https://console.groq.com
echo 2. Run the app with: streamlit run app.py
echo ========================================
echo.
pause