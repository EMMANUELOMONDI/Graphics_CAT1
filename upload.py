from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import json
from zenlog import log
import requests
import datetime


def upload_to_drive(filename: str, SCOPES=None):
    """
    Uploads a file to google drive and returns the file id
    """
    log.info(f"Uploading the file: {filename}")
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("drive", "v3", credentials=creds)
        access_token = creds.token
        filesize = os.path.getsize(filename)

        stamped_name= filename.replace(".zip", str(datetime.datetime.now())+".zip").replace(" ","_")

        headers = {"Authorization": "Bearer " + access_token, "Content-Type": "application/json"}
        params = {
            "name": stamped_name,
            "mimeType": "application/zip"
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable",
            headers=headers,
            data=json.dumps(params)
        )
        location = r.headers['Location']

        headers = {"Content-Range": "bytes 0-" + str(filesize - 1) + "/" + str(filesize)}
        r = requests.put(
            location,
            headers=headers,
            data=open(filename, 'rb')
        )
        log.info(f"Uploaded backup file: {stamped_name}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None
    except Exception as error:
        log.error(str(error))