#
import os
from classes import PesquisaCargo
from classesarquivoanalise import AnaliseArquivo

#pesquisa = input("Pesquisa por cargo: ")
pesquisa = 'apresentador'


x = PesquisaCargo(pesquisa).PegaMediaSalarioJob()
print(x)










