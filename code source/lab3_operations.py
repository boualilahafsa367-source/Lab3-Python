a = 15
b = 4
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")      # division classique → float
print(f"{a} // {b} = {a // b}")    # quotient entier
print(f"{a} % {b} = {a % b}")      # reste
print(f"{a} ** {b} = {a ** b}")    # puissance (a^b)

x = 20
y = 15
print(x == y)   # False
print(x != y)   # True
print(x < y)    # False
print(x >= y)   # True

mot_1 =("Hello")
mot_2 =("World")
print(mot_1==mot_2) #false
print(mot_1!=mot_2) #True
print(mot_1<mot_2)  #True
print(mot_1 >=mot_2) #False

age = 22
permis = True
casier_vierge = False

peut_conduire = (age >= 18) and permis
print(peut_conduire) #True

peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print(peut_louer_voiture) #True

sanction = not casier_vierge #True
print(sanction)
