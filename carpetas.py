import pandas as pd
import pyodbc
import sqlalchemy

import os
import unicodedata
import shutil

def update():
    estructura()
    # folder()

def folder():
    palta = pd.read_csv("paltas3.csv")
    fuente = "220101001cupos__concejales_test__maranon.png"

    ruta = "test/"
    valor = "carpeta1"
    rutaFinal = ruta + valor

    os.mkdir(rutaFinal)

    destino = rutaFinal + "/palta.png"
    shutil.copyfile(fuente, destino)

def generarRuta(texto):
    aux = texto.lower()
    aux = unicodedata.normalize("NFKD", aux).encode("ascii","ignore").decode("ascii") # ***
    return aux.replace(" ","_")

def IntToString(numero):
    return str(numero)

def estructura():
    palta = pd.read_csv("paltas3.csv")
    fuente = "220101001cupos__concejales_test__maranon.png"

    carpetas = ['Datos', 'Image']

    for i in carpetas:
        print(i)
        
        carpeta = i

        conection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=sud-austral.database.windows.net;Database=graficos;uid=sudaustral;pwd=Sud123456789")
        cursor = conection.cursor()

        query = "SELECT * FROM INDUSTRIA"
        df = pd.read_sql(query, conection)

        query = "SELECT * FROM INDUSTRIA"
        df = pd.read_sql(query, conection)
        df["ruta"] = df["nombre"].apply(generarRuta)
        df["id2"] = df["id"].apply(IntToString)
        df["ruta"] = df["id2"] + df["ruta"]

        ruta = str(carpeta) + "/"

        # print(" ------------ NIVEL 1 ------------ ")
        for i in range(len(df)):
            #ruta = "D:/GitHub/MPG/Datos/" + df["ruta"][i]
            ruta = str(carpeta) + "/" + df["ruta"][i]
            # print(df["ruta"][i])

            if os.path.isdir(ruta):
                # print('La carpeta ' + ruta + ' existe.');
                pass
            else:

                try:
                    os.mkdir(ruta)

                    destino = ruta + "/palta.png"
                    shutil.copyfile(fuente, destino)

                except:
                    pass
            query = "SELECT * FROM SECTOR WHERE INDUSTRIA_id = " + str(df["id"][i])
            df2 = pd.read_sql(query, conection)
            df2["ruta"] = df2["nombre"].apply(generarRuta)
            df2["id2"] = df2["id"].apply(IntToString)
            df2["ruta"] = df2["id2"] + df2["ruta"]

            # print(" ------------ NIVEL 2 ------------ ")

            for j in range(len(df2["ruta"])):
                try:
                    ruta2 = ruta + "/" + df2["ruta"][j]
                    # print(ruta2)
                    if os.path.isdir(ruta2):
                        # print('La carpeta ' + ruta2 + ' existe.');
                        pass
                    else:
                        try:
                            os.mkdir(ruta2)

                            destino = ruta2 + "/palta.png"
                            shutil.copyfile(fuente, destino)

                        except:
                            pass
                    query = "SELECT * FROM PRODUCTO WHERE SECTOR_id = " + str(df2["id"][j])
                    df3 = pd.read_sql(query, conection)
                    df3["ruta"] = df3["nombre"].apply(generarRuta)
                    df3["id2"] = df3["id"].apply(IntToString)
                    df3["ruta"] = df3["id2"] + df3["ruta"]

                    # print(" ------------ NIVEL 3 ------------ ")

                    for k in range(len(df3["ruta"])):
                        try:
                            ruta3 = ruta2 + "/" + df3["ruta"][k]
                            # print(ruta3)

                            if os.path.isdir(ruta3):
                                # print('La carpeta ' + ruta3 + ' existe.');
                                pass
                            else:

                                try:
                                    os.mkdir(ruta3)

                                    destino = ruta3 + "/palta.png"
                                    shutil.copyfile(fuente, destino)

                                except:
                                    pass
                            query = "SELECT * FROM CATEGORIA WHERE PRODUCTO_id = " + str(df3["id"][k])
                            df4 = pd.read_sql(query, conection)
                            df4["ruta"] = df4["nombre"].apply(generarRuta)
                            df4["id2"] = df4["id"].apply(IntToString)
                            df4["ruta"] = df4["id2"] + df4["ruta"]

                            # print(" ------------ NIVEL 4 ------------ ")

                            for l in range(len(df4["ruta"])):
                                try:
                                    ruta4 = ruta3 + "/" + df4["ruta"][l]
                                    # print(ruta4)
                                    if os.path.isdir(ruta4):
                                        # print('La carpeta ' + ruta3 + ' existe.');
                                        pass
                                    else:
                                        try:
                                            os.mkdir(ruta4)

                                            destino = ruta4 + "/palta.png"
                                            shutil.copyfile(fuente, destino)
                                        except:
                                            pass

                                    destino = ruta4 + "/palta.png"
                                    shutil.copyfile(fuente, destino)
                                    #palta.to_csv(ruta4 + "/palta.csv", index=False)
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass

if __name__ == '__main__':
    print('Empezando proceso ha comenzando.')
    update()
    print('Empezando proceso ha finalizado.')