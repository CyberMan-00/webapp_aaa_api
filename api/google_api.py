import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials


class GoogleAPI:
    load_dotenv("creds/.env")
    SPREADSHEET_ID: str = os.getenv("SPREADSHEET_ID")
    RANGE: str = os.getenv("RANGE")
    SERVICE_ACCOUNT_FILE: str = os.getenv("SERVICE_ACCOUNT_FILE")

    if not SPREADSHEET_ID:
        raise ValueError("SPREADSHEET_ID is not set in the environment variables.")

    if not RANGE:
        raise ValueError("RANGE is not set in the environment variables.")

    if not SERVICE_ACCOUNT_FILE:
        raise ValueError("SERVICE_ACCOUNT_FILE is not set in the environment variables.")

    # Set up credentials and Google Sheets API service
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    @classmethod
    def initialize_service(cls):
        try:
            creds = Credentials.from_service_account_file(cls.SERVICE_ACCOUNT_FILE, scopes=cls.SCOPES)
            service = build("sheets", "v4", credentials=creds)
            return service
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Google Sheets API service: {e}")


# Fetch the Google Sheets API service
GoogleSheetsService = GoogleAPI.initialize_service()
