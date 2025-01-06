import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def make_db():
    conn = sqlite3.connect('filmi.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS films (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              year Integer,
              genre Text)''')
    conn.commit()
    conn.close()

def save_data():
    title = entry_title.get()
    year = entry_year.get()
    genre = entry_genre.get()


    if title and year and genre:
        try:
            year = int(year)
            conn = sqlite3.connect('filmi.db')
            c = conn.cursor()
            c.execute('INSERT INTO films (title, year, genre) VALUES (?, ?, ?)', (title, year, genre))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Dati ir saglabati")

            entry_title.delete(0, tk.END)
            entry_year.delete(0, tk.END)
            entry_genre.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error")

    else:
        messagebox.showerror("Error1")


def load_film_titles():
    try:
        film_combobox['values'] = ()
        conn = sqlite3.connect('filmi.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title from films")
        titles = []
        title_all=cursor.fetchall()
        for title in title_all:
            titles.append(str(title[0]))
        conn.close()

        film_combobox['values'] = titles

    except Exception as e:
        messagebox.showerror("Error", f"Neizdevas nolasīt grāmatu nosaukumu: {e}")


def read_data():
    try:
        selected_film = film_combobox.get()
        if not selected_film:
            messagebox.showwarning("Bridinājums")
            return
        conn = sqlite3.connect('filmi.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * from books where title = ?", (selected_film,))
        film = cursor.fetchone()
        conn.close()
        
        if film:
            messagebox.showinfo("Grāmatas info", f"Nosaukums: {film[0]}\nGads: {film[1]}\nŽanrs: {film[2]}")
        else:
            messagebox.showwarning("Error", "Neizdevas atrast gramatu")

    except Exception as e:
        messagebox.showerror("Error", f"Neizdevas paradit grāmatu informaciju: {e}")



root = tk.Tk()
root.title("Filma sistema")

tk.Label(root, text="Pievienot filmu:", padx=10, pady=10).grid(row=0, column=0)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=2, column=0, padx=10, pady=5)
entry_genre = tk.Entry(root)
entry_genre.grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Saglabat", command=save_data).grid(row=4, column=0, padx=10, pady=10)

tk.Label(root, text="Apskatīt info").grid(row=0, column=1, padx=10, pady=10)
film_combobox = ttk.Combobox(root, width=50, state="readonly").grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Radīt info", command=read_data).grid(row=2, column=1, padx=10, pady=10)

make_db()
load_film_titles()
root.mainloop()