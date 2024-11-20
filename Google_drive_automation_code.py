
# Google Drive Automation Script

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_drive():
    """Authenticate and return a Google Drive instance."""
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if credentials are not available
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh the credentials if expired
        gauth.Refresh()
    else:
        # Initialize the saved credentials
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
    return GoogleDrive(gauth)

def upload_file(drive, local_file_path, remote_folder_id=None):
    """Upload a file to Google Drive.
    
    Args:
        drive: Authenticated GoogleDrive instance.
        local_file_path: Path to the local file to be uploaded.
        remote_folder_id: Google Drive folder ID (optional).
    """
    file_name = os.path.basename(local_file_path)
    file_drive = drive.CreateFile({'title': file_name, 'parents': [{'id': remote_folder_id}] if remote_folder_id else []})
    file_drive.SetContentFile(local_file_path)
    file_drive.Upload()
    print(f"Uploaded file '{file_name}' to Google Drive.")

def list_files(drive, folder_id=None):
    """List files in a specified Google Drive folder or root.
    
    Args:
        drive: Authenticated GoogleDrive instance.
        folder_id: Google Drive folder ID (optional).
        
    Returns:
        List of file metadata.
    """
    query = f"'{folder_id}' in parents and trashed=false" if folder_id else "trashed=false"
    file_list = drive.ListFile({'q': query}).GetList()
    for file in file_list:
        print(f"Title: {file['title']}, ID: {file['id']}")
    return file_list

if __name__ == "__main__":
    # Authenticate with Google Drive
    drive = authenticate_drive()

    # Example usage: Upload a file
    local_path = "example.txt"  # Replace with your file path
    upload_file(drive, local_path)

    # Example usage: List files in root directory
    list_files(drive)
