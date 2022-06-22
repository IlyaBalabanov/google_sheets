import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("arctic-depth-353614-f94b688223db.json", scope)

client = gspread.authorize(creds)

sheet = client.open("api test").sheet1  # Open the spreadhseet

data = sheet.get_all_values()  # Get a list of all records

row = sheet.row_values(1)

pprint (row)

