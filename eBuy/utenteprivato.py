from datetime import *
from mytypes_eBuy import Popolarità
from mytypes_eBuy import RealZO
from utente import Utente

class UtentePrivato(Utente):

    def __init__(self, username:str, registrazione:datetime):
        super().__init__(username, registrazione)