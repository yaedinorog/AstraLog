import pandas as pd
import data as data

import arg_parser
import time
import os


# function for analyze log files

def analyze_logs(log_file, level,):
    with open(log_file, 'r') as f:
        log_data = f.readlines()

    global_data = data.data_frame_regex(log_data, level)
    print("\n")

    time.sleep(2)

    writing_to_file = input("Записать в файл?(y/n) ")
    if writing_to_file in ['y', 'Y', 'yes', 'да', 'д', 'Д']:
        path_to_file = input("Напишите путь и куда сохранить файл -> ")
        with open(f'{os.path.expanduser(path_to_file)}', "w") as write_file:
            write_file.write(global_data['message'].value_counts().to_string())
    else:
        print('Конец!')


if __name__ == "__main__":
    args = arg_parser.parser_args()
    analyze_logs(args.log_file, args.level)
