import os

def get_csv_files(directory: str):
    """
    Збирає список CSV-файлів у заданій папці та їх абсолютні шляхи.

    :param directory: Шлях до папки, де шукати файли.
    :return: Два списки — назви файлів і абсолютні шляхи до цих файлів.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")

    # Список для назв файлів
    csv_files = []
    # Список для абсолютних шляхів
    csv_paths = []

    # Ітеруємося по вмісту папки
    for file in os.listdir(directory):
        if file.endswith('.csv'):  # Перевіряємо розширення
            csv_files.append(file)
            csv_paths.append(os.path.abspath(os.path.join(directory, file)))

    return csv_files, csv_paths
