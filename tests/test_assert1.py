from sys import path

path.append("/home/thiago/Documentos/cursos/python/python_strings")
from main import QueryToDict


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
    