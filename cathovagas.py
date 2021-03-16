#
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup
from ClasseDadosPesquisaCatho import DadosPesquisa
from ClasseAnaliseInfoWeb import AnaliseArquivo



#print(DadosPesquisa(pesquisa="engenheiro de dados").PegaLinkJobDataFrame())




#print(AnaliseArquivo(pesquisa="engenheiro de dados").GeraArquivocsv())
#print(AnaliseArquivo(pesquisa="").GeraArquivocsv())
#print(DadosPesquisa(pesquisa="").PegaDescricaoJob())
print(AnaliseArquivo(pesquisa="engenheiro de dados").GeraArquivocsv())










