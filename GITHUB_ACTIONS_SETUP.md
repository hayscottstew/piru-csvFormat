# 🚀 GitHub Actions Cross-Platform Build Setup

This guide will help you set up automatic building of your CSV Formatter for Windows, macOS, and Linux using GitHub Actions.

## 📋 Prerequisites

- A GitHub account
- Git installed on your computer
- Your CSV Formatter files

## 🛠️ Quick Setup

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Name it `csv-formatter` (or any name you prefer)
4. Make it **Public** (required for free GitHub Actions)
5. ✅ Check "Add a README file"
6. Click "Create repository"

### Step 2: Upload Your Files

**Option A: Using GitHub Web Interface**
1. In your new repository, click "uploading an existing file"
2. Drag and drop all these files:
   - `csv_formatter_gui.py`
   - `requirements.txt`
   - `build_executable.py`
   - `README_EXECUTABLE.md`
   - `.github/workflows/build-executables.yml`
   - `.gitignore`
3. Commit the files

**Option B: Using Git (Command Line)**
```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/csv-formatter.git
cd csv-formatter

# Copy your files here, then:
git add .
git commit -m "Add CSV Formatter application"
git push origin main
```

### Step 3: Trigger the Build

The GitHub Action will automatically run when you:
- Push code to the `main` branch
- Create a pull request
- Manually trigger it from the Actions tab

**To manually trigger:**
1. Go to your repository on GitHub
2. Click the "Actions" tab
3. Click "Build Cross-Platform Executables"
4. Click "Run workflow" → "Run workflow"

## 📦 Download Your Executables

### From Actions Tab (Always Available)
1. Go to "Actions" tab in your repository
2. Click on the latest successful workflow run
3. Scroll down to "Artifacts"
4. Download:
   - `CSV_Formatter-Windows.exe-package` (for Windows users)
   - `CSV_Formatter-macOS-package` (for Mac users)  
   - `CSV_Formatter-Linux-package` (for Linux users)

### From Releases (When Tagged)
1. Create a tag to trigger a release:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
2. Check the "Releases" section of your repository
3. Download the executables from the release

## 🔧 Workflow Features

The GitHub Actions workflow automatically:

### ✅ **Builds for Multiple Platforms**
- **Windows**: Creates `CSV_Formatter.exe`
- **macOS**: Creates `CSV_Formatter` (app bundle)
- **Linux**: Creates `CSV_Formatter` (binary)

### ✅ **Tests Each Build**
- Verifies executable was created
- Checks file permissions
- Reports build sizes

### ✅ **Creates Distribution Packages**
- Includes the executable
- Includes documentation
- Includes requirements.txt

### ✅ **Handles Dependencies**
- Installs Python 3.11
- Installs pandas and PyInstaller
- Installs system dependencies (Linux tkinter)

### ✅ **Creates Releases**
- Automatically creates GitHub releases for tagged versions
- Attaches all platform executables
- Generates release notes

## 🎯 Distribution Strategy

### For Your Employees:

1. **Windows Users:**
   - Download `CSV_Formatter-Windows.exe-package.zip`
   - Extract and run `CSV_Formatter.exe`

2. **Mac Users:**
   - Download `CSV_Formatter-macOS-package.zip`
   - Extract and run `CSV_Formatter`

3. **Linux Users:**
   - Download `CSV_Formatter-Linux-package.zip`
   - Extract, make executable: `chmod +x CSV_Formatter`
   - Run: `./CSV_Formatter`

## 🔄 Updating Your Application

To release a new version:

1. **Update your code** (modify `csv_formatter_gui.py`)
2. **Commit and push** changes
3. **Create a new tag** for releases:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```
4. **GitHub Actions automatically builds** new executables
5. **Download from Releases** or Actions artifacts

## 🎨 Customization

### Modify the Build Process
Edit `.github/workflows/build-executables.yml` to:
- Change Python version
- Add custom icons
- Modify PyInstaller options
- Add code signing (for production)

### Add More Platforms
The workflow can be extended to support:
- ARM64 builds
- Different Python versions
- Custom build matrices

## 🔐 Security & Permissions

### Repository Settings
- **Public repos**: Free GitHub Actions (2000 minutes/month)
- **Private repos**: Limited free minutes

### Permissions
- The workflow only needs default repository permissions
- No secrets required for basic building
- For code signing, add secrets in repository settings

## 🐛 Troubleshooting

### Build Fails
- Check the Actions tab for error logs
- Common issues:
  - Missing dependencies in `requirements.txt`
  - Platform-specific code issues
  - PyInstaller configuration problems

### Downloads Don't Work
- Ensure workflow completed successfully (green checkmark)
- Artifacts expire after 90 days
- Use releases for permanent downloads

### Large File Sizes
- Executables include Python + all dependencies
- Windows: ~30-50MB
- macOS/Linux: ~40-60MB
- This is normal for PyInstaller builds

## 📞 Support

If you encounter issues:
1. Check the [Actions logs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs)
2. Verify all files are committed correctly
3. Ensure your repository is public (for free Actions)
4. Check that `requirements.txt` includes all dependencies

---

**🎉 That's it! Your CSV Formatter will now build automatically for all platforms whenever you update your code.** 