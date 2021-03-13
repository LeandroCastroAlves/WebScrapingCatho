import requests
from bs4 import BeautifulSoup

a = []
def PegaLocalizacaoJob():
    a = ["https://www.catho.com.br/vagas/apresentador/"]
    vetor_localizacao_vagas = []
    for i in a:
        go = requests.get(i)
        soup = BeautifulSoup(go.content.decode('UTF-8'), 'html.parser')
        classe_job = soup.find_all(id="search-result")
        soup_ = BeautifulSoup(classe_job, 'html.parser')

        print(soup_.prettify())


print(PegaLocalizacaoJob())