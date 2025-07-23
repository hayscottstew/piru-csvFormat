#!/usr/bin/env python3
"""
Build script to create a standalone executable from the CSV Formatter GUI
"""
import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command with options
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Create a single executable file
        "--windowed",                   # Hide console window (GUI only)
        "--name=CSV_Formatter",         # Name of the executable
        "--icon=icon.ico",              # Icon file (optional, will skip if not found)
        "--add-data=requirements.txt;.", # Include requirements.txt in the bundle
        "csv_formatter_gui.py"          # Main Python file
    ]
    
    # Remove icon option if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd = [arg for arg in cmd if not arg.startswith("--icon")]
        print("Note: No icon.ico found, building without custom icon")
    
    try:
        subprocess.check_call(cmd)
        print("\n✅ Build successful!")
        print(f"Executable created in: {Path.cwd() / 'dist' / 'CSV_Formatter.exe'}")
        print("\nYou can now distribute the 'dist' folder to your employees.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def main():
    print("CSV Formatter - Executable Builder")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("csv_formatter_gui.py"):
        print("❌ Error: csv_formatter_gui.py not found in current directory")
        print("Please run this script from the same directory as csv_formatter_gui.py")
        sys.exit(1)
    
    try:
        # Step 1: Install requirements
        install_requirements()
        
        # Step 2: Build executable
        if build_executable():
            print("\n🎉 Success! Your CSV Formatter is ready for distribution.")
            print("\nNext steps:")
            print("1. Test the executable in the 'dist' folder")
            print("2. Copy the 'dist' folder to your employees' computers")
            print("3. They can run CSV_Formatter.exe directly (no Python needed)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 