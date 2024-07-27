

# python -m venv venv
# .\venv\Scripts\activate or source venv/bin/activate
# pip install -r requirements.txt


import os # lib work system
import random # lib random 
from datetime import date, datetime # lib with date, datetime

import gspread # lib work with google sheet 
from google.oauth2 import service_account # lib oauth(creds)
# from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials # lib creds 

SERVICE_ACCOUNT_FILE = 'creds.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)


spreadsheet_id = '1cWzW_6HwnuLx8XKtR4R21dc7fYG3If-v96lte_VTlJU'
spreadsheet = client.open_by_key(spreadsheet_id)

sheet_readonly = spreadsheet.worksheet('Gifts')
sheet_users = spreadsheet.worksheet('Scores')
sheet_score = spreadsheet.worksheet('Send_score')

# task 1: all gifts name 
records = sheet_readonly.get_all_records()

# create function with doc-s
# for record in records: 
#     if record['is_active'] == 'TRUE' and record['Amount'] >= 1:
#         print(record['Gift_name'], record['Value'], record['Describe'])

# task 2: check score by user 

def get_now() -> str:
    return datetime.now().strftime('%Y-%m-%d')


def is_valid_user(user_id: str, sheet_name: str = sheet_users) -> bool:
    """_summary_

    Args:
        user_id (str): _description_

    Returns:
        bool: _description_
    """
    records = sheet_name.get_all_records()
    
    for record in records:
        if record['user_id'] == user_id:
            return True 
    return False


def get_score(user_id: str, sheet_name: str = sheet_users) -> int | None:
    
    records = sheet_name.get_all_records()
    for record in records: 
        if user_id == record['user_id']:
            return record['score'] # if more than one score, need sum 
        
    return None    


user_id = 10001
user_id_second = 10002 

if is_valid_user(user_id) and is_valid_user(user_id_second):
    
    score_user_id = (user_id, get_score(user_id))
    score_user_id2 = (user_id_second, get_score(user_id_second))
    
    score = 500
    
    if score_user_id[1] >= score:
        sheet_score.append_row([score_user_id[0], score_user_id2[0], score, get_now(), 'for gifts'])
        
        # MARK: /// Update Scores sheet
             
    else:
        print(f'No score {score_user_id[0]}')
        
# re-write to function 
# if is_valid_user(user_id):
#     tmp = 0
#     for record in sheet_users.get_all_records():
#         if record['date'] == get_now():
#             tmp += record['score']
            
#     print(f'User_id: {user_id}\n. Score: {tmp}.\n Date: {get_now()}')
        