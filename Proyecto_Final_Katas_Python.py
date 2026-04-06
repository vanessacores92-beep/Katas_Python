# %%
#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(texto):
    """
    Esta función devuelve la frecuencia de cada letra en una cadena de texto

    Args:
         texto (str): cadena de texto
    
    Returns:
        dict: un diccionario con las frecuencias de cada letra sin tener en cuenta los espacios.
    """
    frecuencias = {}
    
    for letra in texto:
        if letra == " ":
            continue  # ignorar espacios
        
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    
    return frecuencias

##Ejemplo de uso
resultado = contar_frecuencias("hola mundo")
print(resultado)


# %%
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

numeros = [5, 9, 45, 33, 87]

dobles = list(map(lambda x: x * 2, numeros))

print(dobles)

# %%
#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista, objetivo):
    """
    Esta función encuentra las palabras que contengan la palabra objetivo

    Args:
         lista (list): lista de palabras
         objetivo (str): palabra objetivo
    
    Returns:
         list: Una lista con todas las palabras que contienen la palabra objetivo.
    """
    resultado = []
    
    for palabra in lista:
        if objetivo in palabra:
            resultado.append(palabra)
    
    return resultado

##Ejemplo de uso
palabras = ["casa", "casamiento", "perro", "casual", "gato", "casandra"]

print(filtrar_palabras(palabras, "casa"))

# %%
#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    """
    Esta función calcula la diferecia entre los números de dos listas

    Args:
         lista 1 (list): lista de números enteros
         lista 2 (list): lista de números enteros
    
    Returns:
         (list): La diferencia entre los valores de la lista1 y la lista2 
    """
    return list(map(lambda x, y: x - y, lista1, lista2))

##Ejemplo de uso
lista1 = [5, 9, 45, 33, 87]
lista2 = [1, 2, 27, 14, 54]

print(diferencia_listas(lista1, lista2))


# %%
#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

def evaluar_notas(numeros, nota_aprobado=5):
    """
    Esta función resuelve si la media de una lista de números dada es mayor o igual que la nota aprobado

    Args:
         numeros (list): lista de números enteros
         nota_aprobado (int): nota de aprobado

    Returns:
         (tuple): Una tupla que contiene la media de la lista de números enteros y el estado
    """
    media = sum(numeros) / len(numeros)
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return (media, estado)

##Ejemplo de uso
notas = [6, 7, 5, 8, 4]

print(evaluar_notas(notas))


# %%
#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    """
    Esta función calcula el factorial de un número de manera recursiva

    Args:
         n: número entero

    Returns:
         (int): factorial del número entero dado
    """
    if n == 0:
        return 1
    else:
        resultado = n * factorial(n - 1)
        print(resultado)  # imprime el valor después de multiplicar
        return resultado

##Ejemplo de uso
numero = 5
factorial(numero)


# %%
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    """
    Esta función convierte una lista de tuplas en una lista de strings.

    Args:
         lista_tuplas: serie de tuplas
    
    Returns:
         (list): lista de strings
    """
    return list(map(str, lista_tuplas))

##Ejemplo de uso
tuplas = [("hola maria"), ("buenos días"), ("katas python")]
resultado = tuplas_a_strings(tuplas)
print(resultado)


# %%
#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

def dividir_numeros():
    """
    Esta función pide al usuario ingresar dos números para poder dividirlos

    Args:
         (int): números enteros
         (float): números con decimales
    
    Returns:
         (int): resultado sin decimales
         (float): resultado con decimales
         (error): si los valores ingresados no son válidos
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"¡División exitosa! El resultado es {resultado}")

# Ejecutar la función
dividir_numeros()


# %%
#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    """
     Elimina mascotas prohibidas de una lista.

    Args:
         lista (list): Lista de nombres de mascotas.

    Returns:
         (list): Lista filtrada sin mascotas prohibidas.
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    resultado = filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)
    
    return list(resultado)

##Ejemplo de uso
mis_mascotas = ["Perro", "Gato", "Mapache", "Cocodrilo", "Conejo"]

resultado = filtrar_mascotas(mis_mascotas)
print(resultado)
    

