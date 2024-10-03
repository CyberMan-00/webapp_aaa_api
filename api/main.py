from fastapi import FastAPI
from api.google_api import GoogleAPI

# FastAPI app
app = FastAPI()
# Access Google Sheets API service
GoogleSheetsService = GoogleAPI.initialize_service()


@app.get("/")
async def get_product_feed():
    sheet = GoogleSheetsService.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=GoogleAPI.SPREADSHEET_ID, range=GoogleAPI.RANGE
    ).execute()

    values = result.get('values', [])

    if not values:
        return {"error": "No data found."}
    else:
        return values

