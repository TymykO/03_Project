from Modules.CSV import csv_processor
import os

def upd_csv_from_xlsx():
    base_dir = os.path.dirname(__file__)
    directory = os.path.join(base_dir, "Data_BV.xlsx")
    output_dir = os.path.join(base_dir, "CSV_creation")
    return csv_processor.convert_xlsx_to_csv(directory, output_dir)

def upd_all():
    pass


a = upd_csv_from_xlsx()
print(a)