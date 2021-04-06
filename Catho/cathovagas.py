import os
from PesquisaDadosCatho import DadosPesquisa
from GeraArquivoCsvCatho import AnaliseArquivo
from AnaliseArquivoCsvCatho import EstatisticasArquivo



# altere isso para sua pesquisa
pesquisa = "gerente farmaceutico"
# fim pesquisa

FormataPesquisa = DadosPesquisa(pesquisa).valor_pesquisa_traco
arquivo = f"Catho/{FormataPesquisa}.csv"

def info(arquivo=arquivo):
    print(EstatisticasArquivo(arquivo).MediaGeral())
    print(EstatisticasArquivo(arquivo).SalarioPorCidade())
    print(EstatisticasArquivo(arquivo).SalarioPorRegiao())

if not os.path.isfile(arquivo):
    AnaliseArquivo(pesquisa).GeraArquivoCsv()
    info()
else:
    info()














