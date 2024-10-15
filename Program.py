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

input_path = StringVar()
output_path = StringVar()
file_comuni = StringVar()

 
def setInputPath():
    str=filedialog.askdirectory()
    input_path.set(str)

def setOutputPath():
    str=filedialog.askdirectory()
    output_path.set(str)

def setFileComuni():
    str=filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    file_comuni.set(str)       
   
def elabora():
    print("in: "+input_path)
    print("out: "+output_path)
    print("file:" + file_comuni)

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

frameTitolo = Frame(root)
labelTitolo=Label(frameTitolo, text="Verbali Excel", font=("Helvetica",24))
labelTitolo.pack()

#seconda riga, cartella input
frameInput_titolo = Frame(root)
frameInput_labelTitolo=Label(frameInput_titolo, text="Cartella Input", font=("Helvetica",14))
frameInput_labelTitolo.pack()

frameInput_field = Frame(root)
frameInput_fieldEntiry = ttk.Entry(frameInput_field,textvariable=input_path, width=50)
frameInput_fieldEntiry.pack()

frameInput_button = Frame(root)
frameInput_buttonInput = Button(frameInput_button, text="Scegli", command=setInputPath)
frameInput_buttonInput.pack()

#terza riga, cartella output
frameOutput_titolo = Frame(root)
frameOutput_labelTitolo=Label(frameOutput_titolo, text="Cartella Output", font=("Helvetica",14))
frameOutput_labelTitolo.pack()

frameOutput_field = Frame(root)
frameOutput_fieldEntiry = ttk.Entry(frameOutput_field,textvariable=output_path, width=50)
frameOutput_fieldEntiry.pack()

frameOutput_button = Frame(root)
frameOutput_buttonInput = Button(frameOutput_button, text="Scegli", command=setOutputPath)
frameOutput_buttonInput.pack()

#quarta riga, file comuni
frameFileComuni_titolo = Frame(root)
frameFileComuni_labelTitolo=Label(frameFileComuni_titolo, text="File comuni", font=("Helvetica",14))
frameFileComuni_labelTitolo.pack()

frameFileComuni_field = Frame(root)
frameFileComuni_fieldEntiry = ttk.Entry(frameFileComuni_field,textvariable=file_comuni, width=50)
frameFileComuni_fieldEntiry.pack()

frameFileComuni_button = Frame(root)
frameFileComuni_buttonInput = Button(frameFileComuni_button, text="Scegli", command=setFileComuni)
frameFileComuni_buttonInput.pack()

#quinta riga, progressbar
frameProgressbar = Frame(root)
progressbar = ttk.Progressbar(frameProgressbar, orient='horizontal', length=500)
progressbar.pack()

#sesta riga, bottone elabora 
frameElabora = Frame(root)
frameElabora_button = Button(frameElabora, text="Elabora", command=elabora)
frameElabora_button.pack()


#prima riga, aggancio frame titolo
frameTitolo.grid(column=0, row=0, columnspan=3)

#seconda riga, aggancio frame cartella input
frameInput_titolo.grid(column=0, row=1)
frameInput_field.grid(column =1, row=1)
frameInput_button.grid(column=2, row=1)

#terza riga, aggancio frame cartella out
frameOutput_titolo.grid(column=0, row=2)
frameOutput_field.grid(column =1, row=2)
frameOutput_button.grid(column=2, row=2)

#terza riga, aggancio frame file comuni
frameFileComuni_titolo.grid(column=0, row=3)
frameFileComuni_field.grid(column =1, row=3)
frameFileComuni_button.grid(column=2, row=3)

#quarta riga, aggancio frame progressbar
frameProgressbar.grid(column=0, row=4, columnspan=3)

#quinta riga, aggiocio frame bottone elabora
frameElabora.grid(column=0, row=5, columnspan=3)

root.mainloop()