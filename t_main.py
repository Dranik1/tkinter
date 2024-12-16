from tkinter import *
from random import *



root=Tk()
root.title('Spele')
root.geometry('600x600')
root.resizable(width=False, height=False)

root.config(bg='orange')

def WHYknb():
    knb=['Akmens', 'Šķēres', 'Papīrs']
    value=choice(knb)
    labelText.configure(text=value)


labelText=Label(root, 
              text="", 
              font=('Comic Sans MS', 20, 'bold'),
              bg='green',
              fg='blue')

labelText.place(x=250, y=100)

stone=Button(root,
             text="Akmens",
             font=('Comic Sans MS', 20, 'bold'),
             bg='white',
             command=WHYknb)

stone.place(x=20, y=300)

scissors=Button(root,
             text="Šķēres",
             font=('Comic Sans MS', 20, 'bold'),
             bg='white',
             command=WHYknb)

scissors.place(x=220, y=300)

paper=Button(root,
             text="Papīrs",
             font=('Comic Sans MS', 20, 'bold'),
             bg='white',
             command=WHYknb)

paper.place(x=420, y=300)


root.mainloop()