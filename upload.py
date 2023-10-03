from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive
import os

def upload_file(file):
        
    gauth = GoogleAuth() 
    drive = GoogleDrive(gauth)

    # Create GoogleDriveFile instance
    file1 = drive.CreateFile() 

    # Set content of the file from given file and then upload
    file1.SetContentFile(file) 
    file1.Upload()

    print("The file has been uploaded to Google Drive")
