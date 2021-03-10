from googlesearch import search
import pandas as pd

valor_pesquisa = input("Cargo: ")

acentos_map = {" ": "_", "ã": "a", "ç":"c", "é": "e"}
df = pd.DataFrame(valor_pesquisa)
valor_pesquisa_x = valor_pesquisa.format_map(acentos_map)

print(valor_pesquisa_x)

for resultado in search(f'"{valor_pesquisa}" catho', stop=1):
    link = resultado
print(link)