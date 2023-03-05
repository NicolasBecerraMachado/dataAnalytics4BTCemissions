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
#SCRIPT FOR BTCGAS_GUE# 
#######################
#######################

df = pd.read_csv("BTC_Footprints_v1.csv")

#calculate mean, median and mode
media = df["BTCGAS_GUE"].mean()
mediana = df["BTCGAS_GUE"].median()
moda = df["BTCGAS_GUE"].mode()
print("""
    Media: %f
    Mediana: %f
    Moda: %f
""" % (media,mediana,moda))
#calculate range, variance and standard deviation
rango = df["BTCGAS_GUE"].max() - df["BTCGAS_GUE"].min()
var = df["BTCGAS_GUE"].var(ddof=0)
std = df["BTCGAS_GUE"].std(ddof=0)
print("""
    Rango: %f
    Varianza: %f
    Desviación Estándar: %f
""" % (rango,var,std))
#calculate coefficient of variation
cv = df["BTCGAS_GUE"].std(ddof=0) / df["BTCGAS_GUE"].mean() * 100
print("""
    CV: %f
""" % (cv))

#call plot function
plotValues(df, "BTCGAS_GUE")

#show plot
plt.show()

# for data analysis refer to 
#    BTC C02 emissions.pptx
