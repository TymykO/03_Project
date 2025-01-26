from Modules.CSV import csv_processor
from Modules.CSV.csv_processor import valve_data_processed, list_csv_in_creation
from Modules.Utils.file_manager import get_csv_files
import os


#Закачуємо всі данні з Data_BV.xlsx у окремі CSV файли, розділені і посортовані для решти процесів
def upd_csv_from_xlsx():
    base_dir = os.path.dirname(__file__)
    directory = os.path.join(base_dir, "Data_BV.xlsx")
    output_dir = os.path.join(base_dir, "CSV_creation")
    return csv_processor.convert_xlsx_to_csv(directory, output_dir)


#################
#Збирає з "CSV_creation" данні клапана і коефіцієнти для рівняння у словник і попертає список з словником для кожного файлу в дерикторії
def download_all_valve_data():
    # base_dir = os.path.dirname(__file__)
    # path_csv_dir = os.path.join(base_dir, "CSV_creation")
    # csv_files = get_csv_files(path_csv_dir)
    csv_files = list_csv_in_creation()
    deg = 6
    for path_csv in csv_files[1]:
        data = valve_data_processed(path_csv, deg)
        print(data)
#################

def upd_all():
    pass


a = upd_csv_from_xlsx()
print(a)
print(download_all_valve_data())