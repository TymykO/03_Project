from Modules.CSV.csv_processor import valve_data_processed, list_csv_in_creation, convert_xlsx_to_csv, save_list_csv, \
    prepare_data_for_csv
from Modules.Utils.file_manager import get_csv_files
import os


#Закачуємо всі данні з Data_BV.xlsx у окремі CSV файли, розділені і посортовані для решти процесів, повертає список записаних файлів до CSV_creation
def upd_csv_from_xlsx():
    base_dir = os.path.dirname(__file__)
    directory = os.path.join(base_dir, "Data_BV.xlsx")
    output_dir = os.path.join(base_dir, "CSV_creation")
    return convert_xlsx_to_csv(directory, output_dir)

#Збирає з "CSV_creation" данні клапана і коефіцієнти для рівняння у словник і попертає список з словником для кожного файлу в дерикторії
def download_all_valve_data():
    csv_files = list_csv_in_creation()
    deg = 6
    valves_data = []
    for path_csv in csv_files[1]:
        data = valve_data_processed(path_csv, deg)
        valves_data.append(data)
    return valves_data

#Записує дані клапану і коефіцієнти рівняння у зручній формі.
def save_all_valve_data():
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "save_all_valve_data.csv")
    data = download_all_valve_data() #Список зі словників
    data = prepare_data_for_csv(data) #Перетворення словників у списку на списки з ключами в першій лінійці
    print(data)
    save_list_csv(data, output_dir)
    return output_dir

def upd_all():
    pass


# a = save_all_valve_data()
# print(a)
# # print(download_all_valve_data())