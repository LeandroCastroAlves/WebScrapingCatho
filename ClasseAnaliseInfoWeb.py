import pandas as pd
import requests
from bs4 import BeautifulSoup
from ClasseDadosPesquisaCatho import DadosPesquisa
import os

class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = DadosPesquisa(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()
    def GeraArquivocsv(self):
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")
        print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')
        arquivo = DadosPesquisa(self.pesquisa).PegaDtPubliJob()\
            .join(DadosPesquisa(self.pesquisa).PegaNomeJob())\
            .join(DadosPesquisa(self.pesquisa).PegaLocalizacaoJob())\
            .join(DadosPesquisa(self.pesquisa).PegaSalarioJob())\
            .join(DadosPesquisa(self.pesquisa).PegaLinkJobDataFrame()) \
            .to_csv(f'{self.valor_pesquisa_traco}.csv', index=None)
        os.remove('Conjunto_Link.csv')
        return arquivo

    def GeraDf(self):
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")

        return DadosPesquisa(self.pesquisa).PegaDtPubliJob()\
            .join(DadosPesquisa(self.pesquisa).PegaNomeJob())\
            .join(DadosPesquisa(self.pesquisa).PegaLocalizacaoJob())\
            .join(DadosPesquisa(self.pesquisa).PegaSalarioJob())\
            .join(DadosPesquisa(self.pesquisa).PegaDescricaoJob()) \
            .join(DadosPesquisa(self.pesquisa).PegaLinkJobDataFrame())