# %%
#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """
     Calcula el promedio de una lista.

    Args:
        lista (list): Lista de números.

    Returns:
        float: Promedio de la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """
    pass

def promedio_lista(lista):
    if len(lista) == 0:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    
    return sum(lista) / len(lista)

# Uso con manejo de errores
try:
    numeros = []  
    resultado = promedio_lista(numeros)
except ListaVaciaError as e:
    print(f"Error: {e}")
else:
    print(f"El promedio es {resultado}")


# %%
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.

def pedir_edad():
    """
      Solicita al usuario una edad y valida que sea un número dentro del rango permitido.

    Returns:
        None: Muestra un mensaje indicando si la edad es válida o no.
    """
    try:
        edad = int(input("Introduce tu edad: "))
        
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera del rango permitido (0-120).")
            
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Edad ingresada correctamente: {edad}")

# Ejecutar la función
pedir_edad()


# %%
#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    """
     Calcula la longitud de cada palabra en una frase.

    Args:
         frase (str): Texto de entrada.

    Returns:
         (list): Lista con la longitud de cada palabra.
    """
    palabras = frase.split()  
    return list(map(len, palabras))  

##Ejemplo de uso
frase = "Python es muy divertido"
resultado = longitudes_palabras(frase)
print(resultado)


# %%
#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayus_minus_tuplas(conjunto):
    """
      Genera una lista de tuplas con cada letra en mayúscula y minúscula, sin repetir.

    Args:
         texto (str): Conjunto de caracteres.

    Returns:
         (list): Lista de tuplas (mayúscula, minúscula).
    """
    lista = []
    for c in conjunto:
        lista.append((c.upper(), c.lower()))
    return lista
##Ejemplo de uso
letras = {'a', 'n', 'h', 'f', 'v'}
resultado = mayus_minus_tuplas(letras)
print(resultado)


# %%
#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def filtrar_por_letra(lista_palabras, letra):
    """
     Filtra palabras que comienzan con una letra específica.

    Args:
         lista (list): Lista de palabras.
         letra (str): Letra inicial.

    Returns:
         (list): Palabras que empiezan por la letra indicada.
    """
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))
##Ejemplo de uso
palabras = ["manzana", "mango", "pera", "melon", "banana"]
resultado = filtrar_por_letra(palabras, "m")
print(resultado)


# %%
#15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))
"""
 Suma 3 a cada número de una lista.

    Args:
         lista (list): Lista de números.

    Returns:
         (list): Nueva lista con los valores incrementados.
"""

##Ejemplo de uso
numeros = [15, 28, 33, 49]
resultado = sumar_tres(numeros)
print(resultado)


# %%
#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto, n):
    """
      Devuelve palabras cuya longitud es mayor que un valor dado.

    Args:
         frase (str): Texto de entrada.
         n (int): Longitud mínima.

    Returns:
         (list): Palabras que superan esa longitud.
    """
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

##Ejemplo de uso
frase = "Python es un lenguaje de programación muy potente"
resultado = palabras_largas(frase, 4)
print(resultado)


# %%
#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(lista):
    """
      Convierte una lista de dígitos en un número entero.

    Args:
         lista (list): Lista de dígitos.

    Returns:
         (int): Número formado por los dígitos.
    """
    return reduce(lambda acc, x: acc * 10 + x, lista)

##Ejemplo de uso
numeros = [4, 9, 3]
resultado = lista_a_numero(numeros)
print(resultado)


# %%
#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()

def filtrar_estudiantes(estudiantes):
    """
    Filtra estudiantes con calificación mayor o igual a 90.

    Args:
         estudiantes (list): Lista de diccionarios con datos de estudiantes.

    Returns:
         (list): Estudiantes destacados.
    """
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

##Ejemplo de uso
estudiantes = [
    {"nombre": "Luisa", "edad": 20, "calificacion": 95},
    {"nombre": "Miguel", "edad": 22, "calificacion": 85},
    {"nombre": "Greta", "edad": 21, "calificacion": 90},
    {"nombre": "Pablo", "edad": 23, "calificacion": 78}
]

resultado = filtrar_estudiantes(estudiantes)
print(resultado)


# %%
#19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))
"""
  Devuelve solo los números impares de una lista.

    Args:
         lista (list): Lista de números.

    Returns:
         (list): Lista de números impares.
