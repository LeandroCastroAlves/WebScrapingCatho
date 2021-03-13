import requests
from bs4 import BeautifulSoup

a = []
def PegaLocalizacaoJob():
    a = ["https://www.catho.com.br/vagas/apresentador/"]
    vetor_localizacao_vagas = []
    for i in a:
        go = requests.get(i)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.find_all('header')
        print(v.)





PegaLocalizacaoJob()