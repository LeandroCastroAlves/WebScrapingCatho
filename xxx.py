import csv

from googlesearch import search
import pandas as pd
import requests
from bs4 import BeautifulSoup

from classes import PesquisaCargo, GetDados
from i import PesquisaCargo, GetDados

# instancie o objeto cria_link com sua pesquisa entre aspas
# aplique o método ConjuntoLink
# a partir deste conjunto - que nada mais é do que um lista de links de paginas
# contendo varias vagas de emprego - , basta pega o

dataframe = PesquisaCargo("cientista de dados").PegaNomeJob()

print(dataframe)

