import requests
from bs4 import BeautifulSoup
import pandas as pd



def i():
    df = pd.read_csv('engenheiro-de-dados.csv', sep=";")
    j = []
    for i in df['estado']:
        print(i.split()[0])
        j.append(i.split()[0])
    dfJ = pd.DataFrame(j)
    df['estado'] = dfJ
    print(df['estado'].values)
    df.to_csv('engenheiro-de-dados.csv', index=None)

df = pd.read_csv('engenheiro-de-dados.csv')
df = df.rename({'Unnamed: 0': 'id'})
print(df)



go.Scatter(x=list(i['salariomedia']), y=list(i['estado']),
                   mode='lines',
                   name='Gráfico com linhas tracejadas',
                   )