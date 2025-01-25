from Data_BV import csv_processor as csv_pro
import numpy
import os

#-----------------To Do-----------------#

def from_csv_data_sort(path: str):
    data = csv_pro.open_csv_list(path)
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

def polynomial_equation_6(x, y):
    deg = 6
    coefficients = numpy.polyfit(x, y, 6)
    c_value = {}
    for i, value in enumerate(coefficients):
        try:
            a = i + 1
            e = len(coefficients) - a
            x = f'x{e}'
            c_value[x] = float(str(value))
        except ValueError as e:
            print(f"Error converting value: {value} to float — {e}")
    return c_value



# path_s = "Data_BV/CSV_creation/STAD_DN10.csv"
# path = os.path.abspath(path_s)
# print(from_csv_data_sort(path))

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_abs = os.path.join(base_dir,'Data_BV', 'CSV_creation','STAD_DN25.csv')
# print(from_csv_data_sort(path_abs)[0])
# print(from_csv_data_sort(path_abs)[1])
# print(from_csv_data_sort(path_abs)[2])
# print(from_csv_data_sort(path_abs)[3])

x = from_csv_data_sort(path_abs)[2]
y = from_csv_data_sort(path_abs)[3]

xs = polynomial_equation_6(from_csv_data_sort(path_abs)[2], from_csv_data_sort(path_abs)[3])

# c_value = {}
# for i, value in enumerate(xs):
#     try:
#         a = i + 1
#         e = len(xs)-a
#         x = f'x{e}'
#         c_value[x] = float(str(value))
#     except ValueError as e:
#         print(f"Error converting value: {value} to float — {e}")

print(xs)
print(len(xs))
