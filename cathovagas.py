from classes import PesquisaCargo
import pandas as pd
import csv
import time
pesquisa = input("Cargo: ")
info_lista = []
df = pd.DataFrame(info_lista, columns=['nome', 'descricao', 'localizacao', 'salario'])




encontrados = PesquisaCargo(pesquisa).PegaQtdJob()
print(encontrados)



