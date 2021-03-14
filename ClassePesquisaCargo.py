import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

# Classe para formatar o texto do link
class PesquisaCargo():

    def __init__(self, pesquisa, loop=0, valor_pesquisa_traco=""):
        self.loop = loop
        self.pesquisa = pesquisa
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é", "e").replace("á", "a").lower()
        self.link = f"https://www.catho.com.br/vagas/{self.valor_pesquisa_traco}/"

    def ConjuntoLink(self):
        pesquisa = self.pesquisa
        id_comum = "search-result"  # Classe de pagina sem vagas
        lista_unica = []
        lista_unica.append(self.link)
        for iteracao in range(2, 10, 1):
            link_formatado = self.link + PesquisaCargo(pesquisa, iteracao).FormataPesquisaParaLink()
            requests_paginas_formatadas = requests.get(link_formatado).text
            if id_comum in requests_paginas_formatadas:
                lista_unica.append(link_formatado)
            else:
                break
        return lista_unica

    def FormataPesquisaParaLink(self):
        pesquisa = self.pesquisa.replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
        string = ""
        item = pesquisa.split()
        i_len = len(item)
        if i_len > 1:
            for i, valor in enumerate(pesquisa.split()):
                string += f"{valor}%20"
                if i == (i_len - 2):
                    string_if = "?q=" + string + item[-1] + "&page=" + str(self.loop)
            return string_if
        elif i_len == 1:
            string_if = "?q=" + pesquisa + "&page=" + str(self.loop)
        return string_if


    def PegaDescricaoJob(self):

        vetor_desc_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('article')
            for i in v:
                link = i.div.h2.a.get('href')
                go = requests.get(link)
                v = BeautifulSoup(go.content.decode('UTF-8'), 'html.parser')
                v = v.find_all(id='descricaoVagaTexto')
                for i in v:
                    v = i.text.replace("         ", "").replace('\n', '').replace("'", "").replace("    ", "")
                    vetor_desc_vagas.append(v)
        return pd.DataFrame({'descricao': vetor_desc_vagas})

        return vetor_desc_vagas

    def PegaNomeJob(self):
        vetor_nome_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('li')
            for i in v:
                vetor_nome_vagas.append(i.h2.a.string)
        return pd.DataFrame({'nome': vetor_nome_vagas})

    def PegaLocalizacaoJob(self):
        vetor_localizacao_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('header')
            for i in v:
                vetor_localizacao_vagas.append(i.button.string)
        return pd.DataFrame({'localizacao': vetor_localizacao_vagas})

    def PegaSalarioJob(self):
        vetor_salario_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('header')
            for i in v:
                for j in i:
                    v = j.find_all('div')
                    vetor_salario_vagas.append(v[2].text)
        return pd.DataFrame({'salario': vetor_salario_vagas})

    def PegaDtPubliJob(self):
        vetor_dtpupli_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('time')
            for i in v:
                v = i.span.string.split()[-1]
                vetor_dtpupli_vagas.append(v)
        return pd.DataFrame({'datapubl': vetor_dtpupli_vagas})

    def PegaQtdJob(self):
        go = requests.get(self.link)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.div.p.string
        v = v.replace("Total de anúncios: ", "").replace(".", "")
        return int(v)

    def PesquisaFormat(self):
        return self.valor_pesquisa_traco















