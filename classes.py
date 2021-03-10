from bs4 import BeautifulSoup
import requests
# Classe para formatar o texto do link
class cria_link():
    def cria(vl, loop):
        vl = vl.replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
        string = ""
        item = vl.split()
        i_len = len(item)

        if i_len > 1:

            for i, valor in enumerate(vl.split()):
                string += f"{valor}%20"

                if i == (i_len - 2):
                    string_if = "?q=" + string + item[-1] + "&page=" + str(loop)
            return string_if

        elif i_len == 1:
            string_if = "?q=" + vl + "&page=" + str(loop)
        return string_if

class link():
    def PegaNomeJob(link):
        vai_pra_pagina = requests.get(link)
        soup = BeautifulSoup(vai_pra_pagina.text, 'html.parser')
        classe_nome = soup.find_all(class_="sc-jAaTju bBEyWy")
        vetor_nome_vagas = []

        for i in classe_nome:
            vetor_nome_vagas.append(i.a.text)
        return vetor_nome_vagas