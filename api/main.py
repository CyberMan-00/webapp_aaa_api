import random

from fastapi import FastAPI
from api.google_api import GoogleAPI

# FastAPI app
app = FastAPI()
# Access Google Sheets API service
GoogleSheetsService = GoogleAPI.initialize_service()

@app.get("/")
async def get_hello():
    return {'message': 'hello world!'}

@app.get("/random-{limit}")
async def get_hello(limit: int):
    return {'your_random_number': random.randint(0, limit)}

@app.get("/p-f-all")
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

