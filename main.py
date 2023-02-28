
class QueryToDict:
    def __init__(self, url):
        self.url = url
        self.param_index = self.url.find("?")+1
    
    def __str__(self):
        return  str(self.start())
        
    def validate_protocol(self, protocol:list[str]) -> ValueError:
        if all(s not in self.url for s in protocol):
            raise ValueError("Invalid URL. Must be HTTP or HTTPS")
        
    def check_params_in_query(self) -> dict:
        self.validate_protocol(["http://", "https://"])
        if self.param_index:
            return {
                i.split('=')[0]:i.split("=")[1]
                for i in self.url[self.param_index:].split("&")
            }
        return {"Error":"Não tem parâmetro"}
        
    def start(self) -> dict:
        if len(self.url.strip()) > 0:
            return self.check_params_in_query()
        raise ValueError("Invalid URL. Must not be empty")
        

def main():
    print(QueryToDict("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"))

if __name__ == '__main__':
    main()