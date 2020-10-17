# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:44:24 2020

@author: Johnier Sanchez
"""

import EjercicioUno
import EjercicioDos

def main():
    
    # Se inicializa la varibale booleana.
    ciclo=False
    # Se crea blucle para la presentación de los mensajes.
    while ciclo==False:
        # Se imprime petición de nombre.
        nombreIngresado=input("Ingrese nombre de usuario: ")
        # Se realizan las validaciones especificadas.
        if EjercicioUno.nombreUsuario(nombreIngresado) == True:
            # Se muestra mensaje exitoso de creación.
            print("Usuario creado exitosamente")
            # Se termina ciclo while.
            ciclo=True
    
    while ciclo == False:
        # Se imprime petición de Contraseña.
        contraseñaIngresada=input("Ingrese su Contraseña: ")
        # Se realizan las validaciones especificadas.
        if EjercicioDos.contraseñaUsuario(contraseñaIngresada) == True:
            # Se muestra mensaje exitoso de creación.
            print("Contraseña creada exitosamente")
            # Se termina ciclo while.
            ciclo = False
            
main()