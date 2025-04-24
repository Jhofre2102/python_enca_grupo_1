'''
realizar las importaciones de las funciones
segun las 4 variantes vistas
hacer print a la ejecucion de las funciones importadas
'''

from operaciones import sumar
print(sumar(4,5))

from operaciones import *
print(restar(10,5))

import operaciones as op
print(op.multiplicar (4,5))

from operaciones import division_piso
print (division_piso(4,5))

from operaciones import numero_aleatorio
print(numero_aleatorio())

from operaciones import *
print(numero_modulo(20,3))

