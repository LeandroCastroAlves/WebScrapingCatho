#
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

from ClasseAnaliseWeb import EstatisticasWeb
from ClassePesquisaDados import DadosPesquisa
from ClasseGeraArquivoCsvEdf import AnaliseArquivo
from ClasseAnaliseArquivoCsv import EstatisticasArquivo


#EstatisticasWeb("engenheiro de alimentos").SalarioPorRegiao()

#print(DadosPesquisa(pesquisa="engenheiro de dados").)




#a = AnaliseArquivo(pesquisa="manaus").GeraArquivoCsvBackup()
#print(AnaliseArquivo(pesquisa="mg").GeraArquivoCsvBackup())
print(DadosPesquisa(pesquisa="mg").PegaLocalizacaoJob())
#print(AnaliseArquivo(pesquisa="cientista de dados").)

#EstatisticasArquivo('mgBK.csv').SalarioPorRegiao()











