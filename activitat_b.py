import pandas as pd
import matplotlib.pyplot as plt

def totalPoblacio():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv("activitat_b.csv", usecols=['City', 'Population'])

    # Eliminem la linae buida de l'arxiu
    dades = dades.dropna()

    # Funcio per a que hagafi 10 resultats aleatoris
    dades = dades.sample(10)
    print(dades)

    # Eliminem les comes de les poblacions ja que sino conta que son decimals
    dades["Population"] = dades["Population"].apply(lambda x : x.replace(',',''))

    plt.pie(dades["Population"], labels=dades['City'], autopct='%1.1f%%')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    return plt.show()

def densitatKM2():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv("activitat_b.csv", usecols=['City', 'Density KM2'])

    # Eliminem la linae buida de l'arxiu
    dades = dades.dropna()

    # Funcio per a que hagafi 10 resultats aleatoris
    dades = dades.sample(10)
    print(dades)

    # Eliminem les comes de les poblacions ja que sino conta que son decimals
    dades["Density KM2"] = dades["Density KM2"].apply(lambda x: x.replace(',', ''))

    plt.pie(dades["Density KM2"], labels=dades['City'], autopct='%1.1f%%')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    return plt.show()

def densitatM2():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv("activitat_b.csv", usecols=['City', 'Density  M2'])

    # Eliminem la linae buida de l'arxiu
    dades = dades.dropna()

    # Funcio per a que hagafi 10 resultats aleatoris
    dades = dades.sample(10)
    print(dades)

    # Eliminem les comes de les poblacions ja que sino conta que son decimals
    dades["Density  M2"] = dades["Density  M2"].apply(lambda x: x.replace(',', ''))

    plt.pie(dades["Density  M2"], labels=dades['City'], autopct='%1.1f%%')
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    return plt.show()