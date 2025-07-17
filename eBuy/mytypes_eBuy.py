from typing import Self

class Popolarità:
    pass 

class RealGEZ(float):

    def __new__(cls, number:float| int | bool | str | Self) -> Self:

        if number >= 0 and number <= 1:
        
            return number
        
        else:
            raise ValueError(f"Il numero inserito {number} deve essere compreso tra 0 e 1 (estremi inclusi) ed un reale")

class RealGEZ(float):

    def __new__(cls, number:float| int | bool | str | Self) -> Self:

        if number > 0:
        
            return number
        
        else:
            raise ValueError(f"Il numero inserito {number} deve essere maggiore di 0 e un reale")

class RealGEZ(float):

    def __new__(cls, number:float| int | bool | str | Self) -> Self:

        if number >= 0:
        
            return number
        
        else:
            raise ValueError(f"Il numero inserito {number} deve essere maggiore/uguale di 0 e un reale")