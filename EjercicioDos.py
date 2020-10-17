# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:38:31 2020

@author: Johnier Sanchez
"""
import EjercicioDos

def contraseñaUsuario(contraseñaIngresada):
        
        # Se inicializa la varibale booleana que controla el cumplimiento de todos los requisitos.
        validador=False
        # Se calcula la longitud de la contraseña.
        long=len(contraseñaIngresada)
        # Se inicializa la variable para identificar los espacios.
        espacio=False
        # Se inicializa la variable para identificar letras mayúsculas.
        mayuscula=False
        # Se inicializa la variable para identificar letras minúsculas.
        minuscula=False
        # Se inicializa la variable para identificar números.
        numeros=False 
        # Se valida si hay caracteres alfanumérica y se retona True.
        y=contraseñaIngresada.isalnum()
        # Se inicializa la variable para verificar que hayan mayuscula, minuscula, numeros y no alfanuméricos
        aceptable=True 
        
        # Se genera ciclo for para recorrer caracter por caracter en la contraseña ingresada.
        for carac in contraseñaIngresada: 
            # Se valida si el caracter es un espacio
            if carac.isspace()==True: 
                #si encuentra un espacio se cambia el valor user
                espacio = True 
            # Se valida si hay mayuscula
            if carac.isupper()==True: 
                #acumulador o contador de mayusculas
                mayuscula=True 
            # Se valida si hay minúsculas    
            if carac.islower()==True:
                #acumulador o contador de minúsculas
                minuscula=True 
            # Se valida si hay números
            if carac.isdigit()==True:
                #acumulador o contador de numeros
                numeros = True 
                
        # Se valida si hay espacios en blanco                    
        if espacio == True: 
                print("La contraseña no puede contener espacios")
        else:
            #se cumple el primer requisito que no hayan espacios
            validador = True 
                       
        if long <8 and validador == True:
            print("Mínimo 8 caracteres")
            #cambia a Flase si no se cumple el requisito móinimo de caracteres
            validador = False 

        if mayuscula == True and minuscula == True and numeros == True and y == False and validador == True:
            #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
            validador = True 
        else:
           #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           aceptable=False 
           
        if validador == True and aceptable == False:
           print("La contraseña elegida no es segura")

        if validador == True and aceptable == True:
           return True
       
def main():
    
    # Se inicializa la varibale booleana.
    ciclo=False
    # Se crea blucle para la presentación de los mensajes.
    while ciclo == False:
        # Se imprime petición de Contraseña.
        contraseñaIngresada=input("Ingrese su Contraseña: ")
        # Se realizan las validaciones especificadas.
        if EjercicioDos.contraseñaUsuario(contraseñaIngresada) == True:
            # Se muestra mensaje exitoso de creación.
            print("Contraseña creada exitosamente")
            # Se termina ciclo while.
            ciclo = True
        
main()