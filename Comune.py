class ComuneRow:
    comune:str
    provincia:str
    codice:str

    def __init__(self, rowSource : set):
        self.comune     = rowSource["Comune"]
        self.provincia  = rowSource["Provincia"]
        self.codice     = rowSource["CodFisco"] 
