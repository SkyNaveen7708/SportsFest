import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Google API scope
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate
creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Open Google Sheet
spreadsheet = client.open("CIEC QA Sports Fest")


def read_sheet(sheet_name):
    worksheet = spreadsheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)