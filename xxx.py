import requests
from bs4 import BeautifulSoup

a = []
def PegaLocalizacaoJob():
    a = ["https://www.catho.com.br/vagas/engenheiro-de-producao/", "https://www.catho.com.br/vagas/engenheiro-de-producao/?q=Engenheiro%20de%20Produ%C3%A7%C3%A3o&page=2"]
    vetor_localizacao_vagas = []
    for i in a:
        go = requests.get(i)
        soup = BeautifulSoup(go.text, 'html.parser')
        soup = soup.find(id='search-result')
        soup = soup.find_all('li')
        for i in soup:
            print(i.h2.a.string)




PegaLocalizacaoJob()