"""
##Ejemplo de uso
numeros = [1, 527, 46, 78, 895, 45, 7]
resultado = filtrar_impares(numeros)
print(resultado)


# %%
#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
#filter()

def filtrar_enteros(lista):
    """
     Filtra los elementos enteros de una lista que puede contener distintos tipos.

    Args:
         lista (list): Lista con distintos tipos de datos.

    Returns:
         (list): Lista solo con valores enteros.
    """
    return list(filter(lambda x: isinstance(x, int), lista))

##Ejemplos de uso
datos = [1, "hola", 3, "python", 5, 7.5, "mundo"]
resultado = filtrar_enteros(datos)
print(resultado)


# %%
#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3
"""
Calcula el cubo de un número.

    Args:
        x (int/float): Número de entrada.

    Returns:
        (int/float): Resultado del cubo.
"""

##Ejemplo de uso
resultado = cubo(9)
print(resultado)


# %%
#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_lista(lista):
    """
      Calcula el producto de todos los elementos de una lista.

    Args:
        lista (list): Lista de números.

    Returns:
        (int/float): Producto total.
    """
    return reduce(lambda acc, x: acc * x, lista)

##Ejemplo de uso
numeros = [33, 9, 13]
resultado = producto_lista(numeros)
print(resultado)


# %%
#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar_palabras(lista):
    """
       Concatena una lista de palabras en una sola cadena.

    Args:
        lista (list): Lista de strings.

    Returns:
        (str): Cadena concatenada.
    """
    return reduce(lambda acc, palabra: acc + palabra, lista)

##Ejemplo de uso
palabras = ["Buenos", " ", "días", " ", "Vanesa" "!"]
resultado = concatenar_palabras(palabras)
print(resultado)


# %%
#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_lista(lista):
    """
    Calcula la diferencia acumulada de una lista.

    Args:
        lista (list): Lista de números.

    Returns:
        (int/float): Resultado de la resta acumulada.
    """
    return reduce(lambda acc, x: acc - x, lista)

##Ejemplo de uso
numeros = [33, 13, 9]
resultado = diferencia_lista(numeros)
print(resultado)

# %%
#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    """
     Cuenta el número de caracteres en una cadena.

    Args:
        texto (str): Cadena de texto.

    Returns:
        (int): Número de caracteres.
    """
    return len(texto)

##Ejemplo de uso
frase = "Buenos días! Hoy es martes"
resultado = contar_caracteres(frase)
print(resultado)


# %%
#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y
"""
  Calcula el resto de la división entre dos números.

    Args:
        a (int): Dividendo.
        b (int): Divisor.

    Returns:
        (int): Resto de la división.
"""
print(resto(33, 9))

# %%
#27. Crea una función que calcule el promedio de una lista de números.

def promedio_lista(lista):
    """
     Calcula el promedio de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        (float): Promedio.
    """
    return sum(lista) / len(lista)

##Ejemplo de uso
numeros = [33, 13, 9, 99]
resultado = promedio_lista(numeros)
print(resultado)

# %%
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
     Devuelve el primer elemento duplicado en una lista.

    Args:
        lista (list): Lista de elementos.

    Returns:
        any: Primer elemento repetido o None si no hay.
    """
    vistos = set()
    
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    
    return None  # si no hay duplicados

##Ejemplo de uso
numeros = [3, 5, 1, 4, 5, 2]
resultado = primer_duplicado(numeros)
print(resultado)


# %%
#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    """
       Oculta todos los caracteres de una cadena excepto los últimos cuatro.

    Args:
        valor (str/int): Valor a enmascarar.

    Returns:
        (str): Cadena enmascarada.
    """
    texto = str(valor)
    
    if len(texto) <= 4:
        return texto  # no se enmascara
    
    return "#" * (len(texto) - 4) + texto[-4:]

##Ejemplo de uso
print(enmascarar("abcdefg"))


# %%
#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
     Determina si dos palabras son anagramas.

    Args:
        p1 (str): Primera palabra.
        p2 (str): Segunda palabra.

    Returns:
        bool: True si son anagramas, False si no.
    """
    return sorted(palabra1) == sorted(palabra2)

##Ejemplo de uso
print(son_anagramas("roma", "amor"))
print(son_anagramas("osa", "aso"))
print(son_anagramas("python", "perro"))


