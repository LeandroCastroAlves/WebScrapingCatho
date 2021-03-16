import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from math import floor

#//*[@id="search-result"]/div[2]/nav/a[6]
from ClasseDadosPesquisaCatho import DadosPesquisa

def PegaDtPubliJob():
    if os.path.isfile('Conjunto_Link.csv'):
        interacao = pd.read_csv('Conjunto_Link.csv')
        link = []
        for i in interacao['0']:
            link.append(i)
        print(link)
        vetor_dtpupli_vagas = []
        for j, i in enumerate(link):
            print(j)
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('li')
            for i in v:
                vetor_dtpupli_vagas.append(i.get("data-gtm-dimension-44").split("T")[0])
        return pd.DataFrame({'datapubli': vetor_dtpupli_vagas})
    else:
        DadosPesquisa(self.pesquisa).ConjuntoLink()
        return DadosPesquisa(self.pesquisa).PegaDtPubliJob()

    PegaDtPubliJob()
x = 1 + 1
print(x)
