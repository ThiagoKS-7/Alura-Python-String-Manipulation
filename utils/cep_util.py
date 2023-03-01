import re

class CepFinder:
    def __init__(self, endereco:str):
        self.endereco = endereco
    def __str__(self) -> str:
        return re.search("[0-9]{5}(?:-[0-9]{3})",self.endereco).group()