# %%
#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

def buscar_nombre():
    """
    Busca un nombre en una lista y lanza excepción si no existe.

    Args:
        lista (list): Lista de nombres.
        nombre (str): Nombre a buscar.

    Returns:
        None

    Raises:
        ValueError: Si el nombre no se encuentra.
    """
    try:
        # Pedimos lista de nombres (separados por coma)
        entrada = input("Introduce una lista de nombres (separados por comas): ")
        lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
        
        # Pedimos el nombre a buscar
        nombre_buscar = input("Introduce el nombre a buscar: ").strip()
        
        if nombre_buscar in lista_nombres:
            print(f"{nombre_buscar} fue encontrado en la lista.")
        else:
            raise ValueError(f"{nombre_buscar} no se encuentra en la lista.")
    
    except ValueError as e:
        print(f"Error: {e}")

buscar_nombre()

# %%
#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    """
     Busca un nombre en una lista y lanza excepción si no existe.

    Args:
        lista (list): Lista de nombres.
        nombre (str): Nombre a buscar.

    Returns:
        None

    Raises:
        ValueError: Si el nombre no se encuentra.
    """
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return f"{nombre_completo} ocupa el puesto de {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."

##Ejemplo de uso
empleados = [
    {"nombre": "Ana López", "puesto": "Contable"},
    {"nombre": "Luis Pérez", "puesto": "Ingeniero"},
    {"nombre": "Marta Díaz", "puesto": "Gerente"}
]

print(buscar_puesto("Luis Pérez", empleados))
print(buscar_puesto("Pedro Gómez", empleados))


# %%
#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

suma_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
"""
Suma elementos correspondientes de dos listas.

    Args:
        a (list): Primera lista.
        b (list): Segunda lista.

    Returns:
        (list): Lista resultante.
