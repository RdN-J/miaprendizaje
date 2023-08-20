"""Grupo de habilidades 1

Use el operador de asignación = para asignar valores a las variables

Utilice operadores aritméticos básicos con variables para crear expresiones

Utilice la conversión explícita para cambiar un tipo de datos de flotante a cadena"""


# Las siguientes líneas asignan la variable a la izquierda de =
# operador de asignación con los valores y expresiones aritméticas
# en el lado derecho del operador de asignación =.
hotel_room, room_guests = 100, 4
tax = hotel_room * 0.08
total = hotel_room + tax
share_per_person = total/room_guests

# Esta línea genera el resultado del cálculo final almacenado
# en la variable "share_per_person"
# cambiar un tipo de datos
print("Each person needs to pay: " + str(share_per_person))


"""Grupo de habilidades 2

Salida de múltiples variables de cadena en una sola línea para formar una oración

Use el conector más (+) o una coma para conectar cadenas en una función de impresión ()

Crear espacios entre variables en una función print()"""

# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."

print(salutation + " " + first_name + " " +
      middle_name + " " + last_name + ", " + suffix)
# The comma as a string ", " adds the conventional use of a comma plus a
# space to separate the last name from the suffix.

# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name, ",", suffix)
# However, you will find that this produces a space before a comma within a string.
