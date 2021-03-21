import requests
from bs4 import BeautifulSoup
import pandas as pd


def PegaDescricaoJobTeste(arquivo):
    print("Buscando: Descricao")
    interacao = pd.read_csv(arquivo)

    for i in interacao['descricao'].values:
        go = requests.get(i)
        soup = BeautifulSoup(go.text, 'html.parser')
        texto = soup.find(id='descricaoVagaTexto')
        print(texto.string)

    return interacao
print(PegaDescricaoJobTeste("uberaba.csv"))