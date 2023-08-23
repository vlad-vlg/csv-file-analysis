# Программа анализа .scv файлов

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd

# Диалог открытия файла
def do_dialog():
    name = fd.askopenfilename()
    return name

# Обработчик нажатия кнопки
def process_button():
    do_dialog()
    mb.showinfo(title=None, message='Готово')

#Создание главного окна
window = tk.Tk()
window.geometry('550x550')
window.title('Программа анализа .scv файлов')

# Создание меток вывода
label_00 = tk.Label(text = 'Файл:')
label_00.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_01 = tk.Label(text = '')
label_01.grid(row=0, column=1, sticky='w')

label_10 = tk.Label(text = 'Строк:')
label_10.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_11 = tk.Label(text = '')
label_11.grid(row=1, column=1, sticky='w')

label_20 = tk.Label(text = 'Столбцов:')
label_20.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_21 = tk.Label(text = '')
label_21.grid(row=2, column=1, sticky='w')

# Создание текстового вывода
output_text = st(height=22, width=50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Создание кнопки
button = tk.Button(window, text='Прочитать файл', command=process_button)
button.grid(row=4, column=1)




# Запуск цикла mainloop
window.mainloop()
