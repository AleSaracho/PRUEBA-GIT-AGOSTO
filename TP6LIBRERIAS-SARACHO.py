"""" Trabajo Practico N° 6 - LIBRERIAS
Nombre y Apellido: Viviana Alejandra Saracho
Comisión: Jueves - virtual
"""
"""
Ejercicio 01: Escriba una función redondear()  que permita redondear un número decimal
de acuerdo al criterio: Si el número es mayor a 3,50 devolver el 
entero siguiente (en este caso 4) , sino devolver el entero inmediatemente
anterior (3).
"""
import math # se importa de la libreria math las funciones para redondear decimales
def redondear(deci):  # se crea la funcion redondear que recibe un número decimal como parámetro
          num1=int(deci) #la variable num1 contendrá la parte entera del número ingresado
          if deci > (num1+0.50): #se usa el condicional if para comparar el número ingresado con la suma de la parte entera del número ingresado mas 0,50
                   print(math.ceil(deci)) # se muestra el resultado de la función ceil que redondea al entero inmediato siguiente
                   return math.ceil(deci) #la función retorna el número redondeado al entero inmediato superior
          else:                           # si el decimal ingresado es menor a la suma de su parte entera más 0.50
                  print(math.floor(deci))   # se muestra el resultado de la función floor que redondea el decimal al entero inmediato anterior       
                  return math.floor(deci)   # la función retorna el valor del número redondeado al entero inmediato inferior

decimal=float(input("Ingrese un número decimal: ")) # en la variable tipo real de guarda el número decimal ingresado
redondear(decimal) # se llama a la función redondear


"""
Ejercicio 02: Coloque el módulo del ejercicio anterior dentro de paquete.
En un módulo  que esté fuera de ese paquete, cree una función 
de suma de decimales que redondee el resultado haciendo uso de 
la función redondear() del paquete recién creado.
"""

import paquete #se importa del archivo llamado paquete la función redondear

def sumadecimales(num2,num3):  #se crea la función para sumar dos números decimales ingresados por el usuario
             deci=num2+num3    # se crea la variable deci que contendrá la suma de los números ingresados
             paquete.redondear(deci) #se ejecuta la función redondear importada de paquete que recibe como parámetro la variable deci
             

num2=float(input("Ingrese un número decimal:  ")) # se pide al usuario que ingrese un número decimal
num3=float(input("Ingrese otro número decimal:  ")) # se pide al usuario que ingrese otro número decimal
sumadecimales(num2,num3) # se ejecuta la función que recibe como parámetros los dos números ingresados para sumarlos


"""
Ejercicio 03: Usando el módulo datetime, escribe un programa que muestre 
la fecha y hora actuales del sistema.
"""

from datetime import datetime #desde el módulo datetime se importan los datos de  fecha y hora
fechahora=datetime.now() #la variable fechahora contendrá la fecha y hora actual  generados por la función datetime a través del método now
print("FECHA ACTUAL:") #cartel para imprimir título de fecha
print(f"Hoy es el día: {format(fechahora.day)},", end=' ') # se muestra la parte correspondiente al "día" de toda la fecha para obtenerla se usa la función format
print(f"del Mes: {format(fechahora.month)},", end=' ') # se obtiene con la función format la parte que corresponde al mes y se la muestra
print(f"del Año: {format(fechahora.year)}") # se muestra la parte correspondiente al año usando la función format
print("HORA ACTUAL") # cartel para mostrar título de fecha
print(f"Son las  {format(fechahora.hour)} Horas,", end=' ') #se muestra la parte correspondiente a la hora
print(f"{format(fechahora.minute)} Minutos,", end=' ') # se muestra la parte correspondiente a los minutos
print(f"{format(fechahora.second)} Segundos") # se muestra la parte correspondiente a los segundos

print("OTRA FORMA PARA MOSTRAR FECHA Y HORA")
feho=datetime.now() # la variable guarda la fecha y hora actuales que se obtienen con el método  now 
print(feho.date()) # se muestra la parte correspondiente a la fecha solamente que se obtiene con date
print(feho.time()) # se muestra la parte de la hora actual obtenida por time


"""
Ejercicio 04: Escriba un programa que devuelva un número par al azar 
entre 2 y 10 (pista para comprobar si se pueden generar todos los 
números, pruebe ejecutar el programa dentro de un ciclo infinito)
"""
import random # se importa el modulo random
numero=random.randint(2,10) # se crea la variable numero que guardará el número aleatorio entre 2 y 10 que de como resultado la función randint()
#while numero<=10:
if numero%2==0: # si el número aleatorio es par(para saber eso se calcula el resto de la división por 2)
                print(numero, end=' ') # se muestra en pantalla el número aleatorio par
                #numero=random.randint(2,10) # ésta línea la puse para probar el ciclo while
#else:
                #print(numero, end=' ') # ésta línea la puse para ver si mostraba los impares salidos al azar
              #numero=random.randint(2,10) # ésta línea también la puse para probar el ciclo while
                          

"""
Ejercicio 05:Bola Mágica: La bola mágica (Magic 8 ball) es un popular juguete
usado para la adivinación o para buscar un consejo. Su mecanismo
es muy simple: ante una pregunta del usuario, la bola responde
con una de 8 posibles respuestas:
- Es seguro que si
- Las chaces son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no

Escriba una función en Python para simular la bola mágica
"""
import random # se importa el módulo random
def bolamagica(lisres):    # se crea la función que recibe como parámetro una lista que contiene las respuestas
            print(random.choice(lisres)) # se imprime la respuesta de la lista elegida aleatoriamente por la función choice
      

respuestas=["Es seguro que si", "Las chances son buenas", "Puedes contar con ello", 
            "Pregúntame de nuevo más tarde", "Concéntrate y pregunta de nuevo", 
            "No veo con claridad, intenta de nuevo", "Mi respuesta es no", "Mis fuentes me dicen que no"]
# se crea la lista respuestas que contiene las opciones para que elija la función 
print("LA BOLA MÁGICA") # se muestra título del juego
pregunta=input("Realiza una pregunta a la bola mágica: ") # se pide que el usuario ingrese una pregunta
bolamagica(respuestas) # se llama a la función bolamagica que recibe la lista respuestas como parámetro



"""
Ejercicio 06: Encuentra el tiempo de ejecución de los programas de
los ejercicios anteriores (pista: use el módulo time)
"""

import time # se importa el módulo time
inicio=time.time()  # la variable  guardará el tiempo al inicio del código a medir
bolamagica(respuestas) # se coloca el código al que se quiere medir la duración
fin=time.time() # la variable guardará el valor del tiempo al final de la ejecución del código
print(fin-inicio) # se muestra el tiempo transcurrido ( para ello se resta a la medición final la medición inicial)

