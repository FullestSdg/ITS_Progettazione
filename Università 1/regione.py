class Regione:

    _nome:str # noto alla nascita {univoco}

    def __init__(self, nome:str):
        self._nome = nome

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome