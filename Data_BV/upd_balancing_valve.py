from Modules.CSV.csv_processor import valve_data_processed, list_csv_in_creation, convert_xlsx_to_csv, save_list_csv, \
    prepare_data_for_csv, from_csv_data_sort, valve_data_aquapresso
import os
from Modules.Transform.data_transformer import polynomial_coeff, graph_eq_bv, save_figure

#Закачуємо всі дані з Data_BV.xlsx в окремі CSV файли, розділені та посортовані для решти процесів, повертає список записаних файлів до CSV_creation
def creation_csv_from_xlsx():
    base_dir = os.path.dirname(__file__)
    directory = os.path.join(base_dir, "Data_BV.xlsx")
    output_dir = os.path.join(base_dir, "CSV_creation")
    return convert_xlsx_to_csv(directory, output_dir, "Sheet1")

#Збирає з "CSV_creation" дані клапана і коефіцієнти для рівняння у словник і попертає список зі словником для кожного файлу в дерикторії
def download_all_valve_data():
    csv_files = list_csv_in_creation()
    deg = 6
    valves_data = []
    for path_csv in csv_files[1]:
        data = valve_data_processed(path_csv, deg)
        valves_data.append(data)
    return valves_data

#Збирає з "CSV_creation" дані для aquapresso і клапана коефіцієнти для рівняння у словник і повертає список зі словником для кожного файлу в дерикторії
def download_valve_data_aquapresso():
    csv_files = list_csv_in_creation()
    deg = 6
    valves_data = []
    for path_csv in csv_files[1]:
        data = valve_data_aquapresso(path_csv, deg)
        valves_data.append(data)
    return valves_data

#Записує дані клапану і коефіцієнти рівняння у зручній формі в одному файлі.
def all_valve_coefficients_to_csv():
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "all_valve_coefficients.csv")
    data = download_all_valve_data() #Список зі словників
    data = prepare_data_for_csv(data) #Перетворення словників у списку на списки з ключами в першій лінійці
    save_list_csv(data, output_dir) #Записує список зі словників
    return output_dir

#Записує дані aquapresso, клапану і коефіцієнти рівняння у зручній формі в одному файлі.
def all_valve_coefficients_to_aquapresso():
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "valve_data_aquapresso.csv")
    data = download_valve_data_aquapresso() #Список зі словників
    data = prepare_data_for_csv(data) #Перетворення словників у списку на списки з ключами в першій лінійці
    save_list_csv(data, output_dir) #Записує список зі словників
    return output_dir

#Записує зображення графіків у .png для всіх файлів .csv у директорії CSV_creation
def save_all_graph_valve():
    #Створення шляху запису зображення
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, "Graphs")

    #Створення списку шляхів до файлів csv
    paths_data = list_csv_in_creation()
    csv_paths = paths_data[1]

    #Створення списку для зберігання назв створених зображень
    graphs = []

    for path in csv_paths:
        #Витягую дані для побудови графіку
        data_csv = from_csv_data_sort(path)
        x = list(data_csv[2])
        y = list(data_csv[3])
        name = str(data_csv[1][0])

        #Обчислення коефіціентів
        deg = 6 #Степінь полінома
        coefficients = polynomial_coeff(x, y, deg)

        #Створення графіка
        fig = graph_eq_bv(x, y, coefficients, name)

        #Запис зображення графіка
        file_name = f'{name}.png'
        output_paht = os.path.join(output_dir, file_name)
        save_figure(fig, output_paht)


        graphs.append(file_name)

    return graphs

def upd_all():
    pass


#print(save_all_graph_valve())
print(all_valve_coefficients_to_aquapresso())

# print(upd_csv_from_xlsx())
# a = save_all_valve_data()
# print(a)
# print(download_all_valve_data())