# Программа анализа .csv файлов

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd

# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name = fd.askopenfilename(initialdir=my_dir)
    return name

# Обработка csv файла при помощи pandas
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=[0], sep=';')
    cnt_rows = df.shape[0]
    cnt_columns = df.shape[1]
    label_11['text'] = cnt_rows
    label_21['text'] = cnt_columns
    return df

# Выборка столбца в список
def get_column(df, column_ix):
    cnt_rows = df.shape[0]
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i, column_ix])
    return lst

# Если в этом поле Фамилия, пусть вернет True
def meet_last_name(field):
    checkfor = ['ов', 'ова', 'ин', 'ина', 'ев', 'ева', 'ко', 'ий']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат Фамилию, пусть вернет True
def list_meet_last_name(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_last_name(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.5:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Если в этом поле Отчество, пусть вернет True
def meet_middle_name(field):
    checkfor = ['вич', 'вна']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат Отчество, пусть вернет True
def list_meet_middle_name(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_middle_name(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.1:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Если в этом поле Имя, пусть вернет True
def meet_name(field):
    checkfor = ['Вера', 'Анатолий', 'Мария', 'Артём', 'Алексей',
     'Наталья', 'Оксана', 'Галина', 'Марина', 'Вероника', 'Андрей',
     'Екатерина', 'Борис', 'Диана', 'Владимир', 'Николай', 'Павел',
     'Денис', 'Дмитрий', 'Олег', 'Игорь', 'Татьяна', 'Анна', 'Александр',
     'Александра', 'Анастасия', 'Никита', 'Елена', 'Тамара', 'Ольга']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат Имя, пусть вернет True
def list_meet_name(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_name(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.1:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Если в этом поле адрес e-mail, пусть вернет True
def meet_email(field):
    checkfor = ['@mail.ru', '@yandex.ru', '@rambler.ru', '@gmail.com', '@yahoo.com']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат адрес e-mail, пусть вернет True
def list_meet_email(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_email(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.5:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Если в этом поле адрес e-mail.ru, пусть вернет True
def meet_email_ru(field):
    checkfor = ['.ru']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат адрес e-mail.ru, пусть вернет True
def list_meet_email_ru(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_email_ru(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.5:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Если в этом поле дата в формате АМ/РМ, пусть вернет True
def meet_date_am_pm(field):
    checkfor = [' AM', ' PM']
    for s in checkfor:
        if s in str(field):  # Нашлось!
            return True
    return False  # Ничего не совпало!

# если в этом списке многие элементы содержат дату в формате АМ/РМ, пусть вернет True
def list_meet_date_am_pm(fields_list):
    counter_total = 0
    counter_meet = 0
    for list_item in fields_list:
        counter_total += 1
        if meet_date_am_pm(list_item):
            counter_meet += 1
    # Конец подсчета
    ratio = counter_meet / counter_total
    if ratio > 0.5:
        return True, ratio
    # Не набралось нужного количества совпадений
    return False, ratio

# Пройти все столбцы
def check_all_columns(df):
    columns_cnt = df.shape[1]
    for i in range(columns_cnt):  # От 0 до columns_cnt-1
        lst = get_column(df, i)
        
        # Первый критерий
        result1 = list_meet_name(lst)
        if result1[0]:
            output_text.insert(tk.END, 'В столбце ' + str(i+1)
            + ' предположительно содержится имя.' + os.linesep)
            output_text.insert(tk.END, 'Процент совпадений ' + '{:.2f}'.format(result1[1] * 100)
            + '%.' + os.linesep * 2)
            continue  # Все нашли, можно идти к следующему столбцу
        # Второй критерий
        result2 = list_meet_email(lst)
        if result2[0]:
            output_text.insert(tk.END, 'В столбце ' + str(i+1)
            + ' предположительно содержится адрес e-mail' + os.linesep)
            output_text.insert(tk.END, 'Процент совпадений ' + '{:.2f}'.format(result2[1] * 100)
            + '%.' + os.linesep * 2)
            result6 = list_meet_email_ru(lst)
            if result6[0]:
                output_text.insert(tk.END, '-' * 65 + 'Большинство студентов из России.' + os.linesep)
                output_text.insert(tk.END, 'Всего студентов с российким адресом e-mail: ' + '{:.2f}'.format(result6[1] * 100)
                + '%.' + os.linesep + '-' * 65  + os.linesep * 2)
            continue  # Все нашли, можно идти к следующему столбцу
        # Третий критерий
        result3 = list_meet_date_am_pm(lst)
        if result3[0]:
            output_text.insert(tk.END, 'В столбце ' + str(i+1)
            + ' предположительно содержится дата в формате АМ/РМ.' + os.linesep)
            output_text.insert(tk.END, 'Процент совпадений ' + '{:.2f}'.format(result3[1] * 100)
            + '%.' + os.linesep * 2)
            continue  # Все нашли, можно идти к следующему столбцу
        # Четвертый критерий
        result4 = list_meet_last_name(lst)
        if result4[0]:
            output_text.insert(tk.END, 'В столбце ' + str(i+1)
            + ' предположительно содержится фамилия.' + os.linesep)
            output_text.insert(tk.END, 'Процент совпадений ' + '{:.2f}'.format(result4[1] * 100)
            + '%.' + os.linesep * 2)
            continue  # Все нашли, можно идти к следующему столбцу
        # Пятый критерий
        result5 = list_meet_middle_name(lst)
        if result5[0]:
            output_text.insert(tk.END, 'В столбце ' + str(i+1)
            + ' предположительно содержится отчество.' + os.linesep)
            output_text.insert(tk.END, 'Процент совпадений ' + '{:.2f}'.format(result5[1] * 100)
            + '%.' + os.linesep * 2)
            continue  # Все нашли, можно идти к следующему столбцу

        # Соответствия критериям не найдено
        output_text.insert(tk.END, 'Предположений для столбца ' + str(i+1)
            + ' не найдено.' + os.linesep * 2)


# Обработчик нажатия кнопки
def process_button():
    file_name = do_dialog()
    label_01['text'] = file_name
    df = pandas_read_csv(file_name)
#    lst = get_column(df, 2)
#    for item in lst:
#        output_text.insert(tk.END, str(item) + ' ' 
#        + str(meet_name(item)) + os.linesep)
#    if list_meet_name(lst):
#        output_text.insert(tk.END, 'В списке предположительно содержится имя.' 
#        + os.linesep)
#    else:
#        output_text.insert(tk.END, 'Предположений для списка не найдено.' 
#        + os.linesep)
    check_all_columns(df)
    mb.showinfo(title=None, message='Готово')

# Создание главного окна
window = tk.Tk()
window.geometry('660x550+300+200')
window.title('Программа анализа .csv файлов')

# Создание меток вывода
label_00 = tk.Label(text='Файл:')
label_00.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_01 = tk.Label(window, text='', anchor='w', relief='sunken', bg='azure', bd=3)
label_01.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

label_10 = tk.Label(text='Строк:')
label_10.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_11 = tk.Label(text='', relief='sunken', bg='azure', bd=3)
label_11.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

label_20 = tk.Label(text='Столбцов:')
label_20.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_21 = tk.Label(text='', relief='sunken', bg='azure', bd=3)
label_21.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

# Создание текстового вывода с прокруткой
output_text = st(height=22, width=65, bd=5,  selectforeground='snow', selectbackground='blue4')
output_text.grid(row=3, column=1, padx=10, pady=10, sticky='w')

# Создание кнопки
button = tk.Button(window, text='Прочитать файл', command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
