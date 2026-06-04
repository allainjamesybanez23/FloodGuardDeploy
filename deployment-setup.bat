@echo off
REM deployment-setup.bat
REM Prepare the app for deployment (Windows version)

echo === FloodGuard Deployment Setup ===

REM 1. Build Ionic app
echo Building Ionic app...
cd floodguard_ionic
call npm run build
cd ..

REM 2. Collect Django static files
echo Collecting Django static files...
cd floodguard_api
python manage.py collectstatic --noinput --clear
cd ..

REM 3. Create necessary folders
echo Creating necessary directories...
if not exist "floodguard_api\staticfiles" mkdir floodguard_api\staticfiles

echo === Setup Complete ===
echo Your app is ready to deploy!
echo.
echo Next steps:
echo 1. Deploy to Railway/Render with this folder
echo 2. Set environment variables (SECRET_KEY, DEBUG=False, etc.)
echo 3. Run migrations: python manage.py migrate
pause
