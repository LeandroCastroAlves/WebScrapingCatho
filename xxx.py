import requests
from bs4 import BeautifulSoup
import pandas as pd

def PegaLocalizacaoJob():
    vetor_salario_vagas = []
    vetor_salario_media = []
    a = ['https://www.catho.com.br/vagas/engenheiro-de-producao/',
         'https://www.catho.com.br/vagas/engenheiro-de-producao/?q=Engenheiro%20de%20Produ%C3%A7%C3%A3o&page=2']
    vetor_localizacao_vagas = []
    for i in a:
        go = requests.get(i)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.find_all('header')
        for i in v:
            vetor_localizacao_vagas.append(i.button.string
                                           .replace(" (1)", "")
                                           .replace(" (2)", "")
                                           .replace(" (3)", "")
                                           .replace(" (4)", "")
                                           .replace(" (5)", ""))
    return vetor_localizacao_vagas



print(PegaLocalizacaoJob())