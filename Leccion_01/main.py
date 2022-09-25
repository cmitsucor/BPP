import pandas as pd
import matplotlib.pyplot as plt
import csv


pd.options.display.float_format = '{:.2f}'.format

df = pd.read_csv('finanzas2020.csv', sep='\t')
# print(df.head())
# print(df.tail())
# print(df.dtypes)


if __name__ == "__main__":

    ### Comprobamos que el fichero existe y se puede abrir ###

    try:
        with open('finanzas2020.csv', 'r') as csvfile:
            csv_dict = [row for row in csv.DictReader(csvfile)]
            if len(csv_dict) == 0:
                print('csv file is empty')
    except IOError:
        print("No se encuentra el fichero")
    else:
        print("El archivo contiene algo")

    ### Comprobamos que el fichero tiene 12 columnas y que tenemos contenido para cada columna ###

    try:
        if df.shape[1] != 12:
            print("El archivo no contiene las columnas disponibles para cada mes")
    except Exception as e:
        print("Ha habido una excepción", e)
    else:
        print("El archivo contiene datos disponibles.")
    finally:
        if df.shape[0] == 0:
            print("No hay datos")

    ### Modificamos las columnas para que todas tengan elementos correctos ###
    Ener = df["Enero"]

    extr = df["Enero"].str.extract(
        r'^(\-\d+|\d+)$', expand=False)                     # extraemos los valores de
    Eneralista = extr.tolist()                              # pasamos a lista

    # si no es float lo reemplazamos por "0"
    ints = [i for i in Eneralista if type(i) is not float]

    b = 0
    for i in range(len(df["Enero"])-len(ints)):
        ints.append(b)

    # pasamos los valores a ints
    res = [int(float((i))) for i in ints]

    df["Enero"] = res  # reescribimos el df del mes

    Jul = df["Julio"]

    extr = df["Julio"].str.extract(r'^(\-\d+|\d+)$', expand=False)
    Eneralista = extr.tolist()
    ints = [i for i in Eneralista if type(i) is not float]

    b = 0
    for i in range(len(df["Julio"])-len(ints)):
        ints.append(b)

    res = [int(float((i))) for i in ints]

    df["Julio"] = res

    Sep = df["Septiembre"]

    extr = df["Septiembre"].str.extract(r'^(\-\d+|\d+)$', expand=False)
    Eneralista = extr.tolist()
    ints = [i for i in Eneralista if type(i) is not float]

    b = 0
    for i in range(len(df["Septiembre"])-len(ints)):
        ints.append(b)

    res = [int(float((i))) for i in ints]

    df["Septiembre"] = res

    Octu = df["Octubre"]

    extr = df["Octubre"].str.extract(r'^(\-\d+|\d+)$', expand=False)
    Eneralista = extr.tolist()
    ints = [i for i in Eneralista if type(i) is not float]

    b = 0
    for i in range(len(df["Octubre"])-len(ints)):
        ints.append(b)

    res = [int(float((i))) for i in ints]

    df["Octubre"] = res

    Nob = df["Noviembre"]

    extr = df["Noviembre"].str.extract(r'^(\-\d+|\d+)$', expand=False)
    Eneralista = extr.tolist()
    ints = [i for i in Eneralista if type(i) is not float]

    b = 0
    for i in range(len(df["Noviembre"])-len(ints)):
        ints.append(b)

    res = [int(float((i))) for i in ints]

    df["Noviembre"] = res

    ## extremos todos los valores negativos para todos los meses ##

    min_value = None

    negativo = df.mul(~df.gt(0)).sum()
    myList = []
    for key, value in negativo.items():
        if (min_value is None or value < min_value):
            myList.append([key, value])
            min_v = min(myList, key=lambda x: x[1])
    print(
        f'\nEl mes de {min_v[0]} fue el de mayor gasto, con un total de {min_v[1]}')

    ## extremos todos los valores positivos para todos los meses ##

    max_value = None

    positivo = df.mul(df.gt(0)).sum()
    myList1 = []
    for key, value in positivo.items():
        if (max_value is None or value > max_value):
            myList1.append([key, value])
            max_v = max(myList1, key=lambda x: x[1])
    print(
        f'\nEl mes de {max_v[0]} fue el de mayor ahorro, con un total de {max_v[1]}')

    # obtenemos la media del df
    media_ = (df.mul(~df.gt(0)).sum().mean())
    print(f'\nLa media de gastos del año es: {media_}')

    # obtenemos los gastos totales del año
    negativo = df.mul(~df.gt(0)).sum().sum()
    print(f'\nLos gastos totales a lo largo del año han sido: {negativo}')

    # obtenemos los ingresos totales del año

    positivo = df.mul(df.gt(0)).sum().sum()
    print(f'\nLos ingresos totales a lo largo del año han sido: {positivo}')

    df4 = df.sum().sum()
    print(f'\nEl balance total del año es: {df4}\n')

    # Imprimimos una grafica de barras de la variacion de los ingresos del año

    df5 = pd.DataFrame(myList1)
    plt.figure(figsize=(14, 7))
    plt.bar(df5[0], df5[1])

    plt.ylabel("Ingresos\n", fontsize=15)
    plt.xlabel("Meses\n", fontsize=15)
    plt.xticks(rotation=45)

    plt.title('Gráfica de la variación de los ingreso durante el año\n', fontsize=20)
    plt.subplots_adjust(top=0.888,
                        bottom=0.199,
                        left=0.121,
                        right=0.984,
                        hspace=0.2,
                        wspace=0.2)
    plt.savefig("Plot generated using Matplotlib.png")
    plt.show()
