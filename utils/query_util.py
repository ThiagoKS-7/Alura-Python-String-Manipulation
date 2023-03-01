class QueryToDict:
    '''
    QueryToDict
    
    Recebe uma URL com parâmetros, como https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100
    e retorna-os em formato json (como dict).
    
    Exceptions:    
        - Valida protocolos na URL (HTTP  e HTTPS), retornando exception se não houver
        - Valida se há parâmetros, retornando exception se não houver
        - Valida null safety (retorna exception se não for string ou se vier vazio)
    
    :param url:any
    
    :return dict[str]
    '''
    def __init__(self, url:any) -> None:
        self.url = url
        self.protocols = ["http://", "https://", "www.", ".io"]
        if type(url) is str:
            self.param_index = self.url.find("?")+1 # adiciona 1 pra cortar fora a ? da substring, com isso sempre retorna a posição dos params
        
    def __str__(self) -> str:
        return  str(self.start())
    
    def __len__(self) -> int:
        return len(str(self.start()))
    
    def __eq__(self, __o: object) -> bool:
        return str(self.start()) == str(__o.start())
            
    def _handle_validation(self) -> dict:
        return (
            ValueError(f"Error - Invalid URL '{self.url}'. Must be HTTP,HTTPS, WWW or .IO in the domain's end") if
            all(protocol not in self.url for protocol  in self.protocols) else
            self._check_query()
        )
    
    def _check_query(self) -> any:
        '''
            check_query(self) -> any
            
            Retorna dict[str] com keys e values dos params encontrados
            ou uma exceção informando não ter encontrado nenhum.            
            
            OBS: keyval's do dictionary de retorno - 
            Servem como key e value ao splitar (separar) valores  
            de uma lista como ['key=value', 'key=value']
        '''
        print(QueryToDict.__doc__)
        return (
                {
                    keyval.split('=')[0]:keyval.split("=")[1]
                    for keyval in self.url[self.param_index:].split("&")
                } 
                if self.param_index 
                else ValueError(f"Error - No query params found in '{self.url}'")
            )
        
    def start(self) -> dict:
        return (
            self._handle_validation() if type(self.url) is str and len(self.url.strip()) > 0
            else 
            ValueError(
                f"Error - Invalid URL '{self.url}" +
                f"{'- ' + str(type(self.url)) if type(self.url) is not str else ''}'. Must be a string and not empty"
            )
        )
        