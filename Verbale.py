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
        self.annoDebito = row.verbale_id[-4:] #TODO PRENDERE GLI ULTRIMI 4 CARATTERI
        self.codTipoAtto = "VE"
        
        date_format = "%d/%m/%Y"
        # Attempt to convert string to datetime
          
        date_object = datetime.strptime(row.dataNotifica, date_format)
        dateNascita_object = datetime.strptime(row.dataNascita, date_format)

        self.dataAtto = date_object.strftime('%Y%m%d'); # dataNotifica.ToString("yyyyMMdd"));
        self.dataNotificaAtto = date_object.strftime('%Y%m%d')

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
        
        self.Soggetto1_CodiceFiscale = row.codiceFiscale
        self.Soggetto1_Cognome = row.cognome
        self.Soggetto1_Nome = row.nome; 

      
        self.Soggetto1_IndirizzoCodiceBelfiore = datiResidenza.codice
        self.Soggetto1_Indirizzo = indirizzo
        self.Soggetto1_IndirizzoNumero = numero
        self.Soggetto1_IndirizzoCAP = cap
        self.Soggetto1_IndirizzoComune = comune
        self.Soggetto1_IndirizzoSiglaProvincia = datiResidenza.provincia
        self.Soggetto1_NascitaCodiceBelfiore = datiNascita.codice
        self.Soggetto1_NascitaData = dateNascita_object.strftime('%Y%m%d')
        self.Soggetto1_NascitaComune = datiNascita.comune
        self.Soggetto1_NascitaSiglaProvincia = datiNascita.provincia;
        self.Soggetto1_Natura = "1";
        self.Soggetto1_Sesso = row.sesso;

        self.Soggetto2_CodiceFiscale = row.codiceFiscale;
        self.Soggetto2_Cognome = row.cognome;
        self.Soggetto2_Nome = row.nome; 

        #self.Soggetto2_IndirizzoCodiceBelfiore = indirizzoCodiceBelfiore; 
        #self.Soggetto2_Indirizzo = indirizzo;
        #self.Soggetto2_IndirizzoNumero = indirizzoNumero;
        #self.Soggetto2_IndirizzoCAP = cap;
        #self.Soggetto2_IndirizzoComune = comune;
        #self.Soggetto2_IndirizzoSiglaProvincia = indirizzoSiglaProvincia;
        #self.Soggetto2_NascitaCodiceBelfiore = nascitaCodiceBelfiore; 
        #self.Soggetto2_NascitaData = int.Parse(dataNascita.ToString("yyyyMMdd"));
        #self.Soggetto2_NascitaComune = row.comune_nascita;
        #self.Soggetto2_NascitaSiglaProvincia = nascitaSiglaProvincia;
        self.Soggetto2_Natura = "1";
        self.Soggetto2_Sesso = row.sesso;
        #self.Tributo1_Codice = tributo1_Codice;
        #self.Trributo1_Totale = Double.Parse(row.importo_sanzioni_ruolo);
        #self.Tributo2_Codice = tributo2_Codice;
    
 
    
        

    
        