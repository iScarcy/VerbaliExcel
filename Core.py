import time
from tkinter import ttk
import os

def elabora(inputPath : str,outputPath : str, fileComuni : str, pb : ttk.Progressbar):
   
    num_file = os.listdir(inputPath).count
    i = 1
    for filename in os.listdir(inputPath):
        if filename.endswith(".xlsx") or filename.endswith(".xls"): 
            print(filename)
            pb["value"] += (num_file/1)   
            continue
        else:
             continue

    

    pb.stop    
    