import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

from PesquisaDadosCatho import DadosPesquisa
from GeraArquivoCsvCatho import AnaliseArquivo
from AnaliseArquivoCsvCatho import EstatisticasArquivo
#print(DadosPesquisa().PegaDescricaoJob())
#print(DadosPesquisa("araguari").pesquisa)
#print(DadosPesquisa(pesquisa="uberaba").PegaDescCurtaJob())
#EstatisticasArquivo("Catho/uberaba.csv").SalarioPorRegiao()
#print(DadosPesquisa(pesquisa="engenheiro de dados").)
print(AnaliseArquivo(pesquisa="uberaba").GeraArquivoCsv())
#print(AnaliseArquivo(pesquisa="cientista de dados").)
#EstatisticasArquivo('mgBK.csv').SalarioPorRegiao()











