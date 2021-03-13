import requests
from bs4 import BeautifulSoup

a = []


def PegaLocalizacaoJob(self):
    vetor_localizacao_vagas = []
    for i in self.ConjuntoLink():
        go = requests.get(i)
        v = BeautifulSoup(go.content.decode('UTF-8'), 'html.parser')
        v = v.find_all(class_="sc-jhAzac fBEAcd")
        for i in v:
            vetor_localizacao_vagas.append(i.text)
    return vetor_localizacao_vagas




print(PegaLocalizacaoJob())