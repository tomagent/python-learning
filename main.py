import pandas as pd #se manda a llamar a la librería pandas que permite leer, modificar y escribir datos en base de datos, nosotros la utilizamos para abrir el csv
from matplotlib import pyplot as plt # se manda a llamar la librería que nos ayuda a crear gráficos
from collections import Counter # importar la subclase Counter que permite sacar los valores más frecuentes
import numpy as np #llama a la librería que permite generar un cálculo numérico de una base de números extensa
from time import sleep # importar función para darle pausas al programa

# Leer Datos y Limpiar Filas Vacias
df = pd.read_csv("KICKSTARTER_JULIO2020.csv")
df = df.dropna() #limpia las filas vacías de la base de datos

# Dimensiones de la base de datos
print(f"La base de datos a analizar tiene las siguientes medidas: {df.shape[0]} filas y {df.shape[1]} columnas")

# Renombrar encabezados de base de datos
df = df.rename(columns={"name": "nombre", "currency": "divisa", "launched_at":"lanzado_en", "blurb":"titulo",
                   "country": "pais", "deadline": "fecha_limite", "status": "estatus", "usd_pledged": "usd_invertidos",
                   "sub_category": "sub_categoria", "main_category": "categoria_principal",
                   "blurb_length": "longitud_titulo", "goal_usd": "meta_usd", "city": "ciudad", "duration": "duracion",
                   "backers_count": "conteo_inversionistas"})


# Verificar que no haya valores vacíos, esto nos permitirá no tener ningún error durante la ejecución de la base de datos
print(df.isnull().sum())
sleep(5)
# Datos generales de la base de datos
print("Estadisticas de la base de datos", df.describe(), sep="\n")

# Reemplazar datos en inglés, esto nos permitirá tener una mayor comprensión de los datos de nuestra base
df = df.replace(["successful", "failed"], ["exitoso", "fallido"])

# Cambiar tamaño de gráfica, nos permitirá tener un mejor diseño
def cambia_tamaño(anchura, altura):
    """Cambia el tamaño de la gráfica"""
    f = plt.figure()
    f.set_figwidth(anchura)
    f.set_figheight(altura)
    return f

# ¿Cuáles fueron los proyectos más exitosos en Julio 2020?
def proyectos_exitosos(style):
    """Gráfica de los 10 proyectos que recibieron más inversion en Julio 2020"""

    # En esta gráfica comenzamos a recopilar los datos de los proyectos que más éxito tuvieron, es decir, más inversión
    plt.style.use(style)
    # Los 10 proyectos que recibieron más inversión - Thomas
    proyectos = df[df["estatus"] == "exitoso"].sort_values(by="usd_invertidos", ascending=True).tail(10)
    proyectos_nombres = proyectos["nombre"].str[:18] # Deja los primeros 18 caracteres de cada proyecto
    # cambiar tamaño
    f = cambia_tamaño(20,8)
    # crear gráfica,
    plt.barh(proyectos_nombres, proyectos["usd_invertidos"], color="lightblue", linestyle="--")
    plt.title("Los 10 emprendimientos que recibieron más inversión en Kickstarter Julio 2020, a nivel mundial")
    plt.xlabel("Dinero recibido en mdd")
    plt.savefig("10_emprendimientos_mas_inversion.png")
    plt.show()

def preparar_base(df, agrupa, inversion):
    """Prepara la base de datos para sumar la inversion"""

    # Inicializamos diccionario vacio
    dict = {}
    # Iterar por todas las filas, y sacar el indice de cada fila
    for i in df.index:
        # Crea una nueva variable y le dices en que lo te va a agrupar
        c = df[agrupa][i] # i = 0 1 2 3 4 5 6 ... len(df["name"])
        if c not in dict: # Si esta clave no esta en el dicccionario
            dict[c] = 0 # Inicializa en 0
        dict[c] += df[inversion][i] # Sumarlo
    return dict

# ¿Cuáles fueron las categorías de emprendimientos que recibieron más inversión?
def categorias_exitosas(style):
    """Gráfica de las categorías mas populares"""

    plt.style.use(style)
    # Se espera recopilar las categorías que mas llamaron la atención de los inversionistas,
    # por lo cual tuvieron un acaudalado apoyo
    categorias = preparar_base(df, "categoria_principal", "usd_invertidos")
    categorias_populares = dict(Counter(categorias).most_common(5))
    categoria, dinero = zip(*categorias_populares.items())
    # cambiar tamaño
    f = cambia_tamaño(15,8)
    # Graficas
    plt.bar(categoria, dinero, color="turquoise", width=0.4, label="inversión por categorías en Kickstarter")
    plt.xlabel("Categorias")
    plt.ylabel("Inversión en decenas de mdd")
    plt.legend()
    plt.title("Las 5 categorias de emprendimientos que recibieron más inversion en Kickstarter durante Julio 2020")
    plt.savefig("5_categorias_mas_inversion.png")
    plt.show()


