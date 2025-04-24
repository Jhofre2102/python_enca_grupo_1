'''
crear las funciones sumar, resta, multiplicacion
division(validar 0 denominador)
division piso
crear una funcion que genere un numero aleatorio
(import random)
crear una funcion operacion modulo(%)



'''
import random

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "no se puede dividir por cero"
        return a/b
    
def division_piso(a,b):
    return a//b

def numero_aleatorio():
    return round(random.random(),2)

def numero_modulo(a,b):
    return a%b

