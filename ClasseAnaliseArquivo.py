import pandas as pd
from ClassePesquisaCargo import PesquisaCargo
import os


class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = PesquisaCargo(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()
    def GeraArquivocsv(self):
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")
        print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')

        return PesquisaCargo(self.pesquisa).PegaDtPubliJob()\
            .join(PesquisaCargo(self.pesquisa).PegaNomeJob())\
            .join(PesquisaCargo(self.pesquisa).PegaLocalizacaoJob())\
            .join(PesquisaCargo(self.pesquisa).PegaSalarioJob())\
            .join(PesquisaCargo(self.pesquisa).PegaDescricaoJob()).to_csv(f'{self.valor_pesquisa_traco}.csv', sep=";")


    def MediaSalarial(self):
        if os.path.isfile(f'{self.valor_pesquisa_traco}.csv'):
            count_ = 0
            df = pd.read_csv(f'{self.valor_pesquisa_traco}.csv', sep=';')
            soma = 0
            for i in df['salarios']:
                str_ = str(i)
                str_ = str_.replace("A Combinar", "0")\
                    .replace("De R$", "")\
                    .replace("a R$", "")\
                    .replace(",00", "") \
                    .replace("Acima de R$ ", "") \
                    .replace("Até R$ ", "") \
                    .replace(".", "").split()
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



