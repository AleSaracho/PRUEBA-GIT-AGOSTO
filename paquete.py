import math
def redondear(deci):  # se crea la funcion redondear que recibe un número decimal como parámetro
          num1=int(deci) #la variable num1 contendrá la parte entera del número ingresado
          if deci > (num1+0.50): #se usa el condicional if para comparar el número ingresado con la suma de la parte entera del número ingresado mas 0,50
                   print(math.ceil(deci)) # se muestra el resultado de la función ceil que redondea al entero inmediato siguiente
                   return math.ceil(deci)
          else:                           # si el decimal ingresado es menor a la suma de su parte entera más 0.50
                  print(math.floor(deci))   
                  return math.floor(deci)