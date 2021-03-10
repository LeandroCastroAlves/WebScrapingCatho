import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os
from classes import cria_link
valor_pesquisa = input("teste: ")

#valor_pesquisa = "cientista de dados"

acentos_map = {" ": "_", "ã": "a", "ç":"c", "é": "e"}
valor_pesquisa_under = valor_pesquisa.replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
valor_pesquisa.split()
valor_pesquisa_traco = valor_pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
vl = valor_pesquisa.replace("ã", "a").replace("ç", "c").replace("é", "e").lower()

link = f"https://www.catho.com.br/vagas/{valor_pesquisa_traco}/"

if os.path.isfile(f"{valor_pesquisa_under}.csv"):
    try:
        chamada = requests.get(link)
    except:
        print("erro")

f = csv.writer(open(f'{valor_pesquisa_under}.csv', 'w', newline='', encoding='utf-8'))
f.writerow(['NPage', 'Link'])
f.writerow([1, link])
class_error = "sc-kvZOFW cmUGSo" # Classe de pagina sem vagas

for iteracao in range(2, 100, 1):
    objeto = cria_link.cria(valor_pesquisa, iteracao)
    link_n_pag = link+objeto
    chamada_n_pag = requests.get(link_n_pag)
    chamada_n_pag_txt = chamada_n_pag.text

    if not class_error in chamada_n_pag_txt:
        f.writerow([iteracao, link_n_pag])
        print(link + objeto)
    else:
        break
