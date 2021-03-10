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

import os



valor_pesquisa = input("Cargo: ")
valor_pesquisa_under = valor_pesquisa.replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("é", "e").lower()

#valor_pesquisa = "Desenvolvedor Java"
#valor_pesquisa_under = valor_pesquisa.replace(" ", "_").replace("ã", "a").replace("ç", "c").lower()

def webscr():
    for resultado in search(f'"{valor_pesquisa}" linkedin', stop=1):
        link = resultado
    try:
        chamada = requests.get(link)
    except:
        print("erro")
    soup = BeautifulSoup(chamada.text, 'html.parser')
    classe_lk_job = soup.find_all(class_="result-card__full-card-link")
    f = csv.writer(open('links_dowload.csv', 'w', newline='', encoding='utf-8'))
    f.writerow(['Name', 'Link'])
    for i in classe_lk_job:
        nome = i.contents[0]
        link = i.get('href')
        f.writerow([nome, link])

def cria_arquivo_ml():
    arquivo = open('links_dowload.csv')
    df = pd.read_csv(arquivo)
    dfLink = df['Link']
    lista_palavras = []
    for i in dfLink:
        link_job_desc = requests.get(i)
        soup = BeautifulSoup(link_job_desc.text, 'html.parser')
        classe_lk_job = soup.find_all(class_="description")
        for j in classe_lk_job:
            txt = j.find('section')
        for j in classe_lk_job:
            txt = j.find('section')
            txt = txt.contents[0]
        pontuacoes = [",", ".", "(", ")", ";", ":", "-", "#", "&", "!", "?"]
        tags = ["<head>", "</script>", "<title>", "</title>", "</link>", "</meta>", "</head>", "<body>", "</span>",
            "</icon>", "</a>", "</div>", "</button>", "</li>", "</ul>", "</label>", "</section>", "</input>", "</form>",
            "</code>", "</template>", "</nav>", "</header>", "</h3>", "<span>", "</figure>", "</h1>", "<div>", "</h2>",
            "</p>", "</footer>", "<b>", "</b>", "</main>", "<br/>", "<strong>", "<u>", "</u>", "</strong>", "<figure>",
            "</body>", "</html>", "<li>", "<ul>", "</li>", "<p>", "/p", "</em>", "<em>"]
        for i in pontuacoes:
            palavras = str(txt).replace(i, " ")
        for i in tags:
            palavras = palavras.replace(i, " ").replace(",", "")
        palavras = palavras.split()
        palavras = list(palavras)
        del palavras[0:12]
        for i in palavras:
            lista_palavras.append(i)

    f = csv.writer(open(f'{valor_pesquisa_under}.csv', 'w', newline='', encoding='utf-8'))
    f.writerow([lista_palavras])
if not os.path.isfile(f"{valor_pesquisa_under}.csv"):
    webscr()
    cria_arquivo_ml()

    # cria objeto vetorizador
    lista_palavras = pd.read_csv(f"{valor_pesquisa_under}.csv")

    try:
        # cria objeto vetorizador
        vetorizar = CountVectorizer()
        # aplica vetorizador nos dado
        vetorizar.fit(lista_palavras)
        # saida
        matrix = vetorizar.transform(lista_palavras)
        print(matrix.toarray())

        # Instanci o objeto TFIDF
        vetorizar = TfidfVectorizer()
        vetorizar.fit(lista_palavras)
        print(vetorizar.vocabulary_)
        print(vetorizar.idf_)
    except:
        if ValueError:
            print(f"Pesquisa não retornou resultados")
        os.remove(f"{valor_pesquisa_under}.csv")
else:
    # cria objeto vetorizador
    lista_palavras = pd.read_csv(f"{valor_pesquisa_under}.csv")

    try:
        # cria objeto vetorizador
        vetorizar = CountVectorizer()
        # aplica vetorizador nos dados
        vetorizar.fit(lista_palavras)
        # saida
        matrix = vetorizar.transform(lista_palavras)
        print(matrix.toarray())

        # Instanci o objeto TFIDF
        vetorizar = TfidfVectorizer()
        vetorizar.fit(lista_palavras)
        print(vetorizar.vocabulary_)
        print(vetorizar.idf_)
    except:
        if ValueError:
            print(f"Pesquisa não retornou resultados")
        os.remove(f"{valor_pesquisa_under}.csv")






