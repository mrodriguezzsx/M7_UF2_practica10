import pandas as pd
import matplotlib.pyplot as plt

def casosTotals():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_a.csv')

    # La dades de la Columna 'date' la pasem a numeros (1 = Gener, 2 = Febrer...) amb la funcio to_date() i fem que els casos totals es sumin
    # amb els messos respectius
    dadesAgrupades = dades.groupby(['location', pd.to_datetime(dades['date']).dt.month])['total_cases'].sum()

    # Agafem 10 Localitats o Ciutats
    location10 = dadesAgrupades.groupby('location').sum().nlargest(10).index

    # Bucle per iterar tots les Ciutats
    for pais in location10:
        casos = dadesAgrupades[pais]
        plt.plot(casos.index, casos.values, label=pais)

    # Decorem el grafic
    plt.title("Casos por mes - 10 ciutats principals")
    plt.xlabel("Messos")
    plt.ylabel('Casos')
    plt.legend()
    print()
    return plt.show()

def mortsTotals():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_a.csv')

    # La dades de la Columna 'date' la pasem a numeros (1 = Gener, 2 = Febrer...) amb la funcio to_date() i fem que els casos totals es sumin
    # amb els messos respectius
    dadesAgrupades = dades.groupby(['location', pd.to_datetime(dades['date']).dt.month])['total_deaths'].sum()

    # Agafem 10 Localitats o Ciutats
    location10 = dadesAgrupades.groupby('location').sum().nlargest(10).index

    # Bucle per iterar tots les Ciutats
    for pais in location10:
        casos = dadesAgrupades[pais]
        plt.plot(casos.index, casos.values, label=pais)

    # Decorem el grafic
    plt.title("Tasa de mortalitat per mes - 10 ciutats principals")
    plt.xlabel("Messos")
    plt.ylabel('Morts')
    plt.legend()
    print()
    return plt.show()










