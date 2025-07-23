# CSV Formatter - Executable Distribution Guide

This guide will help you create a standalone executable of your CSV formatter that your employees can use without installing Python.

## 📁 Files Overview

- `csv_formatter_gui.py` - Main GUI application
- `build_executable.py` - Automated build script
- `requirements.txt` - Python dependencies
- `csvFormatter.py` - Original command-line script (for reference)

## 🚀 Quick Start (Automated Build)

1. **Run the automated build script:**
   ```bash
   python build_executable.py
   ```

2. **That's it!** The script will:
   - Install required dependencies
   - Create the executable using PyInstaller
   - Generate a `dist` folder with your executable

## 📋 Manual Build Instructions

If you prefer to build manually or the automated script doesn't work:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create Executable
```bash
pyinstaller --onefile --windowed --name=CSV_Formatter csv_formatter_gui.py
```

### Optional: Add Custom Icon
If you have an icon file (icon.ico), add:
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name=CSV_Formatter csv_formatter_gui.py
```

## 📦 Distribution

After building, you'll find:
- `dist/CSV_Formatter.exe` - The standalone executable
- `dist/` folder - Contains everything needed to run

### For Your Employees:
1. Copy the entire `dist` folder to their computers
2. They can run `CSV_Formatter.exe` directly
3. No Python installation required!

## 🖥️ GUI Features

The executable provides a user-friendly interface with:

- **File Upload**: Browse and select CSV files to format
- **Auto-suggestions**: Automatically suggests output filenames
- **Progress Tracking**: Shows real-time processing status
- **Error Handling**: Clear error messages and warnings
- **Status Log**: Detailed processing information

## 📊 What the Tool Does

1. **Loads CSV files** with property and contact data
2. **Keeps specific columns** (property info, emails, names, addresses, equity data)
3. **Unpivots phone numbers** from Phone1_Number through Phone10_Number columns
4. **Removes empty phone numbers** 
5. **Converts phone numbers to integers** (removes decimal points)
6. **Saves formatted data** to a new CSV file

## 🔧 Troubleshooting

### Build Issues

**Problem**: `ModuleNotFoundError: No module named 'tkinter'`
- **Solution**: On Linux, install: `sudo apt-get install python3-tk`

**Problem**: PyInstaller not found
- **Solution**: Install with: `pip install pyinstaller`

**Problem**: Large executable size
- **Solution**: This is normal. The executable includes Python and all dependencies.

### Runtime Issues

**Problem**: Executable won't start
- **Solution**: 
  - Check antivirus software (may block unsigned executables)
  - Try running from command line to see error messages
  - Ensure all files in `dist` folder are present

**Problem**: "Permission denied" error
- **Solution**: 
  - Run as administrator (Windows)
  - Check file permissions
  - Ensure output directory is writable

## 📝 Customization

To modify the tool for different CSV formats:

1. Edit `csv_formatter_gui.py`
2. Modify the `keep_cols` and `phone_cols` lists in the `CSVFormatterGUI.__init__()` method
3. Rebuild the executable

Example:
```python
# In csv_formatter_gui.py, line ~15-25
self.keep_cols = [
    "Your_Column_1", "Your_Column_2", 
    # Add your required columns here
]

self.phone_cols = [f"Phone{i}" for i in range(1, 6)]  # Adjust range as needed
```

## 🔐 Security Considerations

- The executable is unsigned, so Windows may show security warnings
- Consider code signing for production distribution
- Test thoroughly before distributing to employees
- Keep the source code for future modifications

## 💡 Advanced Options

### Creating a Windows Installer
```bash
# Install NSIS (Windows)
# Then use:
pyinstaller --onefile --windowed --name=CSV_Formatter csv_formatter_gui.py
# Use NSIS to create installer from dist folder
```

### Creating for Mac/Linux
The same process works on Mac and Linux:
```bash
# On Mac - creates .app bundle
pyinstaller --onefile --windowed --name=CSV_Formatter csv_formatter_gui.py

# On Linux - creates executable
pyinstaller --onefile --name=CSV_Formatter csv_formatter_gui.py
```

## 📞 Support

If your employees encounter issues:
1. Check that input CSV has the expected column names
2. Ensure they have write permissions to the output location  
3. Verify the CSV file isn't corrupted or locked by another program
4. Check the status log in the application for detailed error information

---

**Built with Python, tkinter, and PyInstaller** 🐍 