from googlesearch import search
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from sklearn.decomposition._nmf import _beta_divergence

valor_pesquisa = "Médico"
valor_pesquisa_under = valor_pesquisa.replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").lower()

def k():
    for resultado in search(f'"{valor_pesquisa}" linkedin', stop=1):
        link = resultado
    try:
        chamada = requests.get(link)
    except:
        print("erro")
    soup = BeautifulSoup(chamada.text, 'html.parser')
    classe_lk_job = soup.find_all(class_="result-card__full-card-link")
    f = csv.writer(open(f'links_dowload_{valor_pesquisa_under}.csv', 'w', newline='', encoding='utf-8'))
    f.writerow(['Name', 'Link'])

    for i in classe_lk_job:
        print(i)
        link = i.get('href')

k()
i = pd.read_csv("links_dowload_medico.csv")
print(i.head)