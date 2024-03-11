import pandas as panda
import matplotlib.pyplot as plot

from sklearn.model_selection import train_test_split

file = "https://raw.githubusercontent.com/rafaelmm82/ufpb-ia-20201/master/02-fundamentos_de_ia/02_aula_pratica_classificacao_iris/iris.csv"
dataset = panda.read_csv(file, header=0)



array = dataset.values
print(type(array))
x = array[:, 0:4]
y = array[:, 4]

print ('\n dimensão de X\n', x.shape)
print ('\n dimensão de Y\n', y.shape)