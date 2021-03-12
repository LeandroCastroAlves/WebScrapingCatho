import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from classes import PesquisaCargo
def somageral():
    a = 0
    count_ = 0
    df = pd.read_csv('engenheiro-de-trafego.csv', sep=';')
    soma = 0
    for i in df['salarios']:
        str_ = str(i)
        str_ = str_.replace("A Combinar", "0").replace("De R$", "").replace("a R$", "").replace(",00", "").replace(".", "").split()
        for i in str_:
            i = float(i)
            soma += i
            if i > 0:
                i = 1
                count_ += i
    return print(round(soma/count_))


somageral()

