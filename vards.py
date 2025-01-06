from tkinter import messagebox
import tkinter as tk
import sqlite3


def create_db():
    conn = sqlite3.connect('user_data.db')
    c= conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              birth_year INTEGER,
              adress TEXT,
              tel TEXT)''')
    
    conn.commit()
    conn.close()

def save_data():
    name = entry_name.get()
    surname = entry_surname.get()
    birth_year = entry_birth_year.get()
    adress = entry_adress.get()
    tel = entry_tel.get()

    if name and surname and birth_year:
        try:
            birth_year = int(birth_year)
            conn = sqlite3.connect('user_data.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (name, surname, birth_year, adress, tel) VALUES (?, ?, ?, ?, ?)', (name, surname, birth_year, adress, tel))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Dati ir saglabati")

            entry_name.delete(0, tk.END)
            entry_surname.delete(0, tk.END)
            entry_birth_year.delete(0, tk.END)
            entry_adress.delete(0, tk.END)
            entry_tel.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error")

    else:
        messagebox.showerror("Error1")


create_db()
root = tk.Tk()
root.title("Datu ievade")

label_name = tk.Label(root, text="Vards: ")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name =tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_surname = tk.Label(root, text="Uzvards: ")
label_surname.grid(row=1, column=0, padx=10, pady=5)
entry_surname =tk.Entry(root)
entry_surname.grid(row=1, column=1, padx=10, pady=5)

label_birth_year = tk.Label(root, text="Dzimsanas gads: ")
label_birth_year.grid(row=2, column=0, padx=10, pady=5)
entry_birth_year =tk.Entry(root)
entry_birth_year.grid(row=2, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Adress: ")
label_name.grid(row=3, column=0, padx=10, pady=5)
entry_adress =tk.Entry(root)
entry_adress.grid(row=3, column=1, padx=10, pady=5)

label_name = tk.Label(root, text="Telefons: ")
label_name.grid(row=4, column=0, padx=10, pady=5)
entry_tel =tk.Entry(root)
entry_tel.grid(row=4, column=1, padx=10, pady=5)

btn = tk.Button(root, text="Saglabat", command=save_data)
btn.grid(row=5, columnspan=2, pady=20)


root.mainloop()