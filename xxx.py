import requests
from bs4 import BeautifulSoup
import pandas as pd



#//*[@id="search-result"]/div[2]/nav/a[6]
from ClasseDadosPesquisaCatho import DadosPesquisa


pesquisa = "apresentador"
        id_comum = "search-result"  # Classe de pagina sem vagas
        lista_unica = []
        lista_unica.append(self.link)
        for interacao in range(3, 5, 1):
            print(interacao)
            link_formatado = self.link + DadosPesquisa(pesquisa, interacao).FormataPesquisaParaLink()
            print(link_formatado)
            requests_paginas_formatadas = requests.get(link_formatado).text
            if id_comum in requests_paginas_formatadas:
                lista_unica.append(link_formatado)
            else:
                break
        pd.DataFrame(lista_unica).to_csv('Conjunto_Link.csv')
        return lista_unica
for i in range(2, 5, 1):
    print(DadosPesquisa("apresentador", i).FormataPesquisaParaLink())
