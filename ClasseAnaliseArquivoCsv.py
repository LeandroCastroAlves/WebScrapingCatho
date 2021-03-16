import pandas as pd


class EstatisticasArquivo():

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.df = pd.read_csv(f'{self.arquivo}')


    def df_salario_full(self):
        df_fil_sal = self.df['salario'] > 0
        df_sal_full = self.df[df_fil_sal]
        return df_sal_full

    def SalarioPorRegiao(self):
        df = self.df_salario_full()
        print(df[["estado", "salario"]].groupby("estado").mean())

    def SalarioPorCidade(self):

        df = self.df_salario_full()
        print(df[["cidade", "salario"]].groupby("cidade").mean())
        print(df[['cidade', 'salario']].describe())

    def MediaGeral(self):
        df = self.df_salario_full()
        print(f"\nMédia Geral: {df[['estado', 'salario']].median()}")

    def SalarioMaximo(self):
        df = self.df_salario_full()
        df['salario'].max()





