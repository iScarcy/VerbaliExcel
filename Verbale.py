import decimal
from Source import SourceRow

class VerbaleRow:
    protocollo:str
    annoDebito:int
    codTipoAtto:str
    dataAtto:int 
    dataNotificaAtto:int
    estremiAtto:str
    motivazioneAtto:str
    descrizioneAtto:str
    canale:str
    soggetto1_CodiceFiscale:str 
    soggetto1_Cognome:str 
    soggetto1_Nome:str  
    soggetto1_IndirizzoCodiceBelfiore:str 
    soggetto1_Indirizzo:str 
    soggetto1_IndirizzoNumero:str 
    soggetto1_IndirizzoComplementi:str 
    soggetto1_IndirizzoLocalita:str 
    soggetto1_IndirizzoCAP:str  
    soggetto1_IndirizzoComune:str  
    soggetto1_IndirizzoSiglaProvincia:str  
    soggetto1_NascitaCodiceBelfiore:str  
    soggetto1_NascitaData:int  
    soggetto1_NascitaComune:str  
    soggetto1_NascitaSiglaProvincia:str  
    soggetto1_Natura:str  
    soggetto1_Sesso:str  

    soggetto2_CodiceFiscale:str 
    soggetto2_Cognome:str 
    soggetto2_Nome:str  
    soggetto2_IndirizzoCodiceBelfiore:str 
    soggetto2_Indirizzo:str 
    soggetto2_IndirizzoNumero:str 
    soggetto2_IndirizzoComplementi:str 
    soggetto2_IndirizzoLocalita:str 
    soggetto2_IndirizzoCAP:str  
    soggetto2_IndirizzoComune:str  
    soggetto2_IndirizzoSiglaProvincia:str  
    soggetto2_NascitaCodiceBelfiore:str  
    soggetto2_NascitaData:int  
    soggetto2_NascitaComune:str  
    soggetto2_NascitaSiglaProvincia:str  
    soggetto2_Natura:str  
    soggetto2_Sesso:str  
    tributo1_codice:str
    tributo1_totale:decimal
    tributo2_codice:str
    tributo2_totale:decimal
    tributo3_codice:str
    tributo3_totale:decimal
 

    def __init__(self, row : SourceRow):
        self.protocollo = row.verbale_id
        self.annoDebito = row.verbale_id #TODO PRENDERE GLI ULTRIMI 4 CARATTERI
        self.codTipoAtto = "VE"
        

    
        