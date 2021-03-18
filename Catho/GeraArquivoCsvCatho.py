import concurrent
from concurrent.futures.thread import ThreadPoolExecutor
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PesquisaDadosCatho import DadosPesquisa
import os
import threading

class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = DadosPesquisa(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()

    def GeraArquivoCsvBackup(self):
        if os.path.isfile('Conjunto_Link.csv'):
            cont_int = int(str(self.encontrados).split()[0])
            print(f"Total de anuncios {cont_int}")
            print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(DadosPesquisa.PegaDtPubliJob, self.pesquisa)
                future2 = executor.submit(DadosPesquisa.PegaNomeJob, self.pesquisa)
                future3 = executor.submit(DadosPesquisa.PegaLocalizacaoJob, self.pesquisa)
                future4 = executor.submit(DadosPesquisa.PegaSalarioJob, self.pesquisa)
                future5 = executor.submit(DadosPesquisa.PegaLinkDescricaoJob, self.pesquisa)

            df = future.result()\
                .join(future2.result())\
                .join(future3.result())\
                .join(future4.result())\
                .join(future5.result())\
                .to_csv(f'{self.valor_pesquisa_traco}.csv', index=None)
            os.remove('Conjunto_Link.csv')
            return df
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()
            AnaliseArquivo(self.pesquisa).GeraArquivoCsvBackup()


    def GeraDf(self):
        if os.path.isfile('Conjunto_Link.csv'):
            cont_int = int(str(self.encontrados).split()[0])
            print(f"Total de anuncios {cont_int}")
            print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(DadosPesquisa.PegaDtPubliJob, self.pesquisa)
                future2 = executor.submit(DadosPesquisa.PegaNomeJob, self.pesquisa)
                future3 = executor.submit(DadosPesquisa.PegaLocalizacaoJob, self.pesquisa)
                future4 = executor.submit(DadosPesquisa.PegaSalarioJob, self.pesquisa)
                future5 = executor.submit(DadosPesquisa.PegaLinkDescricaoJob, self.pesquisa)

            df = future.result() \
                .join(future2.result()) \
                .join(future3.result()) \
                .join(future4.result()) \
                .join(future5.result())
            os.remove('Conjunto_Link.csv')
            return df
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()
            AnaliseArquivo(self.pesquisa).GeraArquivoCsvBackup()