# ¿Que ciudades recibieron más inversión durante Julio 2020 en Kickstarter?
def ciudades_populares(style):
    """Gráfica de las ciudades a nivel mundial que recibieron mayor inversión"""

    plt.style.use(style)
    # Ciudades populares
    ciudades = preparar_base(df, "ciudad", "usd_invertidos")
    ciudades_populares = dict(Counter(ciudades).most_common(25)) # top 25
    ciudad, dinero = zip(*ciudades_populares.items()) # tupla para ciudad, dinero
    # cambiar tamaño
    f = cambia_tamaño(15, 8)
    # Grafica
    ciudad = list(ciudad)
    dinero = list(dinero)
    ciudad.reverse()
    dinero.reverse()
    plt.barh(ciudad, dinero, color="lime", label="inversion por ciudades en Kickstarter")
    plt.title("Inversión de proyectos por ciudades en Kickstarter durante Julio 2020, a nivel mundial")
    plt.xlabel("Inversión en mdd")
    plt.ylabel("Ciudades")
    plt.legend()
    plt.savefig("ciudades_inversion.png")
    plt.show()

# ¿Que países recibieron más inversión en Kickstarter?
def paises_populares(style):
    """Gráfica de los paises que recibieron mayor inversión"""

    plt.style.use(style)
    # Paises populares
    paises = preparar_base(df, "pais", "usd_invertidos") # agrupar datos de inversión por país
    pais, dinero = zip(*paises.items())
    # cambiar tamaño
    f = cambia_tamaño(15, 8)
    # Grafica
    plt.plot(pais, dinero, color="orangered", marker="D", label="inversión en Kickstarter por paises")
    plt.xlabel("Paises")
    plt.ylabel("Inversión en decenas de mdd")
    plt.legend()
    plt.title("Inversión en proyectos por paises en Kickstarter durante Julio 2020")
    plt.savefig("paises_inversion.png")
    plt.show()


def mexico():
    """Esta función limpia la base de datos para dejar solo los de mexico"""

    ciudades_mexicanas = df[df["pais"] == "MX"]
    ciudades = preparar_base(ciudades_mexicanas, "ciudad", "usd_invertidos")
    ciudades["Estado de Mexico"] += ciudades["Mexico"] + ciudades["MÃ©xico"]
    del ciudades['Mexico']
    del ciudades["MÃ©xico"]
    ciudades["Ciudad de México"] = ciudades["Mexico City"]
    del ciudades["Mexico City"]
    del ciudades["Los Angeles"]
    return ciudades

# Inversión total en ciudades mexicanas en Kickstarter Julio 2020
def ciudades_mexicanas(style):
    """Ciudades mexicanas"""

    plt.style.use(style)
    ciudades = mexico()
    ciudades["Garza García"] = ciudades['Garza GarcÃ\xada']
    del ciudades['Garza GarcÃ\xada']
    ciudades = dict(Counter(ciudades).most_common(10))
    ciudad, inversion = zip(*ciudades.items())
    # Cambiar tamaño
    f = cambia_tamaño(15, 8)
    # Crear grafica
    plt.bar(ciudad, inversion, color="mediumpurple", width=0.8, label="inversión de crowdfunding en ciudad mexicanas")
    plt.title("Inversión en proyectos de ciudades mexicanas durante Julio 2020 en Kickstarter")
    plt.ylabel("Inversión en dólares")
    plt.legend()
    plt.savefig("10_ciudades_mexicanas_mas_inversion1.png")
    plt.show()


# ¿Cómo se comporto el mercado mexicano en Kickstarter Julio 2020?
def ciudades_mexicanas_5():
    """5 Ciudades mexicanas"""

    ciudades = mexico()
    ciudades["Garza García"] = ciudades['Garza GarcÃ\xada']
    del ciudades['Garza GarcÃ\xada']
    ciudades_5 = dict(Counter(ciudades).most_common(5))
    ciudad, inversion = zip(*ciudades_5.items())
    colors = ["#FF8D33", "#FF3B33", "#FFD433", "#CCFF33","#33FFD6"]
    explode = [0.1, 0, 0, 0, 0]

    # Grafica
    plt.pie(inversion, labels=ciudad, wedgeprops={"edgecolor": "black"}, explode=explode, colors=colors,
            autopct="%0.1f%%", startangle= 90, shadow=True)

    # Dar estilo de dona
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Circle
    plt.axis('equal')
    plt.title("Inversión en mercado mexicano en Kickstarter durante Julio 2020")
    plt.savefig("5_ciudades_mexicanas_mas_inversion.png")
    plt.show()


