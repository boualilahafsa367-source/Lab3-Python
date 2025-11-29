# mini_reduction.py
try: # try/expect permet de verfier ce que l'utilisateur a sasie peut etre convertir en float , sinon elle affiche un message d'error et arrete le programme
    prix_initial = float(input("Prix du produit (€) : ")) # on demande a l'utilisateur de saisir un prix puis en le convertir en decimale
except ValueError:
    print("Saisie invalide pour le prix.")
    exit(1)

statut = input("Êtes-vous étudiant ? (o/n) ").strip().lower() # la fct lower()transforme ce que l'utilisateur a saisie en minusscules

fidelite = input("Fidélité (en années) : ").strip()# la fct strip() enleve tout espace saisie au debut et a la fin

try:#Try: permet de verifier ce que l'utilisateur a sasie peut etre convertir en int ,
    fidelite = int(fidelite)
except ValueError: #exepct: sinon , un message d'error s'affiche et le programme s'arrete d'execution
    print("Saisie invalide pour la fidélité.")
    exit(1)

code=(input("Code du PROMO:"))


reduction = 0.0
#reduction Etudiant:
if statut == "o":
    reduction += prix_initial * 0.10  # 10 % reduction du prix initial si l'utilisateur a repondu avec 'o'
    print("Réduction Etudiant :", prix_initial * 0.10)
#reduction fidelite:
if fidelite >= 5:
    reduction += prix_initial * 0.15  # 15 % reduction du prix initial si la fidelite sasie >= 5
    print("Réduction fidélité :", prix_initial * 0.15)
#reduction fixe supplementaire:
if (prix_initial > 100):
    reduction += 5.0  #  réduction fixe supplémentaire si le prix_initiale  saisie est > 100
    print("Réduction supplémentaire pour prix > 100 :", 5.0)
#reduction promo:
if  code == "PROMO10":
    reduction += prix_initial * 0.30 #reduction promo
    print("Réduction PROMO :", prix_initial * 0.15)

prix_final = prix_initial - reduction  # calcul du prix final
if prix_final < 0:  #ce bloc final empêche un prix négatif (on recourt à une comparaison + affectation).
     prix_final = 0.0  # garde-fou

#Affichage:
print(f"Réduction totale : {reduction:.2f} €")
print(f"Prix final : {prix_final:.2f} €")