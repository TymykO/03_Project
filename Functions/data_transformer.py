from Data_BV import csv_processor as csv_pro
import numpy
import os
import matplotlib.pyplot as plt

#---------------------------------------#
#-----------------To Do-----------------#
# Одна функція для витягування даних з csv у потрібній формі

def from_csv_data_sort(path: str):
    data = csv_pro.open_csv_list(path)
    top = data[0]
    data = data[1:]

    sorted_data = sorted(data, key=lambda item: float(item[0].replace(",", "."))) #TO

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

#Створення словника з коефіцієнтами полінома
def polynomial_dict(x: list, y: list, deg: int):
    deg = deg #(x, y, deg = 6)
    coefficients = numpy.polyfit(x, y, deg)
    coeff_dict = {}
    for i, value in enumerate(coefficients):
        try:
            a = i + 1
            e = len(coefficients) - a
            x = f'x{e}'
            coeff_dict[x] = float(str(value))
        except ValueError as e:
            print(f"Error converting value: {value} to float — {e}")
    return coeff_dict

#Коефіцієнти полінома у numpy.polyval
def polynomial_coeff(x: list, y: list, deg: int):
    coefficients = numpy.polyfit(x, y, deg)
    return coefficients

#Створення графіку з даними і лінією полінома для BV
def graph_eq_bv(x_values, y_values, coefficients: numpy.ndarray, name: str = ""):
    plt.scatter(x_values, y_values, label='Data', color='red')
    x_fit = numpy.linspace(min(x_values), max(x_values), 500)
    y_fit = numpy.polyval(coefficients, x_fit)
    plt.plot(x_fit, y_fit, label='Matched polynomial')
    plt.xlabel('setpoint')
    plt.ylabel('kv')
    plt.title(f'Valve characteristics {name}')
    plt.legend()
    plt.grid(True)
    plt.show()


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_abs = os.path.join(base_dir,'Data_BV', 'CSV_creation','TA-BVS_DN125.csv')

xs = polynomial_coeff(from_csv_data_sort(path_abs)[2], from_csv_data_sort(path_abs)[3], 6)

graph_eq_bv(from_csv_data_sort(path_abs)[2], from_csv_data_sort(path_abs)[3], xs, from_csv_data_sort(path_abs)[1][0])

print(xs)
print(len(xs))
print(type(xs))
