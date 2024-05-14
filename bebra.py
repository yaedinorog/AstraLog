from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk
from random import *
from datetime import datetime, timedelta
import pandas as pd
import os.path

def analyze_logs():
    log_file = search_entry.get() 
    log_level = log_level_var.get() 
    time_interval = int(time_button.get()) 

    if not os.path.exists(log_file): # Проверяем существование файла
        result_text.delete("1.0", END)
        result_text.insert(END, "Файл не найден, проверьте правильность написания пути")
        return

    errors = []
    current_time = datetime.now()
    time_threshold = current_time - timedelta(minutes=time_interval)

    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(rf"^(.*?) ({log_level}) (.*)$", line)
            if match:
                timestamp_str = match.group(1).strip()
                try: 
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    if timestamp >= time_threshold:
                        errors.append({'message': match.group(3).strip()})
                except ValueError: 
                    print(f"Ошибка при парсинге временной метки: {timestamp_str}") 

    df = pd.DataFrame(errors)
    result_text.delete("1.0", END)

    if not df.empty:
        result_text.insert(END, f"Количество ошибок за последние {time_interval} минут: {len(df)}\n\n") 
        result_text.insert(END, "Типы ошибок:\n") 
        result_text.insert(END, df['message'].value_counts()) 
    else: 
        result_text.insert(END, "Ошибок не найдено.")

def info_but(): 
    info_window = Tk() 
    info_window.title("Справка") 
    info_window.geometry("250x500") 
 
def open_file(): 
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите лог файл", filetypes=(("Log files", "*.log"), ("all files", "*.*"))) 
    if filename: 
        search_entry.delete(0, END) 
        search_entry.insert(0, filename) 

root = Tk() 
root.title("Анализатор данных") 

menu_frame = Frame(root) 
menu_frame.pack(fill=X)  

info_button = ttk.Button(menu_frame, text="info", command=info_but) 
info_button.pack(side=LEFT, padx=5)   

search_entry = ttk.Entry(menu_frame) 
search_entry.pack(side=LEFT, expand=True, fill=X, padx=5)   

file_button = ttk.Button(menu_frame, text="Выбрать файл", command=open_file) 
file_button.pack(side=LEFT, padx=5) 

log_level_var = StringVar(menu_frame) 
log_level_var.set("ERROR") 
log_level_options = ["DEBUG", "INFO", "WARNING", "ERROR"] 
log_level_dropdown = OptionMenu(menu_frame, log_level_var, *log_level_options) 
log_level_dropdown.pack(side=LEFT, padx=5) 

time_button = StringVar(menu_frame) 
time_button.set("30") 
time_button_options = ["5", "15", "30", "60"] 
time_button_dropdown = OptionMenu(menu_frame, time_button, *time_button_options) 
time_button_dropdown.pack(side=LEFT, padx=5) 

analyze_button = ttk.Button(menu_frame, text="Анализировать", command=analyze_logs)
analyze_button.pack(side=LEFT, padx=5) 

# --- Окно вывода ---
result_text = Text(root, state='disabled') 
result_text.pack(expand=True, fill=BOTH)  

root.mainloop()