def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def multiply(x,y):
    return x*y


def divide(x,y):
    # si le diviseur est 0
    if y == 0 :
        # alors j'affiche une erreur
        print("erreur de division par 0)
        # je retourne
        return
    # sinon je retourne la division de x par y
    return x / y


def modulo(x,y):
    return x%y


def revenusParSec(salaireH,heureParJO,JOparAn):
    # Je calcule le salaire annuel
    salaireAnnuel = salaireH * heureParJO * JOparAn 
    # Je calcule le nombre de seconde par an
    nbSecondeParAn = 365 * 24 * 60 * 60 
    # Je divise mon salaire par le nombre de seconde dans une année
    return salaireAnnuel / nbSecondeParAn 


def withdrawFees(total, percent):
    #calcul du montant des taxes a retirer
    fees = total * (percent / 100)
    # je retourne mon total sans les taxes
    return total - fees

def calculSalaireNet(salaireBrut, public):
    # si j'occupe un poste de la fonction publique
    if public :
    # alors je retourne le salaire brut - 15 % de taxes
        return withdrawFees(salaire_brut, 15)
    # sinon, c'est que je suis un travailleur privé
    else :
    # alors je retourne le salaire_brut - 23 % de taxes
        return withdrawFees(salaire_brut, 23)

tour = 0
# Tant que je ne suis pas au tour 5
while tour != 5
# Appeler la fonction JouerUnTour
    jouerUnTour()
# J'effectue l'action de passer un tour
    tour += 1