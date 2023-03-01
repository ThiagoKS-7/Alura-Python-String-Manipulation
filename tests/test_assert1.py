from sys import path

path.append("/home/thiago/Documentos/cursos/python/python_strings")
from main import QueryToDict
'''
https://www.hashtagtreinamentos.com/args-e-kwargs-em-python?
gclid=Cj0KCQiA6fafBhC1ARIsAIJjL8mPtL3ZDQ885G811fbs5UkEBM9Hjg-
4bRcH4LLP_UeGe5OgLFZ8Kr4aAtiiEALw_wcB

Como usar o *Args de maneira inteligente?

Entenda que o args nada mais é do que uma tupla, 
e do mesmo modo devemos colocar dentro valores que se correspondam,
grupos de valores que façam sentido.

**Kwargs
O resultado do Kwargs é um dicionário com todos os parâmetros nele,
por este motivo você tem a opção de criar condições para cada parâmetro
usando o IF ou outras estruturas condicionais:
'''

def test_invalid__http_protocol_exception():
    assert "Must be HTTP or HTTPS" in str(QueryToDict("bytebank"))
    
def test_query_exception():
    assert "Error - No query params found" in str(QueryToDict("https://bytebank.com"))
    
def test_invalid_url_None_exception():
    assert "Error - Invalid URL 'None - <class 'NoneType'>'. Must be a string and not empty" in str(QueryToDict(None))
    
def test_invalid_url_empty_exception():
    assert "Error - Invalid URL ' '. Must be a string and not empty" in str(QueryToDict(""))
    
def test_invalid_url_empty_spaced_exception():
    assert "Must be a string and not empty" in str(QueryToDict("    "))
    
def test_invalid_url_number_exception():
    assert "Error - Invalid URL '2 - <class 'int'>'. Must be a string and not empty" in str(QueryToDict(2))
    