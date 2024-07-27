

# python -m venv venv
# .\venv\Scripts\activate or source venv/bin/activate
# pip install -r requirements.txt


import os
import random
from datetime import date, datetime

import gspread
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT_FILE = 'creds.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)


spreadsheet_id = '1cWzW_6HwnuLx8XKtR4R21dc7fYG3If-v96lte_VTlJU'
spreadsheet = client.open_by_key(spreadsheet_id)


sheet_readonly = spreadsheet.worksheet('Gifts')


records = sheet_readonly.get_all_records()

for i in records:
    print(i)
