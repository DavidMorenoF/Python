
#1- Càlcul de la factura de consum de l’aigua.

"""
Escriu un algoritme que permeti a l’usuari calcular el consum d’aigua en un domicili. Calcula la
factura de l’aigua, donats els litres d’aigua gastats per l’usuari i sabent el següent:

a) Hi ha una quota fixe mensual de 6€ pel servei.
b) Si el consum és menor de 50 litres, no es paga la quota variable, només el fixe.
c) Si el consum d’aigua es troba entre 50 i 200 litre es factura el litre a 0.1 €.
d) Si el consum d’aigua és major a 200 litres es cobra el litre a 0.3 €.

Mostra a l’usuari un menú per consola que permeti calcular l’import de la seva factura en funció
dels litres d’aigua que ha consumit
"""

def calculFactura(consum):
    quota_fixa= 6
    if (consum < 50):
        return quota_fixa
    elif (consum >=50 and consum < 200):
        return consum * 0.1 + quota_fixa
    else:
        return consum * 0.3 + quota_fixa
    

print ("Buenos días, indica su nombre por favor...")
nombre= str(input())
print("Bienvenid@ ", nombre)
print("Indique el consumo en litros para hacer un calculo de su tarifa:")
consum= float(input())
print("El precio final de la factura son ",calculFactura(consum),"€")

