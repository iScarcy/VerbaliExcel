from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Verbali Excel")
# dimensioni e posizione finestra
root.geometry("800x600+360+100") 
root.iconbitmap('./excel.ico')

#massimo e minimo ridimensionamento 
root.minsize(100,100)
root.maxsize(1920,1900)

file_path = ""

def saluta():
    file_path=filedialog.askdirectory()


label=Label(text="ciao", font=("Helvetica",24))

label.pack(padx=10, pady=10, side=LEFT)

button = Button(text="Elabora",command=saluta)
button.pack(side=LEFT)



root.mainloop()