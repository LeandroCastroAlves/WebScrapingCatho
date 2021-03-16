import requests
from bs4 import BeautifulSoup
import pandas as pd



#//*[@id="search-result"]/div[2]/nav/a[6]
def PegaQtdJob():
    go = requests.get("https://www.catho.com.br/vagas/engenheiro%20de%20dados/")
    v = BeautifulSoup(go.text, 'html.parser')
    v = v.find(id='search-result')
    v = v.div.p.string
    v = v.replace("Total de anúncios: ", "").replace(".", "")
    v = int(v)
    return v
print(round(PegaQtdJob()) + 1)
