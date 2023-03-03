import pandas as pd
import matplotlib.pyplot as plt

#create plot function to display line, dispersion and histogram from data using subplot
def plotValues(df, column):
    #create subplot
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    #plot line
    ax[0].plot(df[column])
    ax[0].set_title('Linea')
    #plot dispersion
    ax[1].scatter(df.index, df[column])
    ax[1].set_title('Dispersion')
    #plot histogram
    ax[2].hist(df[column])
    ax[2].set_title('Histograma')
#read csv file

#######################
#######################
#SCRIPT FOR BTCOAL_MAX# 
#######################
#######################

df = pd.read_csv("BTC_Footprints_v1.csv")

#calculate mean, median and mode
media = df["BTCOAL_MAX"].mean()
mediana = df["BTCOAL_MAX"].median()
moda = df["BTCOAL_MAX"].mode()
print("""
    Media: %f
    Mediana: %f
    Moda: %f
""" % (media,mediana,moda))
#calculate range, variance and standard deviation
rango = df["BTCOAL_MAX"].max() - df["BTCOAL_MAX"].min()
var = df["BTCOAL_MAX"].var(ddof=0)
std = df["BTCOAL_MAX"].std(ddof=0)
print("""
    Rango: %f
    Varianza: %f
    Desviación Estándar: %f
""" % (rango,var,std))
#calculate coefficient of variation
cv = df["BTCOAL_MAX"].std(ddof=0) / df["BTCOAL_MAX"].mean() * 100
print("""
    CV: %f
""" % (cv))

#call plot function
plotValues(df, "BTCOAL_MAX")

#show plot
plt.show()