import tkinter as tk

# Создаем основное окно приложения
root = tk.Tk()
# import tkinter as tk

#
# # Создаем основное окно приложения
# root = tk.Tk()
# root.title("Регистрация на семинар")
#
# # Добавляем текстовые поля для ввода данных
f_name_label = tk.Label(root, text="Первое имя:")
f_name_entry = tk.Entry(root)

s_name_label = tk.Label(root, text="Второе имя:")
s_name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Электронная почта:")
email_entry = tk.Entry(root)

phone_label = tk.Label(root, text="Телефон:")
phone_entry = tk.Entry(root)

company_label = tk.Label(root, text="Компания:")
company_entry = tk.Entry(root)

adress_label = tk.Label(root, text='Адрес')
adress_entry = tk.Entry(root)

city_label = tk.Label(root, text='Город')
city_entry = tk.Entry(root)

regions = ['Ростовская обсласть','Краснодарский край','Московская область']

# Создаем виджет Listbox
listbox = tk.Listbox(root,)
for region in regions:
    listbox.insert(tk.END, region)
listbox_entry = tk.Label(root, text='pisya')

cons = ['Ростовская обсласть','Краснодарский край','Московская область']

# Создаем виджет Listbox
country = tk.Listbox(root,)
for con in cons:
    country.insert(tk.END, con)
country_entry = tk.Label(root, text = 'sisya')

submit_button = tk.Button(root, text="Отправить")
#


# # Размещаем элементы на основном окне
f_name_label.grid(row=0, column=0)
f_name_entry.grid(row=0, column=1)

# listbox.grid(row=6, column= 1)

s_name_label.grid(row=1, column=0)
s_name_entry.grid(row=1, column=1)

email_label.grid(row=8, column=0)
email_entry.grid(row=8, column=1)

adress_label.grid(row=3, column=0)
adress_entry.grid(row=3, column=1)

phone_label.grid(row=7, column=0)
phone_entry.grid(row=7, column=1)

city_label.grid(row=4, column= 0)
city_entry.grid(row=4, column = 1)

company_label.grid(row=2, column=0)
company_entry.grid(row=2, column=1)

submit_button.grid(row=9, column=1)

listbox.grid(row=5, column= 1 )
listbox_entry.grid(row=5, column = 0)
country.grid(row=6,column=1)
country_entry.grid(row=6, column=0)
root.title("Выбор региона и языков")



# Запускаем основное окно приложения
root.mainloop()
