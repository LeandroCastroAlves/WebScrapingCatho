import requests
from bs4 import BeautifulSoup
import pandas as pd


def PegaDtPubliJob():
    a = ["https://www.catho.com.br/vagas/apresentador/"]
    vetor_link_vagas = []
    for i in a:
        go = requests.get(i)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.find_all('li')
        for i in v:
            vetor_link_vagas.append(i.get("data-gtm-dimension-44").split("T")[0])
    return pd.DataFrame({'datapubli': vetor_link_vagas})

print(PegaDtPubliJob())