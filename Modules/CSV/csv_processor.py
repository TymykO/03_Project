import csv
import os
from openpyxl import load_workbook
from Modules.Transform import data_transformer
from Modules.Utils.file_manager import get_csv_files

#Збереження списку у csv
def save_list_csv(data: list, path: str):
    try:
        with open(path, mode="w", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
    except FileNotFoundError as e:
        print(f'Error: Unable to find file path — {e}')

#Закачування даних с csv до списку
def open_csv_list(path: str):
    try:
        with open(path, mode="r", encoding='utf-8') as csv_file:
            data_csv = list(csv.reader(csv_file))
            # print(data_csv)
    except FileNotFoundError as e:
        print(f'Error: Unable to find file path — {e}')
        data_csv = []
    return data_csv
####################
#Збирає CSV-файли з папки CSV_creation і повертає їх шляхи.
def list_csv_in_creation():
    # Отримуємо абсолютний шлях до папки Data_BV/CSV_creation
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Шлях до кореня проєкту
    directory = os.path.abspath(os.path.join(base_dir, "Data_BV", "CSV_creation"))
    return get_csv_files(directory)
#####################
#---------------------------------------#
#-----------------To Do-----------------#
# Одна функція для витягування даних з csv у потрібній формі
def from_csv_data_sort(path: str):
    data = open_csv_list(path)
    top = data[0]
    data = data[1:]

    sorted_data = sorted(data, key=lambda item: float(item[0].replace(",", ".")))

    x = []
    y = []

    for row in sorted_data:
        for i, value in enumerate(row):
            value = value.replace(",", ".")
            try:
                number = float(value)
                if i == 0:
                    x.append(number)
                elif i == 1:
                    y.append(number)
                else:
                    print(f"Error: [{i}] '{value}' is incorrect data.")
            except ValueError:
                print(f"Error: [{i}] '{value}' is not a valid number.")
    return sorted_data, top, x, y

#-----------------To Do-----------------#
#---------------------------------------#


#Збереження даних з xlsx по дві колонки у csv
def convert_xlsx_to_csv(xlsx_path: str, output_dir: str):
    workbook = load_workbook(xlsx_path)
    sheet = workbook["Sheet1"]

    data_all_rows = []

    for row in sheet.iter_rows(min_row=1, values_only=True):
        if len(row)%2 == 0:
            data_all_rows.append(row)
        else:
            print('Odd number of columns, program stopped.')
            break

    column_index = 1
    csv_files = []

    for x in data_all_rows[0][::2]: #Ітерація по першому рядку з кроком 2
        data_to_csv = []

        heading = [x,data_all_rows[0][column_index]]
        data_to_csv.append(heading)
        csv_file_name = f'{x.replace(' ', '_')}.csv'

        for y in data_all_rows[1:]:
            setting = y[column_index - 1]
            kv = y[column_index]
            if setting is not None and kv is not None:
                data_to_csv.append([setting, kv])
            else:
                pass
        column_index += 2
        output_path = os.path.join(output_dir, csv_file_name)
        save_list_csv(data_to_csv, output_path)

        csv_files.append(csv_file_name)

    return csv_files


#Збирання даних про клапан у словник
def valve_data_processed(path_csv: str, deg: int):
    data = from_csv_data_sort(path_csv)
    name = data[1][0]
    art_nr = data[1][1]
    x = data[2]
    y = data[3]
    valve_data = data_transformer.polynomial_dict(x, y, deg)
    valve_data['name'] = name
    valve_data['article_number'] = art_nr
    return valve_data



a = list_csv_in_creation()
print(a)


# base_dir = os.path.abspath(__file__)
# print(base_dir)
# base_dir = os.path.dirname(os.path.abspath(__file__))
# print(base_dir)
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# path_abs = os.path.join(base_dir,'Data_BV', 'CSV_creation','TA-BVS_DN125.csv')
#
# data_v = valve_data_processed(path_abs, 6)
# print(data_v)

####


# xlsx_path1 = 'Data_BV.xlsx'
# output_dir1 = 'CSV_creation'

# print(open_csv_list('CSV_creation/STAD_DN10.csv'))

