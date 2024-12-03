import decimal
from datetime import datetime
from Source import SourceRow
from Comune import ComuneRow as cr
from dateutil.parser import parse
import re 

class VerbaleRow:
    tipo:str
    protocollo:str
    annoDebito:int
    codTipoAtto:str
    dataAtto:str 
    dataNotificaAtto:str
    estremiAtto:str
    motivazioneAtto:str
    canale:str
    soggetto1_CodiceFiscale:str 
    soggetto1_Cognome:str 
    soggetto1_Nome:str  
    soggetto1_IndirizzoCodiceBelfiore:str 
    soggetto1_Indirizzo:str 
    soggetto1_IndirizzoNumero:str 
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
        
        personaFisica:bool = False
        personaGiuridica:bool = False
        
        self.tipo = row.tipo
        self.protocollo = row.verbale_id
        self.annoDebito = row.verbale_id[-4:] 
        self.codTipoAtto = "VE"


        cf = row.codiceFiscale

        cfTest = re.search("^[A-Z]{6}\\d{2}[A-Z]\\d{2}[A-Z]\\d{3}[A-Z]$", cf)

        if cfTest:
            personaFisica = True
        else: 
            cfTest = self.controllaPIVA(cf)
            if cfTest:
                personaGiuridica = True
            else:
                raise ValueError(f"verbale:'{self.protocollo}', il codice fiscale '{cf}' non si riferisce ne ad una persona fisica, se ad una giuridica")

              
        
        if(isinstance(row.dataNotifica, datetime)==False):
            dt =  parse(row.dataNotifica)
        else: 
            dt =  row.dataNotifica
        
        self.dataAtto =  dt.strftime("%Y%m%d")
        self.dataNotificaAtto = dt.strftime("%Y%m%d")
        
        if "-" in row.residenza:
            temp = row.residenza.split("-")
            tempIndirizzoNumero = temp[0].lstrip().rstrip();
            tempCapCitta = temp[1].lstrip().rstrip()
            indirizzo = tempIndirizzoNumero[:-2].lstrip().rstrip()
            numero = tempIndirizzoNumero[-2:].lstrip().rstrip()
            cap = tempCapCitta[:5]
            comune = tempCapCitta[5:]
        else:
            tempIndirizzoNumero = ""
            tempCapCitta = ""
            indirizzo = ""
            numero = ""
            cap = ""
            comune = ""
        
        try:
            cercaComuneNascita = row.comuneNascita.upper().strip()          
            setNascita : set = comuni[cercaComuneNascita]
            if len(setNascita) <= 0:
                raise ValueError(f"verbale:'{self.protocollo}', il comune di nascita {cercaComuneNascita} non è stato trovato nel file dei comuni")  
            
        except Exception as ex:
            raise ValueError(f"verbale:'{self.protocollo}', il comune di nascita {cercaComuneNascita} non è stato trovato nel file dei comuni") 
        
        datiNascita = cr(setNascita)

        try:
            cercaComune = comune.upper().strip()  
            setResidenza : set = comuni[cercaComune]
            if len(setResidenza) <= 0:
                raise ValueError(f"verbale:'{self.protocollo}', il comune di residenza {cercaComune} non è stato trovato nel file dei comuni")  
            
        except Exception as ex:
            raise ValueError(f"verbale:'{self.protocollo}', il comune di residenza {cercaComune} non è stato trovato nel file dei comuni") 

        datiResidenza = cr(setResidenza)


        self.estremiAtto = "VERBALE"
        self.motivazioneAtto = "ANZIONE RELATIVA AL VERBALE NR. " + row.verbale_id +" NOTIFICATO IL " + row.dataNotifica;
        self.canale = "CC-RMMESSI"
        
        self.soggetto1_CodiceFiscale = row.codiceFiscale
        self.soggetto1_Cognome = row.cognome
        
        if personaFisica:
            if(isinstance(row.dataNascita, datetime)==False):
                dt =  parse(row.dataNascita)
            else: 
                dt =  row.dataNascita
        
            self.soggetto1_Nome = row.nome
            self.soggetto1_NascitaData = dt.strftime("%Y%m%d")
            self.soggetto1_NascitaComune = datiNascita.comune
            self.soggetto1_NascitaSiglaProvincia = datiNascita.provincia
            self.soggetto1_Natura = "1"
            self.soggetto1_Sesso = row.sesso
            self.soggetto2_Nome = row.nome
            self.soggetto2_NascitaData = dt.strftime("%Y%m%d")
            self.soggetto2_NascitaComune = datiNascita.comune
            self.soggetto2_NascitaSiglaProvincia = datiNascita.provincia
            self.soggetto2_Natura = "1"
            self.soggetto2_Sesso = row.sesso
        else: 
            if personaGiuridica :
                self.soggetto1_Nome = ""
                self.soggetto1_NascitaData = ""
                self.soggetto1_NascitaComune = ""
                self.soggetto1_NascitaSiglaProvincia = ""
                self.soggetto1_Natura = "2"
                self.soggetto1_Sesso = ""
                self.soggetto2_Nome = ""
                self.soggetto2_NascitaData = ""
                self.soggetto2_NascitaComune = ""
                self.soggetto2_NascitaSiglaProvincia = ""
                self.soggetto2_Natura = "2"
                self.soggetto2_Sesso = ""

        self.soggetto1_IndirizzoCodiceBelfiore = datiResidenza.codice
        self.soggetto1_Indirizzo = indirizzo
        self.soggetto1_IndirizzoNumero = numero
        self.soggetto1_IndirizzoCAP = cap
        self.soggetto1_IndirizzoComune = comune
        self.soggetto1_IndirizzoSiglaProvincia = datiResidenza.provincia
        self.soggetto1_NascitaCodiceBelfiore = datiNascita.codice

       
       

        self.soggetto2_CodiceFiscale = row.codiceFiscale
        self.soggetto2_Cognome = row.cognome
       
        self.soggetto2_IndirizzoCodiceBelfiore = datiResidenza.codice
        self.soggetto2_Indirizzo = indirizzo
        self.soggetto2_IndirizzoNumero = numero
        self.soggetto2_IndirizzoCAP = cap
        self.soggetto2_IndirizzoComune = comune
        self.soggetto2_IndirizzoSiglaProvincia = datiResidenza.provincia
        self.soggetto2_NascitaCodiceBelfiore = datiNascita.codice
        

        self.tributo1_codice = "1D80"
        self.tributo1_totale = row.importoSanzioniRuolo
        self.tributo2_codice = "1F03"
        self.tributo2_totale = row.importoSpese
        self.tributo3_codice = ""
        self.tributo3_totale = ""

    def controllaPIVA(self, partita_iva:str):
        IVA_REGEXP = "^[0-9]{11}$"
        ORD_ZERO = ord('0')

        if 0 == len(partita_iva):
            return False
        if 11 != len(partita_iva):
            return False
        match = re.match(IVA_REGEXP, partita_iva)
        if not match:
            return False
        
        s = 0
        for i in range(0, 10, 2):
            s += ord(partita_iva[i]) - ORD_ZERO
        for i in range(1, 10, 2):
            c = 2 * (ord(partita_iva[i]) - ORD_ZERO)
            if c > 9:
                c -= 9
            s += c

        if (10 - s%10)%10 != ord(partita_iva[10]) - ORD_ZERO:
            return False
        
        return True

    def out(self):
         
        verbale = {
                "Protocollo":self.protocollo,
                "AnnoDebito":self.annoDebito,
                "CodTipoAtto":self.codTipoAtto,
                "DataAtto":self.dataAtto,
                "DataNotificaAtto":self.dataNotificaAtto,
                "EstremiAtto":self.estremiAtto,
                "MotivazioneAtto": self.motivazioneAtto,
                "DescrizioneAtto":"",
                "Canale":self.canale,
            
                "Soggetto1_CodiceFiscale":self.soggetto1_CodiceFiscale,
                "Soggetto1_Cognome":self.soggetto1_Cognome,
                "Soggetto1_Nome": self.soggetto1_Nome,
                "Soggetto1_IndirizzoCodiceBelfiore":self.soggetto1_IndirizzoCodiceBelfiore,
                "Soggetto1_Indirizzo":self.soggetto1_Indirizzo,
                "Soggetto1_IndirizzoNumero": self.soggetto1_IndirizzoNumero,
                "Soggetto1_IndirizzoComplementi":"",
                "Soggetto1_IndirizzoLocalita":"",
                "Soggetto1_IndirizzoCAP": self.soggetto1_IndirizzoCAP,
                "Soggetto1_IndirizzoComune": self.soggetto1_IndirizzoComune,
                "Soggetto1_IndirizzoSiglaProvincia": self.soggetto1_IndirizzoSiglaProvincia,
                "Soggetto1_NascitaCodiceBelfiore": self.soggetto1_NascitaCodiceBelfiore,
                "Soggetto1_NascitaData": self.soggetto1_NascitaData,
                "Soggetto1_NascitaComune": self.soggetto1_NascitaComune,
                "Soggetto1_NascitaSiglaProvincia": self.soggetto1_NascitaSiglaProvincia,
                "Soggetto1_Natura": self.soggetto1_Natura,
                "Soggetto1_Sesso": self.soggetto1_Sesso,

                "Soggetto2_CodiceFiscale":self.soggetto2_CodiceFiscale,
                "Soggetto2_Cognome":self.soggetto2_Cognome,
                "Soggetto2_Nome": self.soggetto2_Nome,
                "Soggetto2_IndirizzoCodiceBelfiore":self.soggetto2_IndirizzoCodiceBelfiore,
                "Soggetto2_Indirizzo":self.soggetto2_Indirizzo,
                "Soggetto2_IndirizzoNumero": self.soggetto2_IndirizzoNumero,
                "Soggetto2_IndirizzoComplementi":"",
                "Soggetto2_IndirizzoLocalita":"",
                "Soggetto2_IndirizzoCAP": self.soggetto2_IndirizzoCAP,
                "Soggetto2_IndirizzoComune": self.soggetto2_IndirizzoComune,
                "Soggetto2_IndirizzoSiglaProvincia": self.soggetto2_IndirizzoSiglaProvincia,
                "Soggetto2_NascitaCodiceBelfiore": self.soggetto2_NascitaCodiceBelfiore,
                "Soggetto2_NascitaData": self.soggetto2_NascitaData,
                "Soggetto2_NascitaComune": self.soggetto2_NascitaComune,
                "Soggetto2_NascitaSiglaProvincia": self.soggetto2_NascitaSiglaProvincia,
                "Soggetto2_Natura": self.soggetto2_Natura,
                "Soggetto2_Sesso": self.soggetto2_Sesso,

                "Tributo1_Codice":self.tributo1_codice,
                "Tributo1_Totale": self.tributo1_totale,
                "Tributo2_Codice": self.tributo2_codice,
                "Tributo2_Totale": self.tributo2_totale,
                "Tributo3_Codice": "",
                "Tributo3_Totale": ""
            }
        return verbale


    
 
    
        

    
        