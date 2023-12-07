
import io
import pandas as pd
import xlsxwriter
import datetime

from google_sheets import barcode


def new_date():

    df = pd.read_excel("test.xlsx", header=None, skiprows=0)
    list_df = df.values.tolist()
    sheets_data = barcode()

    for i in list_df:
        i.append(sheets_data[str(i[1][:-10]).upper().replace("\xa0", " ")] if str(i[1][:-10]).upper().replace("\xa0", " ") in sheets_data else None)
        i[1] = str(i[1][:-10])

    return list_df


def write_to_file():
    data = new_date()

    now = datetime.datetime.now()
    date_time = now.strftime("%d.%m.%Y %H:%M")

    filename = f"Поступление.xlsx"
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    head_style = workbook.add_format(
        {
            'bold': True, 'border': 1, 'align': 'center',
        }
    )

    content_style = workbook.add_format(
        {
            'bold': False, 'border': 1, 'align': 'center',
        }
    )

    content_title = workbook.add_format(
        {
            'bold': True, 'align': 'center', 'font_size': 16,
        }
    )

    columns = [
        '№ строки',
        'Штрихкод',
        'Артикул',
        'Название',
        'Характеристика',
        'Серия',
        'Описание',
        'Заявлено',
        'Принято',
        'Цена приемки',
        'Название алко',
        'Объём',
        'Крепость',
        'Производитель',
        'ИНН',
        'КПП',
        'Алко код',
        'PDF417',
        'Серийный номер',
        'Дата розлива',
        'Наличие в формах А',
        'Код формы А',
    ]

    worksheet.set_column('C:C', 10)
    worksheet.set_column('D:E', 15)
    worksheet.set_column('F:F', 25)
    worksheet.set_column('G:G', 20)
    worksheet.set_column('I:I', 15)
    worksheet.set_column('J:K', 10)
    worksheet.set_column('L:L', 15)
    worksheet.set_column('M:O', 15)
    worksheet.set_column('Q:R', 10)
    worksheet.set_column('S:S', 15)
    worksheet.set_column('T:W', 10)
    worksheet.set_column('X:X', 15)

    worksheet.merge_range('C2:H2', f"Поступление {date_time}", content_title)
    worksheet.write('C5:C5', f"Выполнил: оператор")
    worksheet.write('C6:C6', f"Код ТСД: DatalogicMemorX3-P17B03027")
    worksheet.write('C7:C7', f"IP ТСД: ")

    for index, value in enumerate(columns):
        worksheet.write(9, index+2, value, head_style)

    for i, value in enumerate(data, start=10):
        worksheet.write(i, 2, None, content_style)
        worksheet.write(i, 3, value[-1], content_style)
        worksheet.write(i, 4, None, content_style)
        worksheet.write(i, 5, value[1], content_style)
        worksheet.write(i, 6, None, content_style)
        worksheet.write(i, 7, None, content_style)
        worksheet.write(i, 8, None, content_style)
        worksheet.write(i, 9, None, content_style)
        worksheet.write(i, 10, value[2], content_style)
        worksheet.write(i, 11, value[-3], content_style)
        worksheet.write(i, 12, None, content_style)
        worksheet.write(i, 13, None, content_style)
        worksheet.write(i, 14, None, content_style)
        worksheet.write(i, 15, None, content_style)
        worksheet.write(i, 16, None, content_style)
        worksheet.write(i, 17, None, content_style)
        worksheet.write(i, 18, None, content_style)
        worksheet.write(i, 19, None, content_style)
        worksheet.write(i, 20, None, content_style)
        worksheet.write(i, 21, None, content_style)
        worksheet.write(i, 22, None, content_style)
        worksheet.write(i, 23, None, content_style)

    for index, value in enumerate(columns):
        worksheet.write(10+len(data), index+2, None, content_style)

    workbook.close()