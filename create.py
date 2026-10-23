import tkinter as tk

def create_entry(root, text, variable, l_row, l_column, e_row, e_column):
    tk.Label(root, text=text, font=("Arial", 18)).grid(row=l_row, column=l_column, padx=10, pady=10)
    (tk.Entry(
        root,
        textvariable=variable,
        relief="solid",
        bd=1,
        highlightbackground="white",
        highlightcolor="blue",
        highlightthickness=1, )
     .grid(row=e_row, column=e_column, padx=10, pady=10))


def create_activity_options(root,kof):
    activity_options = [
        ("Минимальная (сидячий образ)", "1.2"),
        ("Низкая (1-3 тренировки/нед)", "1.375"),
        ("Средняя (3-5 тренировок/нед)", "1.55"),
        ("Высокий", "1.725"),
        ("Экстремальный","1.9")
    ]

    row = 6
    for text, k in activity_options:
        tk.Label(root, text=text, font=("Arial", 18)).grid(row=row, column=0)
        tk.Radiobutton(root,text=k,variable=kof,value=k, font=("Arial", 18)).grid(row=row, column=1)
        row += 1