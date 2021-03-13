#
import os
from classes import PesquisaCargo
from classesarquivoanalise import AnaliseArquivo

#pesquisa = input("Pesquisa por cargo: ")
pesquisa = 'engenheiro de dados'


x = PesquisaCargo(pesquisa).PegaSalarioJob()
print(x)










