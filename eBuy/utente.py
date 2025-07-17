from datetime import *
from mytypes_eBuy import Popolarità
from mytypes_eBuy import RealZO

class Utente:

    _username:str # noto alla nascita <<immutable>> <<unique>> 
    _registrazione:datetime # noto alla nascita <<immutable>> 

    def __init__(self, username:str, registrazione:datetime) -> None:
        self._username = username 
        self._registrazione = registrazione 

    def getUsername(self) -> str: 
        return self._username

    def getRegistrazione(self) -> datetime: 
        return self._registrazione

    def popolarità(self, i:datetime) -> Popolarità:
        pass 

    def affidabilità(self, i:datetime) -> RealZO:
        pass
