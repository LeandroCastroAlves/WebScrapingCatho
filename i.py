from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

# Classe para formatar o texto do link
class PesquisaCargo():

    def __init__(self, pesquisa, loop=0):
        self.loop = loop
        self.pesquisa = pesquisa

    def ConjuntoLink(self):
        pesquisa = self.pesquisa
        valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
        link = f"https://www.catho.com.br/vagas/{valor_pesquisa_traco}/"
        chamada = requests.get(link)
        class_error = "sc-kvZOFW cmUGSo"  # Classe de pagina sem vagas
        lista_unica = []
        lista_unica.append(link)
        for iteracao in range(2, 100, 1):
            objeto_formata_pesquisa = PesquisaCargo(pesquisa, iteracao).FormataPesquisaParaLink()
            link_formatado = link + objeto_formata_pesquisa
            requests_paginas_formatadas = requests.get(link_formatado)
            requests_paginas_formatadas_txt = requests_paginas_formatadas.text
            if not class_error in requests_paginas_formatadas_txt:
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

    def PegaNomeJob(self):

        vetor_nome_vagas = []
        pesquisa = self.pesquisa
        for i in self.ConjuntoLink():
            requests_paginas_link = requests.get(i)
            soup_paginas_link = BeautifulSoup(requests_paginas_link.text, 'html.parser')
            classe_nome_job = soup_paginas_link.find_all(class_="sc-jAaTju bBEyWy")

            for j in classe_nome_job:
                vetor_nome_vagas.append(j.a.text)
            return vetor_nome_vagas

    def PegaDescricaoJob(self):
        get_pagina = requests.get(self.link)
        soup_pagina = BeautifulSoup(get_pagina.text, 'html.parser')
        soup_pagina.encode()
        classe_descricao_job = soup_pagina.find_all(class_="sc-jAaTju bBEyWy")
        vetor_descricao_vagas = []
        vetor_descricao_vagas_href = []

        for i in classe_descricao_job:
            vetor_descricao_vagas.append(i.a.get('href'))

        for i in vetor_descricao_vagas:
            get_pagina_href = requests.get(i)
            soup_pagina_href = BeautifulSoup(get_pagina_href.text, 'html.parser')
            classe_descrica_vaga_href = soup_pagina_href.find_all(class_="descricaoVaga")

            for i in classe_descrica_vaga_href:
                vetor_descricao_vagas_href.append(i.p.text)

        return vetor_descricao_vagas_href


class GetDados:
    def __init__(self, link):
        self.link = link

    def PegaNomeJob(self):

        vetor_nome_vagas = []

        for i in self.link:
            requests_paginas_link = requests.get(i)
            soup_paginas_link = BeautifulSoup(requests_paginas_link.text, 'html.parser')
            classe_nome_job = soup_paginas_link.find_all(class_="sc-jAaTju bBEyWy")

            for j in classe_nome_job:
                vetor_nome_vagas.append(j.a.text)
            return vetor_nome_vagas

    def PegaDescricaoJob(self):
        get_pagina = requests.get(self.link)
        soup_pagina = BeautifulSoup(get_pagina.text, 'html.parser')
        soup_pagina.encode()
        classe_descricao_job = soup_pagina.find_all(class_="sc-jAaTju bBEyWy")
        vetor_descricao_vagas = []
        vetor_descricao_vagas_href = []

        for i in classe_descricao_job:
            vetor_descricao_vagas.append(i.a.get('href'))

        for i in vetor_descricao_vagas:
            get_pagina_href = requests.get(i)
            soup_pagina_href = BeautifulSoup(get_pagina_href.text, 'html.parser')
            classe_descrica_vaga_href = soup_pagina_href.find_all(class_="descricaoVaga")

            for i in classe_descrica_vaga_href:
                vetor_descricao_vagas_href.append(i.p.text)

        return vetor_descricao_vagas_href

    def PegaMediaSalarioJob(self):
        get_pagina = requests.get(self.link)
        soup_pagina = BeautifulSoup(get_pagina.text, 'html.parser')
        classe_salario_job = soup_pagina.find_all(class_="sc-eqIVtm bTmKXM")
        vetor_salario_vagas = []
        vetor_num = []
        for i in classe_salario_job:
            vetor_salario_vagas.append(i.text)
        for i in vetor_salario_vagas:
            if i != "A Combinar":
                vetor_num.append(i)

        df = pd.DataFrame(vetor_num)
        return df

    def InfoJobDataFrame(self):
        lista = []
        for i in range(5):
            link = self.PegaNomeJob(self.link)
            descricao = self.PegaDescricaoJob(self.link)
            lista.append[link, descricao]
        return lista
