@echo off
echo 🌦️ NextGenMinds Weather Probability Portal - Frontend
echo ==================================================

cd frontend

echo 📦 Installing Node.js dependencies...
call npm install

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

echo 🚀 Starting React development server...
echo 📍 Frontend will be available at: http://localhost:3000
echo 🔑 Demo Login - Username: NextGenMinds, Password: Pass@123
echo.
echo ============================================================

call npm start

pause
