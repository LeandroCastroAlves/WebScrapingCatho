#
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup
from ClasseDadosPesquisaCatho import DadosPesquisa
from ClasseAnaliseInfoWeb import AnaliseArquivo
from ClasseAnaliseArquivoCsv import EstatisticasArquivo



#print(DadosPesquisa(pesquisa="engenheiro de dados").PegaLinkJobDataFrame())




#print(AnaliseArquivo(pesquisa="engenheiro de dados").GeraArquivocsv())
print(AnaliseArquivo(pesquisa="").GeraArquivocsv())
#print(DadosPesquisa(pesquisa="cientista de dados").PegaSalarioJob())
#print(AnaliseArquivo(pesquisa="cientista de dados").)

#EstatisticasArquivo('engenheiro-de-dados.csv').MediaGeral()









