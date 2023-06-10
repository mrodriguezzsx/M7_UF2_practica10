import pandas as pd
import matplotlib.pyplot as plt

def velocitatProdessador():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_c.csv', usecols=['id', 'clock_speed'])

    # Agafem els valors necesaris per el grafic
    # He restat 1 numero a cada id ja que al ser una llista comença per 0
    id = [2, 12, 33, 55, 69, 85, 109, 119, 209, 399]

    # Guardem les files per ID
    n = dades.loc[id]
    print(n.to_string(index=False))

    # Creeem la grafica de Barres passant els valors obtinguts
    # Cambiem el color y la mida de les barres
    plt.bar(n.id, n.clock_speed, color="orange", width=8)
    plt.legend(['Velocidades de reloj'])

    # Personalitzo els eixos
    plt.xlabel("ID's")
    plt.ylabel('Cloock Speed')
    print()
    return plt.show()

def megapixels():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_c.csv', usecols=['id', 'px_width'])

    # Agafem els valors necesaris per el grafic
    # He restat 1 numero a cada id ja que al ser una llista comença per 0
    id = [2, 12, 33, 55, 69, 85, 109, 119, 209, 399]

    # Guardem les files per ID
    n = dades.loc[id]
    print(n.to_string(index=False))

    # Creeem la grafica de Barres passant els valors obtinguts
    # Cambiem el color y la mida de les barres
    plt.bar(n.id, n.px_width, color="black", width=8)
    plt.legend(['Megapixeles'])

    # Personalitzo els eixos
    plt.xlabel("ID's")
    plt.ylabel('Pixel width')
    print()
    return plt.show()

def potenciaBateria():
    # Guardem les dades de l'excel en una variable
    dades = pd.read_csv('activitat_c.csv', usecols=['id', 'battery_power'])

    # Agafem els valors necesaris per el grafic
    # He restat 1 numero a cada id ja que al ser una llista comença per 0
    id = [2, 12, 33, 55, 69, 85, 109, 119, 209, 399]

    # Guardem les files per ID
    n = dades.loc[id]
    print(n.to_string(index=False))

    # Creeem la grafica de Barres passant els valors obtinguts
    # Cambiem el color y la mida de les barres
    plt.bar(n.id, n.battery_power, color="green", width=8)
    plt.legend(['Potecia de la Bateria'])

    # Personalitzo els eixos
    plt.xlabel("ID's")
    plt.ylabel('Battery Power')
    print()
    return plt.show()

