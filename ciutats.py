import pandas as pd

stats0 = pd.read_csv('List.csv')
stats = pd.DataFrame(stats0)
#Funcio que mostra per ciutat el total de poblacio
def totalPoblacio():
    print(stats[['City','Population']].iloc[3:80])

#Funcio que mostra per ciutat la densitat per KM2
def densitatCiutat():
    print(stats[['City', 'Density KM2']].iloc[3:80])

print(densitatCiutat())
