import tkinter as tk
from create import create_entry, create_activity_options
from calculation import get_dci

def get_dci():
    bmi = int(weight.get())*10 + 6.25*int(height.get()) - 5*int(age.get())
    if gender == "Ж":
        bmi = (bmi - 161) * float(kof.get())
    else:
        bmi = (bmi + 5) * float(kof.get())
    tk.Label(root, text=bmi, font=("Arial", 18)).grid(row=12, column=1)

root = tk.Tk()
root.geometry("600x900")
root.configure(background="#AFEADC")
bg_color = "#AFEADC"

font=("Arial", 18)

weight = tk.StringVar()
height = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()
kof = tk.StringVar()

tk.Label(root, text="Калькулятор калорий", font=("Arial", 24, "bold"),background=bg_color).grid(row=0, column=0)

#  Поля ввода
create_entry(root, "Вес:", weight, 1, 0, 1, 1)
create_entry(root, "Рост:", height, 2, 0, 2, 1)
create_entry(root, "Возраст:", age, 3, 0, 3, 1)

#  Выбор пола
tk.Label(root, text="Пол:", font=font).grid(row=4, column=0,padx=10, pady=10)
tk.Radiobutton(root, text="М", variable=gender, font=font).grid(row=4,column=1)
tk.Radiobutton(root, text="Ж", variable=gender, font=font).grid(row=4,column=2)

# Выбор коэффициента активности
tk.Label(root, text="Коэффицент", font=font).grid(row=5, column=0)
create_activity_options(root,kof)

tk.Button(root,text="Высчитать",command=get_dci, font=font).grid(row=12)

root.mainloop()