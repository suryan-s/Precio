@echo off

REM 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    REM Python is not installed, so install Python 3.9.13
    echo Installing Python 3.9.13...
    curl -o python-3.9.13.exe "https://www.python.org/ftp/python/3.9.13/python-3.9.13.exe"
    python-3.9.13.exe /quiet PrependPath=1
    del python-3.9.13.exe
    echo Python 3.9.13 installed.
) else (
    echo Python is already installed.
)

REM 2. Install virtualenv
echo Installing virtualenv...
python -m pip install virtualenv
echo virtualenv installed.

REM 3. Create a new environment
echo Creating a new virtual environment...
python -m virtualenv .env
echo Virtual environment created.

REM 4. Activate the environment
echo Activating the virtual environment...
call .env\Scripts\activate.bat
echo Virtual environment activated.

REM 5. Run setup.py
echo Running setup.py...
python setup.py install
echo setup.py completed.

REM 6. Deactivate the environment
echo Deactivating the virtual environment...
deactivate
echo Virtual environment deactivated.

REM 7. Check if Node.js is installed
echo Checking if Node.js is installed...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    REM Node.js is not installed, so install it
    echo Installing Node.js...
    curl -o node-setup.msi "https://nodejs.org/dist/v16.14.0/node-v16.14.0-x64.msi"
    start /wait node-setup.msi
    del node-setup.msi
    echo Node.js installed.
) else (
    echo Node.js is already installed.
)

REM 8. Check if npm is installed
echo Checking if npm is installed
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    REM npm is not installed, so install it
    echo Installing npm...
    npm install npm@latest -g
    echo npm installed.
) else (
    echo npm is already installed.
)

REM 9. Verify installations
echo Verifying installations...
node --version
npm --version

REM 10. NPM setup
echo NPM setup...
cd frontend
npm install
echo NPM setup completed.
npm run build
echo NPM build completed.

echo Setup completed.
