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
        class_error = "sc-kvZOFW cmUGSo"  # Classe de pagina sem vagas
        lista_unica = []
        lista_unica.append(self.link)
        for iteracao in range(2, 100, 1):
            link_formatado = self.link + PesquisaCargo(pesquisa, iteracao).FormataPesquisaParaLink()
            requests_paginas_formatadas = requests.get(link_formatado).text
            if not class_error in requests_paginas_formatadas:
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

        vetor_desc_vagas_href = []
        vetor_desc_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            soup = BeautifulSoup(go.text, 'html.parser')
            classe_desc_job = soup.find_all(class_="sc-jAaTju bBEyWy")
            for i in classe_desc_job:
                vetor_desc_vagas_href.append(i.a.get('href'))
            for i in vetor_desc_vagas_href:
                go = requests.get(i)
                soup = BeautifulSoup(go.content.decode('UTF-8').replace('\n', '').replace("'", " ").replace("         ", "").replace("     ", ""), 'html.parser')
                classe_desc_vaga_href = soup.find(class_="descricaoVaga")
                vetor_desc_vagas.append(classe_desc_vaga_href.p.text)

        return vetor_desc_vagas

    def PegaNomeJob(self):
        vetor_nome_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            soup = BeautifulSoup(go.text, 'html.parser')
            soup = soup.find(id='search-result')
            soup = soup.find_all('li')
            for i in soup:
                vetor_nome_vagas.append(i.h2.a.string)
        return vetor_nome_vagas

    def PegaSalarioJob(self):

        vetor_salario_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find_all(class_="sc-eqIVtm bTmKXM")
            for i in v:
                vetor_salario_vagas.append(i.text)
        return vetor_salario_vagas

    def PegaLocalizacaoJob(self):
        vetor_localizacao_vagas = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            v = BeautifulSoup(go.text, 'html.parser')
            v = v.find(id='search-result')
            v = v.find_all('header')
            for i in v:
                vetor_localizacao_vagas.append(i.button.string)
            return vetor_localizacao_vagas

    def PegaMediaSalarioJob(self):

        vetor_salario_vagas = []
        vetor_num = []
        for i in self.ConjuntoLink():
            go = requests.get(i)
            soup = BeautifulSoup(go.text, 'html.parser')
            classe_salario_job = soup.find_all(class_="sc-eqIVtm bTmKXM")
            for i in classe_salario_job:
                vetor_salario_vagas.append(i.text)
            for i in vetor_salario_vagas:
                if i != "A Combinar":
                    vetor_num.append(i)

            df = pd.DataFrame(vetor_num)
        return df

    def PegaQtdJob(self):
        go = requests.get(self.link)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')
        v = v.div.p.string
        v = v.replace("Total de anúncios: ", "").replace(".", "")
        return int(v)

    def PesquisaFormat(self):
        return self.valor_pesquisa_traco















