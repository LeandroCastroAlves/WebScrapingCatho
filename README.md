# skills-find
 
 A classe PesquisaDados tem que receber a pesquisa na forma de uma string, feito isso há varios métodos para realizar como buscar os salarios, descrições, descrção curta, link direto, descrição completa, quantidade de vagas e localizacao da vaga, ambos com retorno de um Data Frame do Pandas.

 A classe AnaliseArquivo tambem precisa da string de pesquisa como AnalisaArquivo("engenheiro de dados").Metodo(). Nesta classe Há dois metodos. GeraArquivoCsv() gera um arquivo csv de 6 colunas que são: Data da publicação da vaga, nome, localização, salario(médio caso houver um intervalo), descrição curta e link direto. GeraDf() faz a mesma coisa que o método anterior só que não salva estes dados em um csv

 A classe EstatisticasWeb() Traz alguns métodos de estatisticas mas com input direto de Data Frames Pandas vindos da WEB enquanto a classe EstatisticasArquivo() traz essas estatisticas do arquivo csv baixado formatado atravez da classe GeraArquivoCsv().
 
 GeraArquivoCsv funciona com Threads e isso faz com que a geração do arquivo sera bem rapido.

# Ex:
```
pesquisa = "gerente farmaceutico"
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
```