"""
##Ejemplo de uso
a = [1, 2, 3]
b = [4, 5, 6]

resultado = suma_listas(a, b)
print(resultado)


# %%
#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
#manipular la estructura del árbol.

class Arbol:
    """
     Representa un árbol con tronco y ramas.
    """
    def __init__(self):
        self.tronco = 1        # Longitud inicial del tronco
        self.ramas = []        # Lista vacía de ramas

    # Método para crecer el tronco en 1
    def crecer_tronco(self):
        self.tronco += 1

    # Método para agregar una nueva rama de longitud 1
    def nueva_rama(self):
        self.ramas.append(1)

    # Método para crecer todas las ramas en 1
    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    # Método para quitar una rama en posición específica
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida")

    # Método para obtener información del árbol
    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


# 1. Crear un árbol
mi_arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama en la posición 2
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
info = mi_arbol.info_arbol()
print(info)


# %%
#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
#corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
#agregar dinero al saldo.

class UsuarioBanco:
    """
     Representa un usuario con saldo y operaciones bancarias.
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Método para agregar dinero
    def agregar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"{cantidad} unidades agregadas. Nuevo saldo de {self.nombre}: {self.saldo}")
        else:
            print("Cantidad a agregar inválida.")

    # Método para retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            print("Cantidad a retirar inválida.")
        elif cantidad > self.saldo:
            print(f"Error: saldo insuficiente para {self.nombre}. Saldo actual: {self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"{cantidad} unidades retiradas. Nuevo saldo de {self.nombre}: {self.saldo}")

    # Método para recibir transferencia de otro usuario
    def transferir_dinero(self, remitente, cantidad):
        if cantidad <= 0:
            print("Cantidad de transferencia inválida.")
        elif cantidad > remitente.saldo:
            print(f"Error: {remitente.nombre} no tiene suficiente saldo. Saldo actual: {remitente.saldo}")
        else:
            remitente.saldo -= cantidad
            self.saldo += cantidad
            print(f"{cantidad} unidades transferidas de {remitente.nombre} a {self.nombre}.")
            print(f"Saldo de {remitente.nombre}: {remitente.saldo}")
            print(f"Saldo de {self.nombre}: {self.saldo}")

# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades al saldo de Bob
bob.agregar_dinero(20)

# 3. Hacer transferencia de 80 unidades de Bob a Alicia
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades del saldo de Alicia
alicia.retirar_dinero(50)


# %%
#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
#reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#de la función procesar_texto .

def contar_palabras(texto):
    """
     Procesa un texto según una opción: contar, reemplazar o eliminar.

    Args:
        texto (str): Texto de entrada.
        opcion (str): Tipo de operación.
        *args: Argumentos adicionales.

    Returns:
        (str/dict): Resultado del procesamiento.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()  # opcional: para que "Hola" y "hola" cuenten igual
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    resultado = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            return "Error: se requieren 2 argumentos para reemplazar (original, nuevo)"
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            return "Error: se requiere 1 argumento para eliminar (palabra)"
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida"

##Ejemplo de uso 

texto = "Hola mundo hola Python mundo Python"

# Contar palabras
print("Contar palabras:")
print(procesar_texto(texto, "contar"))

# Reemplazar palabra
print("\nReemplazar 'Python' por 'Java':")
print(procesar_texto(texto, "reemplazar", "Python", "Java"))

# Eliminar palabra
print("\nEliminar 'mundo':")
print(procesar_texto(texto, "eliminar", "mundo"))


# %%
#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia():
    """
    Determina si es día, tarde o noche.

    Args:
        hora (int): Hora del día.

    Returns:
        (str): Momento del día.
    """
    hora = input("Introduce la hora (0-23): ")

    if not hora.isdigit():
        print("Debes introducir un número válido.")
        return

    hora = int(hora)

    if hora < 0 or hora > 23:
        print("Hora inválida. Debe estar entre 0 y 23.")
    elif 6 <= hora < 12:
        print("Es de día 🌅")
    elif 12 <= hora < 20:
        print("Es de tarde 🌇")
    else:
        print("Es de noche 🌙")

momento_del_dia()


# %%
#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#Las reglas de calificación son:
#- 0 - 69 insuficiente
#- 70 - 79 bien
#- 80 - 89 muy bien
#- 90 - 100 excelente

def calificacion_texto():
    """
    Convierte una nota numérica en texto.

    Args:
        nota (int): Nota del alumno.

    Returns:
        (str): Calificación en texto.
    """
    nota = input("Introduce la calificación (0-100): ")

    if not nota.isdigit():
        print("Debes introducir un número válido.")
        return

    nota = int(nota)

    if nota < 0 or nota > 100:
        print("La calificación debe estar entre 0 y 100.")
    elif nota <= 69:
        print("Insuficiente")
    elif nota <= 79:
        print("Bien")
    elif nota <= 89:
        print("Muy bien")
    else:
        print("Excelente")

calificacion_texto()


# %%
#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    """
       Calcula el área de una figura geométrica.

    Args:
        figura (str): Tipo de figura.
        datos (tuple): Datos necesarios.

    Returns:
        (float): Área calculada.
    """
    figura == "rectangulo"
    base, altura = datos
    return base * altura

##Ejemplo de uso
print(calcular_area("rectangulo", (5, 3))) 


# %%
#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
#monto final de una compra en una tienda en línea, después de aplicar un descuento.

def calcular_precio_final():
    """
     Calcula el precio final de un producto aplicando un descuento si existe.

    Returns:
        None: Muestra el resultado final.
    """
    # 1. Precio original
    precio = input("Introduce el precio del artículo: ")

    if not precio.replace(".", "", 1).isdigit():
        print("Precio no válido.")
        return

    precio = float(precio)

    # 2. Preguntar por cupón
    cupon = input("¿Tienes cupón de descuento? (si/no): ").lower()

    # 3. Si tiene cupón
    if cupon == "si":
        descuento = input("Introduce el valor del cupón: ")

        if not descuento.replace(".", "", 1).isdigit():
            print("Descuento no válido.")
            return

        descuento = float(descuento)

        # 4. Validar descuento
        if descuento > 0:
            precio_final = precio - descuento

            # Evitar precios negativos
            if precio_final < 0:
                precio_final = 0

            print(f"Precio final con descuento: {precio_final} €")
        else:
            print("El descuento debe ser mayor que 0.")
            print(f"Precio final: {precio} €")

    # 5. Sin cupón
    elif cupon == "no":
        print(f"Precio final: {precio} €")

    else:
        print("Respuesta no válida. Debe ser 'si' o 'no'.")

calcular_precio_final()