def main():
    """Programa"""
    while True:
        opcion = input("Si deseas ver gráficas sobre Kickstarter pulsa 'G', para estadisticos curiosos pulsa 'E', para salir 'S' ").strip().lower()
        if opcion == "g":
            # Graficas
            print("Graficas")
            sleep(5)
            ciudades_mexicanas_5()
            sleep(3)
            proyectos_exitosos("seaborn")
            sleep(3)
            ciudades_mexicanas("ggplot")
            sleep(3)
            paises_populares("fivethirtyeight")
            sleep(3)
            ciudades_populares("seaborn")
            sleep(3)
            categorias_exitosas("fivethirtyeight")
            sleep(3)
        elif opcion == "e":
            # Estadisticos
            print("Estadisticos")
            sleep(5)

            # Contar todos los proyectos cuyo pais es Mexico
            print("Los emprendimientos mexicanos en Kickstarter durante el mes de Julio 2020 fueron: {}".format
                  (len(df[df["pais"] == "MX"])))
            sleep(5)

            # Saca la media/promedio de los dolares invertidos en proyectos cuya categoria es Product Design y lo redondea
            print("Un proyecto de la categoría de Product Design levanto, en promedio, ${} dólares, en Kickstarter, "
                  "durante Julio 2020".format(round(df[df["categoria_principal"] == "Product Design"]["usd_invertidos"].mean()),2))
            sleep(5)

            # Cuenta todos los proyectos (total)
            print("En julio 2020, {} emprendimientos pidieron inversión por Kickstarter".format(df["nombre"].count()))
            sleep(5)

            # Divide el total de proyectos cuyo estado es exitoso entre todos los proyectos y lo multiplica por 100, y lo redondea
            print("En julio 2020 hubo una tasa de exito de {}% para conseguir inversión en Kickstarter".format
                  (round((len(df[df["estatus"] == "exitoso"])/len(df["estatus"]))*100), 2))
            sleep(5)

            # 3 proyectos que levantaron mas inversion
            proyectos = df[df["estatus"] == "exitoso"].sort_values(by="usd_invertidos", ascending=True).tail(3)
            print("Las 3 máximas cantidades que se invirtieron en un proyecto fueron:")
            for inversion in proyectos["usd_invertidos"]:
                print(f"${inversion} dólares") # Imprime los 3 valores mas altos
            sleep(5)

            print("Las 3 ciudades que se recibieron menos inversión para emprendimientos en México durante Julio 2020 fueron:")
            # Agrupar por ciudades mexicanas y almacenar en mexicanas
            mexicanas = mexico()
            # Diccionario con ciudades mexicanas e inversion
            menos_comunes = dict(Counter(mexicanas).most_common()) # Ordenar de mayor a menor las ciudades en un diccionario
            # Regresa una tupla para ciudades, otra para inversion
            ciudad, inversion = zip(*menos_comunes.items())
            for i in range(3): # Itera 3 veces i=0, i=1, i =2
                print(f"{ciudad[(i+1)*-1]}") # Imprime los ultimos 3 valores de la lista de ciudades


        elif opcion == "s":
            print("Gracias")
            exit()
        else:
            print("Opción invalida")


if __name__ == "__main__":
    incorrecto = False
    while not incorrecto: # #Se ejecuta un bloque de instrucciones de manera continua
        print("\nBienvenido al programa")
        # A continuación se pide el usuario y contraseña que se les ha dado previamente a los integrantes del equipo,
        # esto les permitirá entrar a la base de datos, visualizar gráficas y datos.
        usuarios = {"Thomas": 123, "America": 124, "Luis": 125, "Javier": 126, "Jennifer": 127, "Daniel": 128}
        usuario = input("Digite el usuario: ").strip().capitalize()
        contra = int(input("Digite la contraseña: "))
        usuario_encontrado = False
        for usuario in usuarios:
            if contra == usuarios[usuario]:
                print(f"Bienvenid@ {usuario}")
                usuario_encontrado = True
        if not usuario_encontrado:
            print("Usuario o contraseña incorrecto")
            incorrecto = True
        if not incorrecto:
            main() # Llama a funcion principal
            df.to_csv("Base_de_Datos_Depurada.csv", index=False) # Escribe un nuevo csv sin indices