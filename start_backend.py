#!/usr/bin/env python3
"""
Startup script for NextGenMinds Weather Probability Portal Backend
This script handles dependency installation and starts the FastAPI server
"""

import sys
import subprocess
import os
from pathlib import Path

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_dependencies():
    """Check and install required dependencies"""
    required_packages = [
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "pydantic==2.5.0",
        "python-jose[cryptography]==3.3.0",
        "passlib[bcrypt]==1.7.4",
        "python-multipart==0.0.6",
        "sqlalchemy==2.0.23",
        "python-dotenv==1.0.0",
        "geopy==2.4.1",
        "requests==2.31.0"
    ]
    
    print("🔧 Checking and installing dependencies...")
    
    for package in required_packages:
        package_name = package.split("==")[0]
        try:
            __import__(package_name.replace("-", "_"))
            print(f"✅ {package_name} is already installed")
        except ImportError:
            print(f"📦 Installing {package_name}...")
            if install_package(package):
                print(f"✅ {package_name} installed successfully")
            else:
                print(f"❌ Failed to install {package_name}")
                return False
    
    return True

def start_server():
    """Start the FastAPI server"""
    # Change to backend directory
    backend_dir = Path(__file__).parent / "backend"
    os.chdir(backend_dir)
    
    print("\n🚀 Starting NextGenMinds Weather Probability Portal Backend...")
    print("📍 Server will be available at: http://127.0.0.1:8000")
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("🔑 Demo Login - Username: NextGenMinds, Password: Pass@123")
    print("\n" + "="*60)
    
    try:
        # Start uvicorn server
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app:app", 
            "--host", "127.0.0.1", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    print("🌦️ NextGenMinds Weather Probability Portal")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    if not check_and_install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Start server
    start_server()
