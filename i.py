import requests
from bs4 import BeautifulSoup
import time


from ClassePesquisaCargo import PesquisaCargo



def PegaDtPubliJob():
    a = ['https://www.catho.com.br/vagas/engenheiro-de-dados/']
    vetor_salario_vagas = []
    for i in a:
        go = requests.get(i)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.find_all('time')
        for i in v:
            print(i.string)
        return vetor_salario_vagas
print(PegaDtPubliJob())
#//*[@id="job-18274692"]/header/div/div[2]/time/span
#<class 'bs4.element.Tag'>
#//*[@id="descricaoVagaTexto"]/text()
#//*[@id="job-18274692"]/header/div/div[2]/div