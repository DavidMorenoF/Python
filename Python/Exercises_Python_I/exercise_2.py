# 2- Màquina de venda de bitllets de metro

"""
Els objectius d’aquest exercici són:
• Treballar estructures condicionals
• Treballar estructures iteratives
• Implementar estructures de control d’input de dades

Hem d’implementar una màquina de venda de bitllets de transport metropolità.

En primer lloc la màquina ofereix diferents títols de transport que poden ser adquirits, l’usuari
només pot escollir una opció d’aquesta llista:
o Bitllet senzill
o TCasual
o TMes
o TTrimestre
o TJove

Un cop l’usuari hagi escollit una opció se li preguntarà les zones que vol viatjar.(1,2 o 3).

Un cop escollides les zones es mostrarà el preu i l’usuari podrà introduir els diners (només es
pot pagar en efectiu, amb monedes i bitllets d’EURO existents).

Els preus son els següents:

o Bitllet senzill............2,20€ (1a zona)
o TCasual.................10,20€ (1a zona)
o TMes......................54,00€ (1a zona)
o TTrimestre..........145,30€ (1a zona)
o TJove...................105,00€ (1a zona)

Els preus per la segona zona son els preus de la primera zona multiplicats per 1,35.

Els preus de la tercera zona son els preus de la primera zona multiplicats per 1,89.

Un cop pagat el bitllet es retornarà el canvi i la màquina quedarà altre cop en disposició de
vendre un nou bitllet.

Implementa en python el codi necessari per la venda de bitllets. Pensa que l’usuari pot introduir
dades errònies i ho hem de controlar.
"""

def escull_tipus_bitllet (tipus, llista_de_tipus):
    match (tipus):
        case 1:
            return llista_de_tipus[0]
        case 2:
            return llista_de_tipus[1]
        case 3:
            return llista_de_tipus[2]
        case 4:
            return llista_de_tipus[3]
        case 5:
            return llista_de_tipus[4]
        case _:
            return None

def escull_zones (tipus):
    if (tipus >= 1 and tipus <=3):
        return tipus
    else: 
        return None
        
exit= False
while(exit == False):
    print("Hola, escull una opció:")
    print("1- Comprar Bitllet.")
    print("2- Sortir.")
    seleccio= int(input())
    if (seleccio == 1):
        print("Selecciona un bitllet per començar:")
        llista_de_tipus = ["Bitllet senzill", "Tcasual", "TMes", "TTrimestre", "TJove"]
        boto=1
        for tipus in llista_de_tipus:
            print(boto, "- ", tipus)
            boto += 1
        tipus_bitllet= int(input())
        seleccio_correcta= False
        preus_basic= [2.2, 10.2, 54.0, 145.3, 105]
        preus_zones= [1, 1.35, 1.89]
        while (seleccio_correcta == False):
            if (escull_tipus_bitllet(tipus_bitllet,llista_de_tipus) != None):
                print("Has escollit ",str(escull_tipus_bitllet(tipus_bitllet,llista_de_tipus)), ".\n")
                seleccio_correcta = True
            else:
                print("Selecció incorrecta. Prova de nou...")
                tipus_bitllet= int(input())

        print("Selecciona el numero de zones:")
        for i in range(1, 4):
            print("Zona ", i)
        seleccio_correcta= False
        tipus_zona= int(input())
        preu_final= 0
        while (seleccio_correcta == False):
            if (escull_zones(tipus_zona) != None):
                print("Has escollit opció de",str(escull_zones(tipus_zona)), "zones.")
                preu_final = preus_basic[tipus_bitllet-1] * preus_zones[tipus_zona-1]
                print(preus_basic[tipus_bitllet-1])
                print(preus_zones[tipus_zona-1])
                print ("El preu total del bitllet es", round(preu_final, 2), "€")
                seleccio_correcta = True
            else:
                print("Selecció incorrecta. Prova de nou...")
                tipus_zona= int(input())

        print("Introduiu l'efectiu:")
        seleccio_correcta= False
        efectiu = 0
        canvi= 0
        while (seleccio_correcta == False):
            efectiu= float(input())
            if( efectiu < preu_final):
                print("Quantitat insuficient. Falten", round((preu_final - efectiu), 2), "€")
                print("Introduiu l'efectiu:")
                preu_final = preu_final - efectiu
            else:
                canvi= round(((preu_final- efectiu) * -1), 2)
                print("Transacció correcta. El canvi es", canvi, "€. No oblidi agafar el bitllet i el canvi.")
                seleccio_correcta = True
    elif (seleccio == 2):
        print("Gracies per la seva confiança. Bondia.")
        exit= True
    else:
        print("Selecció no válida. Prova de nou...")
        

