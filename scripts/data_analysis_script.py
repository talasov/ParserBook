import os
from collections import Counter

import pandas as pd


def analyze_data():
    current_directory = os.path.dirname(__file__)

    csv_file_path = os.path.join(current_directory, 'table.csv')

    data = pd.read_csv(csv_file_path)

    ids = data['id'].tolist()

    id_counter = Counter(ids)
    ids_with_three_occurrences = [id_value for id_value, count in id_counter.items() if count == 3]
    print("id которые встречаются 3 раза:", ids_with_three_occurrences)

    occurrences_counter = Counter(id_counter.values())
    print("Частота повторений:", occurrences_counter)


if __name__ == "__main__":
    analyze_data()
