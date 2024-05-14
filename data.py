import re
import pandas as pd


def data_frame_regex(file, levels):
    error_regex = rf"^(.*?) ({levels}) (.*)$"

    errors = []
    for line in file:
        match = re.search(error_regex, line)
        if match:
            errors.append({
                'timestamp': match.group(1),
                'level': match.group(2),
                'message': match.group(3).strip()})

    df = pd.DataFrame(errors)

    try:
        print("Кол-во ошибок:", len(df))
        print(f"\nТип ошибок: {levels}")
        print(df['message'].value_counts())


    except KeyError as k:
        print('\n!!!!!!!!!')
        print(f'\nНе найдено ни одной ошибки {levels}')

    return df
