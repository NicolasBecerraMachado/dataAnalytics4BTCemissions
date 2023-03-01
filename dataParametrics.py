import pandas as pd
import matplotlib.pyplot as plt

#create plot function to display data using subplot
def plotValues(df, column):
    plt.subplot(2, 1, 1)
    plt.plot(df[column])
    plt.title("Gráfico de línea")
    plt.xlabel("Índice")
    plt.ylabel(column)

    plt.subplot(2, 1, 2)
    plt.scatter(df.index, df[column])
    plt.title("Gráfico de dispersión")
    plt.xlabel("Índice")
    plt.ylabel(column)

df = pd.read_csv("BTC_Footprints_v1.csv")

media = df["BTCEMI_MAX"].mean()
mediana = df["BTCEMI_MAX"].median()
moda = df["BTCEMI_MAX"].mode()
print("""
    Media: %f
    Mediana: %f
    Moda: %f
""" % (media,mediana,moda))

rango = df["BTCEMI_MAX"].max() - df["BTCEMI_MAX"].min()
var = df["BTCEMI_MAX"].var(ddof=0)
std = df["BTCEMI_MAX"].std(ddof=0)
print("""
    Rango: %f
    Varianza: %f
    Desviación Estándar: %f
""" % (rango,var,std))

cv = df["BTCEMI_MAX"].std(ddof=0) / df["BTCEMI_MAX"].mean() * 100
print("""
    CV: %f
""" % (cv))

plotValues(df, "BTCEMI_MAX")

plt.show()