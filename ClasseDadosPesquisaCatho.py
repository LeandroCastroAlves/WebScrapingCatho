import requests
from bs4 import BeautifulSoup
from math import floor
import pandas as pd
import os


# Classe para formatar o texto do link
class DadosPesquisa():

    def __init__(self, pesquisa=None, loop=None, estado=None):
        self.estado = f"{estado}/"
        self.loop = loop
        self.pesquisa = pesquisa
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").replace(
            "á", "a").lower()
        if estado is None:
            self.link = f"https://www.catho.com.br/vagas/{self.valor_pesquisa_traco}/"
        elif estado is not None:
            self.link = f"https://www.catho.com.br/vagas/{self.valor_pesquisa_traco}/{self.estado}"
        if len(self.pesquisa) == 0:
            self.link = "https://www.catho.com.br/vagas"

    def ConjuntoLink(self):

        pesquisa = self.pesquisa
        lista_unica = []
        lista_unica.append(self.link)
        x = round(DadosPesquisa(pesquisa).PegaQtdJob() / 20)+2
        print(x)
        for interacao in range(2, x, 1):
            link_formatado = self.link + DadosPesquisa(pesquisa, loop=interacao).FormataPesquisaParaLink()
            print(link_formatado)
            lista_unica.append(link_formatado)
        return pd.DataFrame(lista_unica).to_csv('Conjunto_Link.csv', sep=",", index=False, columns=None)

    def FormataPesquisaParaLink(self):

        global string_if
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
        elif i_len == 0:
            string_if = "/?page=" + str(self.loop)
        return string_if

    def PegaDtPubliJob(self):

        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            print(link)
            vetor_dtpupli_vagas = []
            for j, i in enumerate(link):
                print(j)
                go = requests.get(i)
                v = BeautifulSoup(go.text, 'html.parser')
                v = v.find(id='search-result')
                v = v.find_all('li')
                for i in v:
                    vetor_dtpupli_vagas.append(i.get("data-gtm-dimension-44").split("T")[0])
            return pd.DataFrame({'datapubli': vetor_dtpupli_vagas})
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()
            return DadosPesquisa(self.pesquisa).PegaDtPubliJob()

    def PegaDescricaoJob(self):

        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            vetor_desc_vagas = []
            for i in link:
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
                        v = i.text.replace("         ", "") \
                            .replace('\n', '') \
                            .replace("'", "") \
                            .replace("    ", "")
                        vetor_desc_vagas.append(v)

            return pd.DataFrame({'descricao': vetor_desc_vagas})
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()

            return DadosPesquisa(self.pesquisa).PegaDescricaoJob()

    def PegaNomeJob(self):
        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            vetor_nome_vagas = []
            for i in link:
                go = requests.get(i)
                v = BeautifulSoup(go.text, 'html.parser')
                v = v.find(id='search-result')
                v = v.find_all('li')
                for i in v:
                    vetor_nome_vagas.append(i.h2.a.string)

            return pd.DataFrame({'nome': vetor_nome_vagas})
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()

            return DadosPesquisa(self.pesquisa).PegaNomeJob()

    def PegaLocalizacaoJob(self):

        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            vetor_localizacao_vagas = []
            cidade = []
            estado = []
            for i in link:
                go = requests.get(i)
                v = BeautifulSoup(go.text, 'html.parser')
                v = v.find(id='search-result')
                v = v.find_all('header')
                for i in v:
                    vetor_localizacao_vagas.append(i.button.string
                                                   .replace(" (1)", "")
                                                   .replace(" (2)", "")
                                                   .replace(" (3)", "")
                                                   .replace(" (4)", "")
                                                   .replace(" (5)", "")
                                                   .replace(" (6)", "")
                                                   .replace(" (7)", "")
                                                   .replace(" (8)", "")
                                                   .replace(" (9)", "")
                                                   .replace(" (10)", "")
                                                   .replace(" (11)", "")
                                                   .replace(" (12)", "")
                                                   .replace(" (13)", "")
                                                   .replace(" (14)", "")
                                                   .replace(" (15)", "")
                                                   .replace(" (16)", "")
                                                   .replace(" (17)", "")
                                                   .replace(" (18)", "")
                                                   .replace(" (19)", "")
                                                   .replace(" (20)", "")
                                                   .split(sep="-"))
            for i in vetor_localizacao_vagas:
                cidade.append(i[0])
                estado.append(i[1])
            df = pd.DataFrame({"cidade": cidade,
                               "estado": estado})

            return df
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()

            return DadosPesquisa(self.pesquisa).PegaLocalizacaoJob()

    def PegaSalarioJob(self):

        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            vetor_salario_vagas = []
            vetor_salario_media = []
            for i in link:
                go = requests.get(i)
                v = BeautifulSoup(go.text, 'html.parser')
                v = v.find(id='search-result')
                v = v.find_all('header')
                for i in v:
                    for j in i:
                        v = j.find_all('div')
                        vetor_salario_vagas.append(v[2].text)
            for i in vetor_salario_vagas:
                str(i)
                v = i.replace("A Combinar", "0") \
                    .replace("De R$", "") \
                    .replace("a R$", "") \
                    .replace(",00", "") \
                    .replace("Acima de R$ ", "") \
                    .replace("Até R$ ", "") \
                    .replace(".", "").split()
                v = [int(elem) for elem in v]
                v = sum(v) / len(v)
                vetor_salario_media.append(round(v))

            return pd.DataFrame({'salario': vetor_salario_media})
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()

            return DadosPesquisa(self.pesquisa).PegaSalarioJob()

    def PegaQtdJob(self):
        go = requests.get(self.link)
        v = BeautifulSoup(go.text, 'html.parser')
        v = v.find(id='search-result')

        v = v.div.p.string
        v = v.replace("Total de anúncios: ", "").replace(".", "")

        return int(v)

    def PegaLinkJobDataFrame(self):

        if os.path.isfile('Conjunto_Link.csv'):
            interacao = pd.read_csv('Conjunto_Link.csv')
            link = []
            for i in interacao['0']:
                link.append(i)
            vetor_link_vagas = []
            for i in link:
                go = requests.get(i)
                v = BeautifulSoup(go.text, 'html.parser')
                v = v.find(id='search-result')
                v = v.find_all('article')
                for i in v:
                    vetor_link_vagas.append(i.div.h2.a.get('href'))

            return pd.DataFrame({'link': vetor_link_vagas})
        else:
            DadosPesquisa(self.pesquisa).ConjuntoLink()

            return DadosPesquisa(self.pesquisa).PegaLinkJobDataFrame()

    def PesquisaFormat(self):
        return self.valor_pesquisa_traco
















