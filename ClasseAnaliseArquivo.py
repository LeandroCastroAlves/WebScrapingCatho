import pandas as pd
import requests
from bs4 import BeautifulSoup

from ClassePesquisaCargo import PesquisaCargo
import os


class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = PesquisaCargo(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()
    def GeraArquivocsv(self):
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")
        print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')

        return PesquisaCargo(self.pesquisa).PegaDtPubliJob()\
            .join(PesquisaCargo(self.pesquisa).PegaNomeJob())\
            .join(PesquisaCargo(self.pesquisa).PegaLocalizacaoJob())\
            .join(PesquisaCargo(self.pesquisa).PegaSalarioJob())\
            .join(PesquisaCargo(self.pesquisa).PegaDescricaoJob()).to_csv(f'{self.valor_pesquisa_traco}.csv', sep=";")


    def MediaSalarial(self):
        vetor_salario_vagas = []
        for i in PesquisaCargo(self.pesquisa).ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('header')
            for i in v:
                for j in i:
                    v = j.find_all('div')
                    v = (v[2].text)
                    vetor_salario_vagas.append(v)
        return v






