import pandas as pd
from classes import PesquisaCargo
import os
import time

class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = PesquisaCargo(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()
    def GeraArquivo(self):
        info_lista = []
        df = pd.DataFrame(info_lista, columns=['nome', 'localizacao', 'salarios', 'descricao'])
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")
        print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')
        print(PesquisaCargo(self.pesquisa).PegaNomeJob())
        print(PesquisaCargo(self.pesquisa).PegaLocalizacaoJob())
        print(PesquisaCargo(self.pesquisa).PegaSalarioJob())
        print(PesquisaCargo(self.pesquisa).PegaDescricaoJob())
        print(cont_int)


    def MediaSalarial(self):
        if os.path.isfile(f'{self.valor_pesquisa_traco}.csv'):
            count_ = 0
            df = pd.read_csv(f'{self.valor_pesquisa_traco}.csv', sep=';')
            soma = 0
            for i in df['salarios']:
                str_ = str(i)
                str_ = str_.replace("A Combinar", "0").replace("De R$", "").replace("a R$", "").replace(",00", "").replace(
                    ".", "").split()
                for i in str_:
                    i = float(i)
                    soma += i
                    if i > 0:
                        i = 1
                        count_ += i

            return print(f'Media Salarial para o cargo de {self.pesquisa}: {soma / count_} ')
        else:
            AnaliseArquivo(self.pesquisa).GeraArquivo()
            AnaliseArquivo(self.pesquisa).MediaSalarial()



