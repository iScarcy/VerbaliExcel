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
      #  self.dataAtto = row.dataNotifica. dataNotifica.ToString("yyyyMMdd"));
       # self.dataNotificaAtto = int.Parse(dataNotifica.ToString("yyyyMMdd"));
       # self.estremiAtto = estremiAtto;
       # self.motivazioneAtto = string.Format(motivazioneAtto, row.verbale_id, row.data_notifica);
       # self.canale = canale;
        
        self.Soggetto1_CodiceFiscale = row.codiceFiscale;
        self.Soggetto1_Cognome = row.cognome;
        self.Soggetto1_Nome = row.nome; 

        temp = row.residenza.split("-")
        tempIndirizzoNumero = temp[0].lstrip().rstrip();
        tempCapCitta = temp[1].lstrip().rstrip().split(" ")
        indirizzo = tempIndirizzoNumero[:-2].lstrip().rstrip()
        numero = tempIndirizzoNumero[-2:].lstrip().rstrip()
        cap = tempCapCitta[0].lstrip().rstrip()
        comune = tempCapCitta[1].lstrip().rstrip()
        #self.Soggetto1_IndirizzoCodiceBelfiore = indirizzoCodiceBelfiore; 
        #self.Soggetto1_Indirizzo = indirizzo;
        #self.Soggetto1_IndirizzoNumero = indirizzoNumero;
        #self.Soggetto1_IndirizzoCAP = cap;
        #self.Soggetto1_IndirizzoComune = comune;
        #self.Soggetto1_IndirizzoSiglaProvincia = indirizzoSiglaProvincia;
        #self.Soggetto1_NascitaCodiceBelfiore = nascitaCodiceBelfiore; 
        #self.Soggetto1_NascitaData = int.Parse(dataNascita.ToString("yyyyMMdd"));
        #self.Soggetto1_NascitaComune = row.comune_nascita;
        #self.Soggetto1_NascitaSiglaProvincia = nascitaSiglaProvincia;
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
        

    
        