from tkinter import Tk, Label, Entry, Button, DISABLED, StringVar 
 
def convert(): 
    """Takes miles entered, converts them to km, and displays the result"""
    miles = float(entryMiles.get()) 
    kilometers.set(str(miles * 1.60934)) 
 
#создание ГУИ
 
rootWindow = Tk() #создание окна
rootWindow.title("Miles to kilometers") 
rootWindow.geometry('500x200+0+0') 
rootWindow.grid_columnconfigure(1, weight = 1) 
 
labelMiles = Label(rootWindow, text='Distance in miles:') # текст 
labelMiles.grid(row=0, column=0) 
 
labelKm = Label(rootWindow, text='Distance in kilometers:') # текст
labelKm.grid(row=2, column=0) 
 
entryMiles = Entry(rootWindow) # ввод
entryMiles.grid(row=0, column=1, sticky='w,e') 
 
kilometers = StringVar() # вывод
entryKm = Entry(rootWindow, textvariable = kilometers, state=DISABLED) 
entryKm.grid(row=2, column=1, sticky='w,e') 
 
convertButton = Button(rootWindow, text='Convert', command = convert) # кнопка
convertButton.grid(row=1, column=1) 
 
# цикл 
 
rootWindow.mainloop() 