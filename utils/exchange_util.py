PRICE = 5.50

class Exchange:
    def __init__(self, origin, destination, calc:any) -> None:
        self.origin = origin
        self.destination = destination
        self.calc = calc
        self.accepted = ["BRL", "USD"]
        
    def __str__(self) -> any:
        return f"{str(round(self.calc,2))} {self.destination}"  if self.currency_is_accepted() else "0"
        
    def currency_is_accepted(self) -> bool:
        return self.origin in self.accepted and self.destination in self.accepted
        

class ExchangeBrlUsd(Exchange):
    def __init__(self, val:any) -> None:
        super().__init__("BRL", "USD", val/PRICE)

class ExchangeUsdBrl(Exchange):
    def __init__(self, val:any) -> None:
        super().__init__("USD", "BRL", val*PRICE)
