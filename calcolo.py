import math

print("Scegli se calcolare il perimetro del quadrato, il perimetro del rettangolo o la circonferenza del cerchio")
print("-1 Quadrato")
print("-2 Cerchio")
print("-3 Rettangolo")
print("-0 Se vuoi chiudere il programma")

calcolo=int(input("Scegli tra una di queste 3 opzioni: "))

if calcolo == 0:
    print("Hai scelto di chiudere il programma, arrivederci.")

elif calcolo == 1:
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro_q = 4*lato
    print("Il perimetro del quadrato e': ", perimetro_q)
    
elif calcolo == 2:
    r = float(input("Inserisci il raggio: "))
    circonferenza=2*math.pi*r
    print("La circonferenza del cerchio e': ", circonferenza)
    
elif calcolo == 3:
    b = float(input("Inserisci la base: "))
    h = float(input("Inserisci l'altezza: "))
    perimetro_r = float
    perimetro_r = b*2 + h*2
    print("Il perimetro del rettangolo e': ", perimetro_r)
    
else:
    print("Hai inserito un opzione errata.")
