import pandas as panda
import matplotlib.pyplot as plot

file = "https://raw.githubusercontent.com/rafaelmm82/ufpb-ia-20201/master/02-fundamentos_de_ia/02_aula_pratica_classificacao_iris/iris.csv"
dataset = panda.read_csv(file, header=0)


panda.plotting.scatter_matrix(dataset)
plot.show()