import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import csv


def open_csv():
    global f_path
    f_path = filedialog.askopenfilename(filetypes=[("CSV файлы", "*.csv")])
    show_csv()


def show_csv():
    try:
        with open(f_path, "r", newline="") as file:
            csv_reader = csv.reader(file)
            heads = next(csv_reader)
            tree.delete(*tree.get_children())

            tree["columns"] = heads
            combobox["values"] = heads

            for col in heads:
                tree.heading(col, text=col)
                tree.column(col, width=75, anchor="center")

            for row in csv_reader:
                tree.insert("", "end", values=row)

    except Exception as error:
        label.config(text=f"Ошибка: {str(error)}.")


def mean_csv():
    try:
        df = pd.read_csv(f_path)
        column = combobox.get()
        mean = df[column].mean()
        label.config(text=f"Среднее значение для стобца {column}: {mean}.")

    except Exception as error:
        label.config(text=f"Ошибка: {str(error)}.")


def min_csv():
    try:
        df = pd.read_csv(f_path)
        column = combobox.get()
        min_v = df[column].min()
        label.config(text=f"Минимальное значение для стобца {column}: {min_v}.")

    except Exception as error:
        label.config(text=f"Ошибка: {str(error)}.")


def max_csv():
    try:
        df = pd.read_csv(f_path)
        column = combobox.get()
        max_v = df[column].max()
        label.config(text=f"Максимальное значение для стобца {column}: {max_v}.")

    except Exception as error:
        label.config(text=f"Ошибка: {str(error)}.")


def filter_csv():
    try:
        df = pd.read_csv(f_path)
        column = combobox.get()
        const = int(input_box.get())
        new_df = df[df[column] == const]
        tree.delete(*tree.get_children())

        for col in new_df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=75, anchor="center")
        for i, row in new_df.iterrows():
            tree.insert("", "end", values=list(row))

    except Exception as error:
        label.config(text=f"Ошибка: {str(error)}.")


root = tk.Tk()
root.title("CSV анализатор")
root.geometry("1000x750")

tree = ttk.Treeview(root, show="headings")
tree.pack(fill="both", expand=True, padx=10, pady=10)

label = tk.Label(root, text="", padx=10, pady=10)
label.pack(anchor="nw")

start_button = tk.Button(root, text="Открыть CSV файл", command=open_csv)
start_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10)

f_label = tk.Label(root, text="Выберите столбец", padx=10, pady=10)
f_label.pack(anchor="nw")

combobox = ttk.Combobox(root)
combobox.pack(anchor="nw", ipadx=5, ipady=5, padx=10, pady=10)

i_label = tk.Label(root, text="Введите значение для фильтрации", padx=10, pady=10)
i_label.pack(anchor="nw")

input_box = ttk.Entry(root)
input_box.pack(anchor="nw", ipadx=5, ipady=5, padx=10, pady=10)

sred_button = tk.Button(root, text="Найти среднее", command=mean_csv)
sred_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10, side="left")

min_button = tk.Button(root, text="Найти минимальное", command=min_csv)
min_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10, side="left")

max_button = tk.Button(root, text="Найти максимальное", command=max_csv)
max_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10, side="left")

filter_button = tk.Button(root, text="Фильтровать по значению", command=filter_csv)
filter_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10, side="left")

recover_button = tk.Button(root, text="Вернуть данные", command=show_csv)
recover_button.pack(anchor="nw", ipadx=10, ipady=10, padx=10, pady=10)

root.mainloop()
