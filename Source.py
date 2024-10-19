import datetime
import decimal

class SourceRow:
    
    tipo : str
    verbale_id : str
    cognome : str
    nome : str
    sesso : str
    dataNascita : datetime
    comuneNascita : str
    statoNascita : str
    codiceFiscale : str
    residenza : str
    dataViolazione : str
    targa : str
    dataNotifica : str
    annoRiferimento : str
    importoSanzioniRuolo : decimal
    importoSpese : decimal

    def __init__(self, rowSource : set):
        self.read_data(row=rowSource)

    def read_data(self,row:set):
        self.tipo        =   row["tipo"]
        self.verbale_id  =   row["verbale_id"]
        self.cognome     =   row["cognome"] 
        self.nome        =   row["nome"] 
        self.sesso       =   row["sesso"]
       # self.dataNascita =  row["data_nascita"]
        self.dataNascita =  str(row["data_nascita"]).replace("-","/").replace("00:00:00","").strip()  
        self.comuneNascita =   row["comune_nascita"] 
        self.statoNascita =   row["stato_nascita"]   
        self.codiceFiscale = row["codice_fiscale"]
        self.residenza = row["residenza"]
        self.dataViolazione = str(row["data_violazione"]).replace("-","/").replace("00:00:00","").strip()
        self.targa = row["targa"]
        self.dataNotifica = str(row["data_notifica"]).replace("-","/").replace("00:00:00","").strip()
        self.annoRiferimento = row["anno_riferimento"]
        self.importoSanzioniRuolo = row["importo_sanzioni_ruolo"]
        self.importoSpese = row["importo_spese"]
