class QueryToDict:
    def __init__(self, url):
        self.__set_values__(url)
        
    def __set_values__(self, url):
        self.url = url
        if type(url) is str:
            self.param_index = self.url.find("?")+1
    
    def __str__(self):
        return  str(self.start())
            
    def check_params_in_query(self) -> dict:
        if all(s not in self.url for s in ["http://", "https://"]):
            return ValueError(f"Error - Invalid URL '{self.url}'. Must be HTTP or HTTPS")
        if self.param_index:
            return {
                i.split('=')[0]:i.split("=")[1]
                for i in self.url[self.param_index:].split("&")
            }
        return ValueError(f"Error - No query params found in '{self.url}'")
        
    def start(self) -> dict:
        if type(self.url) is str and len(self.url.strip()) > 0:
            return self.check_params_in_query()
        return ValueError(f"Error - Invalid URL '{self.url} {'- ' + str(type(self.url)) if type(self.url) is not str else ''}'. Must be a string and not empty")
        

def main():
    print(QueryToDict("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"))




if __name__ == '__main__':
    main()