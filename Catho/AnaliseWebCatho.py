from Catho.GeraArquivoCsvCatho import AnaliseArquivo

class EstatisticasWeb():

    def __init__(self, pesquisa):
        df = AnaliseArquivo(pesquisa).GeraDf()
        self.df = df

    def df_salario_full(self):
        df_fil_sal = self.df['salario'] > 0
        df_sal_full = self.df[df_fil_sal]
        print(df_sal_full)

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


