import time
from tkinter import ttk
import pandas as pd
import os
from Verbale import VerbaleRow as vb
from Source import SourceRow as sr
from Comune import ComuneRow as cr
import json

def elabora(inputPath : str,outputPath : str, fileComuni : str, pb : ttk.Progressbar):
   
    verbali = {}

    dfc = pd.read_excel(fileComuni)

    codiciComuni = {}

    for index, row in dfc.iterrows():
        com = cr(row) 
        codiciComuni[com.comune] = {
                "Comune":com.comune,
                "Provincia":com.provincia,
                "CodFisco":com.codice
            }



    files = os.listdir(inputPath) 
    num_file : int = len(files) 
    increment = 100 // num_file
    if increment > 0:
        pb.pack()
        for filename in files:
            if filename.endswith(".xlsx") or filename.endswith(".xls"): 
                 
                df = pd.read_excel(inputPath + "/" + filename)
                for index,row in df.iterrows():
                    source = sr(row)
                    verbale = vb(source,codiciComuni)

                    if verbale.protocollo not in verbali.keys():
                        verbali[verbale.protocollo] = verbale
                    else:
                        verbale2 : vb = verbali[verbale.protocollo]
                        verbale2.soggetto2_CodiceFiscale = verbale.soggetto1_CodiceFiscale
                        verbale2.soggetto2_Cognome = verbale.soggetto1_Cognome
                        verbale2.soggetto2_Nome = verbale.soggetto1_Nome
                        verbale2.soggetto2_IndirizzoCodiceBelfiore = verbale.soggetto1_IndirizzoCodiceBelfiore
                        verbale2.soggetto2_Indirizzo = verbale.soggetto1_Indirizzo
                        verbale2.soggetto2_IndirizzoNumero = verbale.soggetto1_IndirizzoNumero
                        verbale2.soggetto2_IndirizzoCAP = verbale.soggetto1_IndirizzoCAP
                        verbale2.soggetto2_IndirizzoComune = verbale.soggetto1_IndirizzoComune
                        verbale2.soggetto2_IndirizzoSiglaProvincia = verbale.soggetto1_IndirizzoSiglaProvincia
                        verbale2.soggetto2_NascitaCodiceBelfiore = verbale.soggetto1_NascitaCodiceBelfiore
                        verbale2.soggetto2_NascitaData = verbale.soggetto1_NascitaData
                        verbale2.soggetto2_NascitaComune = verbale.soggetto1_NascitaComune
                        verbale2.soggetto2_NascitaSiglaProvincia = verbale.soggetto1_NascitaSiglaProvincia
                        verbale2.soggetto2_Natura = verbale.soggetto1_Natura
                        verbale2.soggetto2_Sesso = verbale.soggetto1_Sesso
                        verbali[verbale2.protocollo] = verbale2

                pb["value"] += increment 
                continue
            else:
                continue
       
        verbaList = []
        for key in verbali:
            x = verbali[key].out()
            verbaList.append(x)
       
        df2 = pd.DataFrame(verbaList)
        df2.to_excel(outputPath + "/" + filename, index=False)
    
    pb.stop    
    