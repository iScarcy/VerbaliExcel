class VerbaleRow:
    tipo = ""
    verbale_id = ""
    cognome = ""

    def __init__(self, rowSource : set):
        self.read_data(row=rowSource)

    def read_data(self,row:set):
        self.tipo       =   row["tipo"]
        self.verbale_id =   row["verbale_id"]
        self.cognome    =   row["cognome"] 