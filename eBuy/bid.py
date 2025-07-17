from datetime import * 

class Bid:

    _istante:datetime # noto alla nascita <<immutable>> <<unique>> 

    def __init__(self, istante:datetime) -> None: 
        self._istante = istante 

    def getIstante(self) -> datetime: 
        return self._istante