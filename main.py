from utils.cep_util import CepFinder
from utils.query_util import QueryToDict
from utils.exchange_util import ExchangeBrlUsd, ExchangeUsdBrl

def main():
    print(QueryToDict("https://bytebank.com/cambio?moedaOrigem=BRL&moedaDestino=USD&quantidade=100"))
    print(f"\nCEP regex: {CepFinder('Rua das Flores 72, ap 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120')}\n")
    print(ExchangeBrlUsd(100))
    print(ExchangeUsdBrl(100))


if __name__ == '__main__':
    main()