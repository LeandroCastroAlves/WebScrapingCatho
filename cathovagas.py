#
import os
import plotly.express as px
import pandas as pd
import requests
from bs4 import BeautifulSoup
from ClasseDadosPesquisaCatho import DadosPesquisa
from ClasseAnaliseArquivo import AnaliseArquivo
import plotly.graph_objects as go


#print(AnaliseArquivo(pesquisa="").PegaDtPubliJob())
print(AnaliseArquivo(pesquisa="").GeraArquivocsv())









