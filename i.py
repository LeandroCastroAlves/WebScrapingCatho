
valor_pesquisa = input("teste: ")

class cria_link():
    def cria(vl, loop):
        vl = valor_pesquisa.replace("ã", "a").replace("ç", "c").replace("é", "e").lower()
        string = ""
        item = vl.split()
        i_len = len(item)

        if i_len > 1:

            for i, valor in enumerate(vl.split()):
                string += f"{valor}%20"

                if i == (i_len - 2):
                    string_if = "?q="+string+item[-1]+"&page="+str(loop)
            return string_if

        elif i_len == 1:
            string_if = "?q=" + vl + "&page="+str(loop)
        return string_if

objeto = cria_link.cria(valor_pesquisa, 1)

print(objeto)