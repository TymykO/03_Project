import numpy
import matplotlib.pyplot as plt

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

#Створення графіку з даними та лінією полінома для характеристики клапана
def graph_eq_bv(x_values: list, y_values: list, coefficients: numpy.ndarray, name: str = "name"):
    # Створюємо нову фігуру
    fig, ax = plt.subplots()  # fig — це об'єкт Figure, ax — об'єкт осей
    ax.scatter(x_values, y_values, label='Data', color='red')  # Додаємо точки
    x_fit = numpy.linspace(min(x_values), max(x_values), 500)  # Масив для побудови лінії
    y_fit = numpy.polyval(coefficients, x_fit)  # Обчислюємо значення полінома
    ax.plot(x_fit, y_fit, label='Matched polynomial')  # Додаємо лінію
    ax.set_xlabel('Setpoint')
    ax.set_ylabel('kv')
    ax.set_title(f'Valve characteristics {name}')
    ax.legend()
    ax.grid(True)
    return fig

#Запис графіку
def save_figure(fig, save_path: str):
    try:
        fig.savefig(save_path, format='png', dpi=300)
    except Exception as e:
        print(f'Error saving graph: {e}')
    finally:
        plt.close(fig)


# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path_abs = os.path.join(base_dir,'Data_BV', 'CSV_creation','TA-BVS_DN125.csv')
# path_fig = os.path.join(base_dir,'Data_BV', 'CSV_creation','TA-BVS_DN125.png')
#
# xs = polynomial_coeff(csv_pro.from_csv_data_sort(path_abs)[2], csv_pro.from_csv_data_sort(path_abs)[3], 6)
#
# graph = graph_eq_bv(csv_pro.from_csv_data_sort(path_abs)[2], csv_pro.from_csv_data_sort(path_abs)[3], xs, csv_pro.from_csv_data_sort(path_abs)[1][0])
#
# save_figure(graph, path_fig)
#
# print(xs)
# print(len(xs))
# print(type(xs))
