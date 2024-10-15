import pandas as pd
 

#1.  LETTURA EVENTUALE FILE DI CONFIGURAZIONE
#2.  VERIFICA DELLA CARTELLA DI INPUT
#3.  INIZIO SCANSIONE CARTELLA INPUT
#3.1 Lettura file excel
#3.2 Estrazione dati
#3.3 Classificazione dati
#3.4 Copia su nuovo file
 

df = pd.read_excel("/Users/peppe/App/Python/Verbali/RUOLI_PROVA.xlsx")

verbali = {}

for index,row in df.iterrows():
    verbale = {
        "Protocollo":row["verbale_id"],
        "AnnoDebito":"TO DO",
        "CodTipoAtto":"TO DO",
        "DataAtto":"TO DO",
        "DataNotificaAtto":"TO DO",
        "EstremiAtto":"TO DO",
        "Canale":"TO DO",
       
        "Soggetto1_CodiceFiscale":row["codice_fiscale"],
        "Soggetto1_Cognome":row["cognome"],
        "Soggetto1_Nome":row["nome"],
        "Soggetto1_IndirizzoCodiceBelfiore":"TO DO",
        "Soggetto1_Indirizzo":"TO DO",
        "Soggetto1_IndirizzoNumero":"TO DO",
        "Soggetto1_IndirizzoCAP":"TO DO",
        "Soggetto1_IndirizzoComune":"TO DO",
        "Soggetto1_IndirizzoSiglaProvincia":"TO DO",
        "Soggetto1_NascitaCodiceBelfiore":"TO DO",
        "Soggetto1_NascitaData":"TO DO",
        "Soggetto1_NascitaComune":row["comune_mascita"],
        "Soggetto1_NascitaSiglaProvincia":"TO DO",
        "Soggetto1_Natura":"TO DO",
        "Soggetto1_Sesso":row["sesso"],

        "Soggetto2_CodiceFiscale":row["codice_fiscale"],
        "Soggetto2_Cognome":row["cognome"],
        "Soggetto2_Nome":row["nome"],
        "Soggetto2_IndirizzoCodiceBelfiore":"TO DO",
        "Soggetto2_Indirizzo":"TO DO",
        "Soggetto2_IndirizzoNumero":"TO DO",
        "Soggetto2_IndirizzoCAP":"TO DO",
        "Soggetto2_IndirizzoComune":"TO DO",
        "Soggetto2_IndirizzoSiglaProvincia":"TO DO",
        "Soggetto2_NascitaCodiceBelfiore":"TO DO",
        "Soggetto2_NascitaData":"TO DO",
        "Soggetto2_NascitaComune":row["comune_mascita"],
        "Soggetto2_NascitaSiglaProvincia":"TO DO",
        "Soggetto2_Natura":"TO DO",
        "Soggetto2_Sesso":row["sesso"],

        "Tributo1_Codice":"TO DO",
        "Trributo1_Totale":"TO DO",
        "Tributo2_Codice":"TO DO"
        
        
    }
    if verbale["Protocollo"] not in verbali.keys():
        verbali[verbale["Protocollo"]] = verbale
    else:
        verbali[verbale["Protocollo"]]["Soggetto2_CodiceFiscale"] = row["codice_fiscale"],
        verbali[verbale["Protocollo"]]["Soggetto2_Cognome"] = row["cognome"]
        verbali[verbale["Protocollo"]]["Soggetto2_Nome"] = row["nome"]
        verbali[verbale["Protocollo"]]["Soggetto2_IndirizzoCodiceBelfiore"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_Indirizzo"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_IndirizzoNumero"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_IndirizzoCAP"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_IndirizzoComune"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_IndirizzoSiglaProvincia"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_NascitaCodiceBelfiore"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_NascitaData"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_NascitaComune"] = row["comune_mascita"]
        verbali[verbale["Protocollo"]]["Soggetto2_NascitaSiglaProvincia"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_Natura"] = "TO DO"
        verbali[verbale["Protocollo"]]["Soggetto2_Sesso"] = row["sesso"]


verbaList = []

for key in verbali:
    verbaList.append(verbali[key])

df2 = pd.DataFrame(verbaList, columns=['Protocollo','Soggetto1_Cognome', 'Soggetto2_Cognome'])

print(df2)
 