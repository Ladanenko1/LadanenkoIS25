import tkinter as tk
from tkinter import StringVar, OptionMenu
# Создаем основное окно приложения
root = tk.Tk()


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

selected_option = StringVar(root)
selected_option.set("Выберите область")


options = ["Ростовская область", "московская область", "Краснодарский Край"]

# Создание виджета OptionMenu
option_menu = OptionMenu(root, selected_option, *options)
option_label = tk.Label(root, text ='Регион')

selecte_option = StringVar(root)
selecte_option.set("Выберите страну")


optionss = ["Россия", "Украина", "Беларусь"]

# Создание виджета OptionMenu
con_menu = OptionMenu(root, selecte_option, *optionss)
con_label= tk.Label(root, text ='Страна')

submit_button = tk.Button(root, text="Отправить")

foods = [u'Соленое',u'Сладкое',u'Острое']

select_option = StringVar(root)
select_option.set("Выберите предпочтения в еде")


optionsss = ["сладкое", "соленое", "острое"]

# Создание виджета OptionMenu
food_menu = OptionMenu(root, select_option, *optionsss)
food_label= tk.Label(root, text ='Еда')

submit_button = tk.Button(root, text="Отправить")

var1 = tk.IntVar()
check1= tk.Radiobutton(root,text=u'Карта',variable=var1,value = 1 )
check2 = tk.Radiobutton(root, text = u'Наличные',variable=var1,value =2 )
var1_entry = tk.Label(root, text = 'Режим оплаты')

name_Bank = tk.Label(root, text="Первое имя:")
name_bank_entry = tk.Entry(root)

zp = tk.Label(root,text ='День зарплаты')
zp_entry = tk.Entry(root)

# # Размещаем элементы на основном окне
f_name_label.grid(row=0, column=0, pady=5)
f_name_entry.grid(row=0, column=1, pady=5)


s_name_label.grid(row=1, column=0, pady=5)
s_name_entry.grid(row=1, column=1, pady=5)

email_label.grid(row=7, column=0, pady=5)
email_entry.grid(row=7, column=1, pady=5)

adress_label.grid(row=3, column=0, pady=5)
adress_entry.grid(row=3, column=1, pady=5)

phone_label.grid(row=8, column=0, pady=5)
phone_entry.grid(row=8, column=1, pady=5)

city_label.grid(row=4, column= 0, pady=5)
city_entry.grid(row=4, column = 1, pady=5)

company_label.grid(row=2, column=0, pady=5)
company_entry.grid(row=2, column=1, pady=5)

submit_button.grid(row=9, column=1, pady=5)

option_menu.grid(row=5, column= 1 , pady=5)
option_label.grid(row=5,column=0, pady= 5 )

con_menu.grid(row=6,column=1, pady=5)
con_label.grid(row=6, column=0, pady=5)

food_menu.grid(row=0, column=4, pady=5)
food_label.grid(row=0, column=3, pady=5)

check1.grid(row=1,column=5, pady=5)
check2.grid(row=1,column=4, pady=5)


var1_entry.grid(row=1,column=3, pady=5)

name_Bank.grid(row=2,column= 3, pady=5)
name_bank_entry.grid(row=2,column=4, pady=5)

zp.grid(row=3,column=3, pady=5)
zp_entry.grid(row=3,column=4, pady=5)
root.title("Резюме")
root.resizable(False, False)
root.geometry('800x500')

# Запускаем основное окно приложения
root.mainloop()
