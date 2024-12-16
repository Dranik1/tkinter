import tkinter as tk



root=tk.Tk()

root.title('PROG')

root.iconbitmap('avalanche_avax_crypto_icon_264373.ico')

root.geometry('600x600')

root.resizable(width=True, height=False)

root.config(bg='yellow')

def click():
    print('Click')

'''btn=tk.Button(root, 
              text="Poga", 
              command=click,
              font='Arial 20',
              bg='green',
              activebackground='orange',
              activeforeground='white',
              fg='blue')
btn.pack()'''

label=tk.Label(root, 
              text="Poga", 
              font='Arial 20',
              bg='green',
              fg='blue')
label.pack()
label.place(x=100, y=100)

img=tk.PhotoImage(file='moai_building_icon_263779.png')
l_logo=tk.Label(root, image=img, width=200, height=200)
l_logo.place(x=100, y=250)

root.mainloop()