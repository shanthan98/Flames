import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Connect to Google Sheets
def connect_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "flames-credentials.json", scope
    )
    
    client = gspread.authorize(creds)
    sheet = client.open("FLAMES Data").sheet1
    
    return sheet


def save_to_sheet(data):
    sheet = connect_sheet()
    
    sheet.append_row([
        data["name1"],
        data["name2"],
        data["length1"],
        data["length2"],
        data["result"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])