import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from classes import PesquisaCargo

x = PesquisaCargo("engenheiro civil").PegaLocalizacaoJob()
print(x)






