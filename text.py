import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Найти и открыть файл"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]  #Форматы файлов для открытия
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:   #отрывает файл
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Сохраняет файл как новый"""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],   #Форматы файла
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:   #Сохранение
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

window = tk.Tk()   #Гланое окно
window.title("Simple Text Editor")    #Название окна

window.rowconfigure(0, minsize=800, weight=1)    #конфигурация строк 
window.columnconfigure(1, minsize=800, weight=1)  #конфигурация столбцов

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)    #кнопка открытия
btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)   #кнопка сохранения

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)   #расположение элементов
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()   #главный цикл для работы