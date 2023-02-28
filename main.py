def query_to_dict(url:str) -> str:
    if len(url.strip()) > 0:
        if all(s not in url for s in ["http://", "https://"]):
            raise ValueError("Invalid URL. Must be HTTP or HTTPS")
        param_index = url.find("?")+1
        if param_index:
            return {
                i.split('=')[0]:i.split("=")[1]
                for i in url[param_index:].split("&")
            }
        return "Não tem parâmetro"
    raise ValueError("Invalid URL. Must not be empty")

def main():
    print(query_to_dict("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"))

if __name__ == '__main__':
    main()