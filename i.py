from googlesearch import search
import pandas as pd
import requests
from bs4 import BeautifulSoup


class link():
    def PegaNomeJob(link):
        vai_pra_pagina = requests.get(link)
        soup = BeautifulSoup(vai_pra_pagina.text, 'html.parser')
        classe_nome = soup.find_all(class_="sc-jAaTju bBEyWy")
        vetor_nome_vagas = []

        for i in classe_nome:
            vetor_nome_vagas.append(i.a.text)
        return vetor_nome_vagas

    def PegaDescricaoVaga(self):
n = []
df = pd.read_csv('engenheiro_de_dados.csv')
for i in df["Link"]:
    teste = link.PegaNomeJob(i)
    n += teste

print(n)


