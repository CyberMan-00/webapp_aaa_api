import logging
import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.google_api import GoogleAPI
from logger import config_logging

config_logging(process_name="deal-reviews.com")

# FastAPI app
app = FastAPI()
# Add CORS middleware
origins = [
    "http://localhost:3000",  # Allow localhost
    "https://deal-reviews.com",  # Add your frontend domain if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
try:
    GoogleSheetsService = GoogleAPI.initialize_service()
except Exception as e:
    logging.error(f'GoogleSheetsService initialization failed: {e}')

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

