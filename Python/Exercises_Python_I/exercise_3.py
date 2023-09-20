
import os

# 3- Renaming files

"""
L’objectiu d’aquest exercici és el de crear un script que permeti a l’usuari renombrar els noms
dels arxius d’un determinat directori. Per a tal cosa, se li demanarà la ruta del directori on hi ha
els arxius a modificar i seguidament el patró de text a buscar pera ser modificar usant
expressions regulars i finalment el text que volem que s’hi posi enlloc del text actual buscat.

Crea un script python en un fitxer .py per a ésser executat des del terminal de la següent manera:
py + nomScript.py

Nota: En funció de com hagueu configurat el PATH de la variable d’entorn de l’intèrpret de
python, per executar un script de python potser heu de fer ús d’una paraula diferent a py.

Aquest script, un cop executat, ha de permetre interacció amb l’usuari a través del terminal de
manera que se li pregunti a l’usuari a quin directori hi ha els fitxers a renombrar, quin patró de
text buscar i quin text posar en el seu lloc.

Com podeu imaginar, haureu de crear un bucle que pugui iterar sobre tots els fitxers continguts
dins de la carpeta que ha demanat l’usuari.

Nota: Us podeu crear un conjunt de fitxers .txt de prova dins del mateix directori per testejar que
funciona."""

print("Bondia\n Introdueix el nom del directori per començar:")
ruta = str(input())
llista_fitxers = os.listdir(ruta)
print("A continuació escriu el text a cambiar:")
text_inicial = str(input())
result = False
for fitxer in llista_fitxers:
    if (text_inicial in fitxer):
        result = True
if (result == False):
    print("No s'han trobat fitxers amb aquest nom")
else:
    print("Per ultim, posa el text que vols que substitueixi l'anterior:")
    text_final = str(input())
    for fitxer in llista_fitxers:
        if (text_inicial in fitxer):
            fitxer_final = fitxer.replace(text_inicial,text_final)
            os.rename(ruta + "/" + fitxer,ruta + "/" + fitxer_final)
            print("S'ha modificat el nom correctament.")


#/home/sjo/Escriptori/DADES/DavidMorenoFernández/M15-Sistemes_Experts/Python/Exercises_Python_I/Prova_3