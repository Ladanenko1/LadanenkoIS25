# разобрать любой код из PZ(2-9)(я взял из PZ-7 задание 2) с помощью пакета tk
import tkinter as tk
root = tk.Tk()
input_string = tk.StringVar()
text_entry = tk.Entry(root, textvariable=input_string)
def format_string():
    formatted_string = input_string.get().title()
    result_label.configure(text=formatted_string)

format_button = tk.Button(root, text="Форматировать", command=format_string)
result_label = tk.Label(root)
text_entry.pack()
format_button.pack()
result_label.pack()
root.mainloop()
