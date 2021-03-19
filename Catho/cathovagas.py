#
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

from AnaliseWebCatho import EstatisticasWeb
from PesquisaDadosCatho import DadosPesquisa
from GeraArquivoCsvCatho import AnaliseArquivo
from AnaliseArquivoCsvCatho import EstatisticasArquivo
print(DadosPesquisa(pesquisa="uberaba").PegaLocalizacaoJob())

#EstatisticasWeb("engenheiro de alimentos").SalarioPorRegiao()

#print(DadosPesquisa(pesquisa="engenheiro de dados").)




#a = AnaliseArquivo(pesquisa="manaus").GeraArquivoCsvBackup()
#print(AnaliseArquivo(pesquisa="uberaba").GeraArquivoCsvBackup())

#print(AnaliseArquivo(pesquisa="cientista de dados").)

#EstatisticasArquivo('mgBK.csv').SalarioPorRegiao()











