# Google Drive Automation with Python

This repository contains a Jupyter Notebook that automates Google Drive tasks such as file uploads and listing folder contents. The notebook uses the `PyDrive` library to interact with the Google Drive API.

## Features

1. **Google Drive Authentication**: 
   - Authenticate securely using OAuth2.
   - Store credentials locally for reuse.
2. **File Upload**: 
   - Upload files to a specific folder in Google Drive or the root directory.
3. **List Folder Contents**: 
   - Retrieve and display metadata of files stored in a folder or the root directory.

## Requirements

- Python 3.6 or higher.
- Jupyter Notebook or JupyterLab.
- The following Python libraries:
  - `PyDrive`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chemekeki/Google-Drive.git
   cd google-drive-automation
   ```

2. Install required dependencies:
   ```bash
   pip install pydrive
   ```

3. Set up Google Drive API credentials:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the **Google Drive API** for your project.
   - Create OAuth 2.0 credentials and download the `client_secrets.json` file.
   - Place the `client_secrets.json` file in the project directory.

## Usage

### 1. Authenticate with Google Drive
Run the notebook to authenticate with Google Drive. On the first run, you'll be prompted to log in and authorize access. The credentials will be saved locally (`mycreds.txt`) for subsequent use.

### 2. Upload a File
To upload a file, specify the local file path and optional Google Drive folder ID in the upload function:
```python
upload_file(drive, "path_to_file", folder_id="optional_folder_id")
```

### 3. List Folder Contents
To list the contents of a folder or the root directory, use:
```python
list_files(drive, folder_id="optional_folder_id")
```

### 4. Example Workflow
- Authenticate with Google Drive.
- Upload a file to a specific folder.
- List files in the folder.

All these steps are demonstrated in the notebook.

## File Overview

### `Code to automate google drive.ipynb`
A Jupyter Notebook containing:
- Code to authenticate with Google Drive.
- Functions for uploading and listing files.
- Example workflows to guide users.

### `Google_drive_automation_code.py`
A standalone Python script with similar functionality for users who prefer to run the automation outside a notebook.

## Notes

- Ensure the `client_secrets.json` file is correctly set up for API access.
- The notebook demonstrates reusable functions for common Google Drive tasks.
- Modify paths and folder IDs in the notebook cells as needed.

