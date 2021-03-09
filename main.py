import os
import pandas as pd
import csv

a = csv.reader("desenvolvedor_java.csv") # cheio
b = open("compras.csv") # vazio
b = csv.reader(b)
a = list(a)

print(a)
print(b)
if len(a) == 0:
    print("zero")
else:
    print("nao zero")
# verfica o B
if len(b) == 0:
    print("zero")
else:
    print("nao zero")