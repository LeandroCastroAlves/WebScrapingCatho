import requests
from bs4 import BeautifulSoup
import pandas as pd


def PegaDescricaoJobTeste(arquivo):
    print("Buscando: Descricao")
    interacao = pd.read_csv(arquivo)

    for i in interacao['descricao'].values:
        go = requests.get(i)
        soup = BeautifulSoup(go.content, 'html.parser')
        texto = soup.find(id='descricaoVagaTexto')
        print(texto.string)

    return interacao
    print(PegaDescricaoJobTeste("uberaba.csv"))

go = requests.get("https://www.catho.com.br/vagas/uberaba/")
soup = BeautifulSoup(go.text, 'html.parser')

soup = soup.find_all(class_='job-description')
for i in soup:
    print(i.string)