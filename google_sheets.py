import asyncio
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials_path = 'config_sheet.json'

credentials = sac.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(credentials)


def gsheet2df(spreadsheet_name, sheet_num):

    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_records(numericise_ignore=['all'])
    df = pd.DataFrame.from_dict(sheet)

    return sheet


def barcode():
    name = "products_export_1683261364555"
    data_sheets = gsheet2df(name, 0)
    new = {i["Название"].upper(): i["ШТРИХКОД"] for i in data_sheets}
    return new