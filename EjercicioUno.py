# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:12:36 2020

@author: Johnier Sanchez
"""

import EjercicioUno

def nombreUsuario(nombreIngresado):
    
        # Se calcular la longitud del nomre de usuario.
        long=len(nombreIngresado) 
        # Se calcula que la cadena contenga valores alfanuméricos.
        x=nombreIngresado.isalnum()
        # Se presenta mensaje cuando la cadena contiene valores no alfanuméricos.
        if x== False:
            print("El nombre de usuario puede contener solo letras y números")
        # Se presenta mensaje cuando la cadena contiene menos de 6 caracteres.    
        if long < 6: 
            print("El nombre de usuario debe contener al menos 6 caracteres")
        # Se presenta mensaje cuando la cadena contiene mas de 12 caracteres.    
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
         # Se valida cantidad de caracteres.   
        if long >5 and long <13 and x ==True:
            # Se retorna verdadero, si el tamaño es mayor a 5 y menor a 13.
            return True 
        
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
    
main()