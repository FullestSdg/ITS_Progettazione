from mytypes_eBuy import * 
from datetime import *
from utente import Utente
from bid import Bid


class Asta:

    _prezzo_bid:RealGZ # noto alla nascita 
    _scadenza:datetime # noto alla nascita

    def __init__(self, prezzo_bid:RealGZ, scadenza:datetime) -> None:
        
        self._prezzo_bid = self.setPrezzo_bid(prezzo_bid)
        self._scadenza = self.setScadenza(scadenza)

    def setPrezzo_bid(self, prezzo_bid:RealGZ) -> None: 
        self.prezzo_bid = prezzo_bid

    def getPrezzo_bid(self) -> RealGZ: 
        return self.prezzo_bid

    def setScadenza(self, scadenza:datetime) -> None: 
        self._scadenza = scadenza

    def getScadenza(self) -> datetime:
        return self._scadenza

    def prezzo(self, i:datetime) -> RealGEZ:
        pass  

    def vincitore(self) -> Utente | None: 
        pass 

    def ultimo_bid(self, i:datetime) -> Bid | None:
        pass 

    def finita(self) -> bool: 
        pass 