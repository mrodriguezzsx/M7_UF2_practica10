import pandas as pd
import matplotlib.pyplot as plt

def casosTotals():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_a.csv', usecols=['location', 'date', "total_cases"])

    # Passem les dates a format datetime, i transformem els valors en nomes el mes
    dades['date'] = pd.to_datetime(dades.date).dt.month

    # Agrupen les dades en localitzacio i data. Les sumem i fem unstack(No se que fa)
    dadesAgrupades = dades.groupby(by=['date', 'location']).sum().unstack()

    # Seleccionem les primeres 10 columnes (No se com fer-ho aleatori)
    columnas_seleccionadas = dadesAgrupades.iloc[:, :10]
    print(columnas_seleccionadas.to_string(index=False))

    columnas_seleccionadas.plot()
    plt.xlabel("Mes")
    plt.ylabel('Casos')
    plt.legend(['Casos Totals x Mes'])
    print()
    return plt.show()

def mortsTotals():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_a.csv', usecols=['location', 'date', "total_deaths"])

    # Passem les dates a format datetime, i transformem els valors en nomes el mes
    dades['date'] = pd.to_datetime(dades.date).dt.month

    # Agrupen les dades en localitzacio i data. Les sumem i fem unstack(No se que fa)
    dadesAgrupades = dades.groupby(by=['date', 'location']).sum().unstack()

    # Seleccionem les primeres 10 columnes (No se com fer-ho aleatori)
    columnas_seleccionadas = dadesAgrupades.iloc[:, :10]
    print(columnas_seleccionadas.to_string(index=False))

    columnas_seleccionadas.plot()
    plt.xlabel("Mes")
    plt.ylabel('Morts')
    plt.legend(['Morts Totals x Mes'])
    print()
    return plt.show()









