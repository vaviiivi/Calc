import tkinter as tk

def get_dci(root, weight, height, age, gender, k):
    bmi = int(weight.get())*10 + 6.25*int(height) - 5*int(age)
    if gender == "Ж":
        bmi = (bmi - 161) * float(k)
    else:
        bmi = (bmi + 5) * float(k)
    tk.Label(root, text=bmi, font=("Arial", 18)).grid(row=12, column=1)