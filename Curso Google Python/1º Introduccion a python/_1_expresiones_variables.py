""""Utilice la función print() para generar una cadena """

# Sintaxis para imprimir una cadena de texto
print("I love Python!")

# Sintaxis para imprimir valores numéricos
print(360)
print(32*45)

# Sintaxis para imprimir el valor de una variable
value = 8 * 6  # pylint: disable=invalid-name
print(value)

# Usar operadores aritméticos, con especial atención a los exponentes

# Multiplicación, división, suma y resta
print(3*8/2+5-1)

# Exponentes
print(4**6)  # Sintaxis significa 4 elevado a 6
print(4**2)  # Para elevar al cuadrado un numero
print(4**3)  # Para elevar al cubo un numero
print(4**0.5)  # Para encontrar la raíz cuadrada de un número

# Para calcular cuántas combinaciones posibles diferentes se pueden hacer
# formado usando un conjunto de caracteres "x" con cada carácter en "x"
# teniendo un número "y" de valores posibles, necesitará usar un
# exponente para el cálculo:
x, y = 4, 26
print(y**x)

# Usar variables con asignación y operadores aritméticos

# Asignación de valores a las variables:
years, weeks_in_a_year = 10, 52
# A esta variable se le asigna un cálculo aritmético:
weeks_in_decade = years * weeks_in_a_year  # pylint: disable=invalid-name
# Imprime el cálculo almacenado en la variable "weeks_in_a_decade":
print(weeks_in_decade)
