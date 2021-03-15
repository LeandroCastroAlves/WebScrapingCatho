import pandas as pd
import requests
from bs4 import BeautifulSoup
from ClasseDadosPesquisaCatho import DadosPesquisa
import os

class AnaliseArquivo():
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa
        self.encontrados = DadosPesquisa(pesquisa).PegaQtdJob()
        self.valor_pesquisa_traco = pesquisa.replace(" ", "-").replace("ã", "a").replace("ç", "c").replace("é",
                                                                                                           "e").lower()
    def GeraArquivocsv(self):
        cont_int = int(str(self.encontrados).split()[0])
        print(f"Total de anuncios {cont_int}")
        print(f'Por favor aguarde o rastreio das informações, isso pode demorar um pouco...')
        return DadosPesquisa(self.pesquisa).PegaDtPubliJob()\
            .join(DadosPesquisa(self.pesquisa).PegaNomeJob())\
            .join(DadosPesquisa(self.pesquisa).PegaLocalizacaoJob())\
            .join(DadosPesquisa(self.pesquisa).PegaSalarioJob())\
            .join(DadosPesquisa(self.pesquisa).PegaDescricaoJob()) \
            .join(DadosPesquisa(self.pesquisa).PegaLinkJobDataFrame()) \
            .to_csv(f'{self.valor_pesquisa_traco}.csv', sep=";")

    def MediaSalario(self):
        print(f"Vagas encontradas: {DadosPesquisa(self.pesquisa).PegaQtdJob()}")
        df = pd.DataFrame(DadosPesquisa(pesquisa=self.pesquisa).PegaSalarioJob())
        df_fil_sal = df['salario'] > 0
        df_sal_mai_zer = df[df_fil_sal]
        media_salarial = df_sal_mai_zer['salario'].sum() / len(df_sal_mai_zer['salario'])
        print(f"Média para o cargo de {self.pesquisa}: {media_salarial} \n\nObs: Há Várias vagas em que não há salário, e elas foram excluidas do cálculo")






