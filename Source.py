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
        self.tipo        =   str(row["tipo"]).upper()
        self.verbale_id  =   row["verbale_id"]
        self.cognome     =   row["cognome"] 
        self.nome        =   row["nome"] 
        self.sesso       =   row["sesso"]
       # self.dataNascita =  row["data_nascita"]
        self.dataNascita =  row["data_nascita"]
        self.comuneNascita =   str(row["comune_nascita"]).upper()
        self.statoNascita =   row["stato_nascita"]   
        self.codiceFiscale = row["codice_fiscale"]
        self.residenza = row["residenza"]
        self.dataViolazione = row["data_violazione"]
        self.targa = row["targa"]
        self.dataNotifica = row["data_notifica"]
        self.annoRiferimento = row["anno_riferimento"]
        self.importoSanzioniRuolo = row["importo_sanzioni_ruolo"]
        self.importoSpese = row["importo_spese"]
