
# 4- Proporció àuria

"""
Donada la imatge de l’espiral d’or de proporció àuria següent, desenvolupa un algoritme recursiu
que retorni qualsevol element de la sèrie:

Veient la imatge anterior, se’n desprèn que correspon a una successió de valors determinada
per una funció. Per exemple, l’element 1 de la successió que correspon al quadrat on hi ha el
primer punt al centre de l’espiral, per tant f(1), és igual a 1, l’element 2 de la successió és també
1 i l’element 3 de la successió val 2.

Una altra manera de graficar-ho és de la següent manera:

Com podeu veure a la gràfica, el nombre de quadradets d’ample i alt, correspon al valor de la
successió.

Així doncs:
- f(1) = 1
- f(2) = 1
- f(3) = 2
- f(4) = 3
- ...
"""

def numero (numero):
    lista =[1]
    print("f(", 1, ") = ",lista[0])
    for i in range(0,numero -1):
        if (len(lista) <= 1):
            anterior = lista[-1] + i
        else: 
            anterior = lista[-1] + lista[len(lista) - 2]   
        lista.append(anterior)
        print("f(", i + 2, ") = ",anterior)

def serie (numero_inicial, numero_final):
    print("\n")
    lista =[1]
    for i in range(0, numero_final -1):
        if (len(lista) <= 1):
            anterior = lista[-1] + i
            if(len(lista) >= numero_inicial -1):
                print("f(", i + 2, ") = ",anterior)
        else: 
            anterior = lista[-1] + lista[len(lista) - 2] 
            if(len(lista) >= numero_inicial -1):
                print("f(", i + 2, ") = ",anterior)
        lista.append(anterior)

def _init_():
    print("Bondia. Selecciona una opció: \n 1- Introduïu el numero de Finonacci. \n 2- Introduïu la serie de Fibonacci. \n 3- Sortir")
    exit = False
    while (exit == False):
        print("\n 1- Introduïu el numero de Finonacci. \n 2- Introduïu la serie de Fibonacci. \n 3- Sortir")
        seleccio = int(input())
        if (seleccio == 1):
            print("Introdueix un numero:")
            numero(int(input()))
        elif (seleccio == 2):
            print("Introdueix una serie:")
            serie (int(input()), int(input()))
        elif (seleccio == 3):
            print("Gracies per tot.")
            exit = True
        else:
            print("Selecció incorrecta")

_init_()
