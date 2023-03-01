import pandas as pd
import matplotlib.pyplot as plt

#print(str(pd.__version__))
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


df.describe()
plt.xlabel('year')
plt.ylabel('avg emissions')
df.hist('BTCEMI_MAX')



plt.show()