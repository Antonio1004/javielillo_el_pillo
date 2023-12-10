def menu_juego():
    print("=======================")
    print("1. Apostar.")
    print("2. Mostrar historial.")
    print("3. Retirarse.")
    print("=======================")
    opcion=int(input("Introduzca la accion que desea realizar:"))
    return opcion

def apostar(opcion1):
    if opcion1==1:
        numero_apuesta=int(input("Introduce el numero sobre el que va apostar:"))
        cantidad_apuesta=int(input("Introduzca la cantida a apostar:"))
        dados=numero_aleatorio1+numero_aleatorio2
        if dados==numero_apuesta:
            ganancia=cantidad_apuesta*2
            print(f"La suma de los dados es de {dados}, usted aposto por el {numero_apuesta} y gana {ganancia}.")
            lista_ganancia.append(ganancia)
        elif dados!=numero_apuesta:
            perdida=cantidad_apuesta
            print(f"La suma de los dados es de {dados},usted aposto por el {numero_apuesta} y usted pierde {perdida}.")
            lista_perdida.append(perdida)
             
        print(f"Usted lleva jugado un total de{lista_ganancia+lista_perdida}, {lista_ganancia} ganados y {lista_perdida} perdidos.")     
#def historial_jugadas(opcion2):
#    if opcion2==2:
import random
numero_aleatorio1=random.randint(1,6)
numero_aleatorio2=random.randint(1,6)
opcion=menu_juego()
lista_ganancia=[]
lista_perdida=[]
print(opcion)
apostar(opcion)
