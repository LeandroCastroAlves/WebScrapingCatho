import requests
from bs4 import BeautifulSoup
import time


from ClassePesquisaCargo import PesquisaCargo



def PegaDtPubliJob():
    vetor_dtpupli_vagas = []
    for i in a:
        go = requests.get(i)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.find_all('time')
        for i in v:
            v = i.span.string.split()[-1]
            vetor_dtpupli_vagas.append(v)
        return vetor_dtpupli_vagas
print(PegaDtPubliJob())
#//*[@id="job-18274692"]/header/div/div[2]/time/span
#<class 'bs4.element.Tag'>
#//*[@id="descricaoVagaTexto"]/text()
#//*[@id="job-18274692"]/header/div/div[2]/div