from mytypes_eBuy import * 
from datetime import *
from utente import Utente
from bid import Bid


class Asta:

    _prezzo_bid:RealGZ # noto alla nascita 
    _scadenza:datetime # noto alla nascita

    def __init__(self, preddo_bid:RealGZ, scadenza:datetime) -> None:
        pass 

    def setPrezzo_bid(self, prezzo_bid:RealGZ) -> None: 
        pass 

    def getPrezzo_bid(self) -> RealGZ: 
        pass 

    def setScadenza(self, scadenza:datetime) -> None: 
        pass 

    def getScadenza(self) -> datetime:
        pass 

    def prezzo(self, i:datetime) -> RealGEZ:
        pass 

    def vincitore(self) -> Utente | None: 
        pass 

    def ultimo_bid(self, i:datetime)