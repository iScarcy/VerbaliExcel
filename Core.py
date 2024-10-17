import time
from tkinter import ttk
import pandas as pd
import os
from Verbale import VerbaleRow as vb
from Source import SourceRow as sr
def elabora(inputPath : str,outputPath : str, fileComuni : str, pb : ttk.Progressbar):
   
    files = os.listdir(inputPath) 
    num_file : int = len(files) 
    increment = 100 // num_file
    if increment > 0:
        pb.pack()
        for filename in files:
            if filename.endswith(".xlsx") or filename.endswith(".xls"): 
                print(filename)
                df = pd.read_excel(inputPath + "/" + filename)
                for index,row in df.iterrows():
                    source = sr(row)
                    verbale = vb(source)
                     
                pb["value"] += increment 
                continue
            else:
                continue

    

    pb.stop    
    