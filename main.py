import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['URL for google sheets feed']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

docid = "ID for Document"

client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(docid)
for i, worksheet in enumerate(spreadsheet.worksheets()):
    filename = docid + '-worksheet' + str(i) + '.csv'
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(worksheet.get_all_values())