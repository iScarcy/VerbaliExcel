import decimal
from datetime import datetime
from Source import SourceRow
from Comune import ComuneRow as cr

class VerbaleRow:
    protocollo:str
    annoDebito:int
    codTipoAtto:str
    dataAtto:str 
    dataNotificaAtto:str
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
 
    

    def __init__(self, row : SourceRow, comuni: dict):
        self.protocollo = row.verbale_id
        self.annoDebito = row.verbale_id[-4:] 
        self.codTipoAtto = "VE"
        
        date_format = "%d/%m/%Y"
        date_formatEN = "%Y/%m/%d"
        
        try:
            date_object = datetime.strptime(row.dataNotifica, date_format)
        except:
            date_object = datetime.strptime(row.dataNotifica, date_formatEN)
        
        try:
            dateNascita_object = datetime.strptime(row.dataNascita, date_format)
        except:
            dateNascita_object = datetime.strptime(row.dataNascita, date_formatEN)

       
        self.dataAtto =  date_object.strftime("%Y%m%d")
        self.dataNotificaAtto = date_object.strftime("%Y%m%d")
        
        temp = row.residenza.split("-")
        tempIndirizzoNumero = temp[0].lstrip().rstrip();
        tempCapCitta = temp[1].lstrip().rstrip().split(" ")
        indirizzo = tempIndirizzoNumero[:-2].lstrip().rstrip()
        numero = tempIndirizzoNumero[-2:].lstrip().rstrip()
        cap = tempCapCitta[0].lstrip().rstrip()
        comune = tempCapCitta[1].lstrip().rstrip()
          
        setNascita : set = comuni[row.comuneNascita]
        datiNascita = cr(setNascita)

        setResidenza : set = comuni[comune]
        datiResidenza = cr(setResidenza)


        self.estremiAtto = "VERBALE"
        self.motivazioneAtto = "ANZIONE RELATIVA AL VERBALE NR. " + row.verbale_id +" NOTIFICATO IL " + row.dataNotifica;
        self.canale = "CC-RMMESSI"
        
        self.soggetto1_CodiceFiscale = row.codiceFiscale
        self.soggetto1_Cognome = row.cognome
        self.soggetto1_Nome = row.nome; 
        self.soggetto1_IndirizzoCodiceBelfiore = datiResidenza.codice
        self.soggetto1_Indirizzo = indirizzo
        self.soggetto1_IndirizzoNumero = numero
        self.soggetto1_IndirizzoCAP = cap
        self.soggetto1_IndirizzoComune = comune
        self.soggetto1_IndirizzoSiglaProvincia = datiResidenza.provincia
        self.soggetto1_NascitaCodiceBelfiore = datiNascita.codice

       
        self.soggetto1_NascitaData = dateNascita_object.strftime("%Y%m%d")
        self.soggetto1_NascitaComune = datiNascita.comune
        self.soggetto1_NascitaSiglaProvincia = datiNascita.provincia;
        self.soggetto1_Natura = "1";
        self.soggetto1_Sesso = row.sesso;

        self.soggetto2_CodiceFiscale = row.codiceFiscale
        self.soggetto2_Cognome = row.cognome
        self.soggetto2_Nome = row.nome; 
        self.soggetto2_IndirizzoCodiceBelfiore = datiResidenza.codice
        self.soggetto2_Indirizzo = indirizzo
        self.soggetto2_IndirizzoNumero = numero
        self.soggetto_IndirizzoCAP = cap
        self.soggetto2_IndirizzoComune = comune
        self.soggetto2_IndirizzoSiglaProvincia = datiResidenza.provincia
        self.soggetto2_NascitaCodiceBelfiore = datiNascita.codice
        self.soggetto2_NascitaData = dateNascita_object.strftime("%Y%m%d")
        self.soggetto2_NascitaComune = datiNascita.comune
        self.soggetto2_NascitaSiglaProvincia = datiNascita.provincia;
        self.soggetto2_Natura = "1";
        self.soggetto2_Sesso = row.sesso;

        self.Tributo1_Codice = "1D80";
        self.Trributo1_Totale = row.importoSanzioniRuolo;
        self.Tributo2_Codice = "1F03";

    
 
    
        

    
        