# 1. Demande du nom d'utilisateur
def nom_user():
    while True:
        Nom = input("Entrez votre Nom : ").strip()
        if not Nom:
            print("veuillez saisir votre nom ! ")
        elif not Nom.isalpha():
            print("Nom invalide : Veuillez entrez uniquement que des lettres ! \n")
        else:
            return Nom

nom = nom_user()
print(f"Bonjour {nom} ! \n")
print()
print("*****************************************")

# 2. Dictionnaire des villes
ville = {
    1: "pkekunou",
    2: "Akato",
    3: "segbé",
    4: "wonyonmé",
    5: "sagbado",
    6: "Adidogomé",
    7: "Atikoume",
    9: "Gbonssimé",
    8: "Adétikopé",
    11:"zanguera",
    10:"Légbassito",
    12:"Djidjolé",
    13:"Avepozo",
    14:"Adétikopé",
}

# Affichage des villes
for numero, nom_ville in ville.items():
    print(f"{numero}-{nom_ville}")
print("*****************************************")
print()

# 3. Choix de la ville de départ
def Depart():
    while True:
        depart = input("veuillez entrer le chiffre qui correspond a votre ville de depart . ").strip()
        if not depart:
            print("Erreur :Vous n'avez rien saisis.")
        elif not depart.isdigit():
            print("Erreur veuillez n'entrer que le chiffre correspondant a la ville .")
        elif int(depart) not in ville:
            print("Erreur ce numero ne figure pas dans la liste ")
        else:
            numero_depart = int(depart)
            print(f"depart sélectionné: {ville[numero_depart]}")
            return numero_depart
#afficher je nom de la ville
code_depart = Depart()
print()

# 4. Choix de la ville de destination
def Destination():
    while True:# si condition
        destination = input("veuillez entrer le chiffre qui correspond a votre ville de destination . ").strip()
        if not destination:
            print("Erreur :Vous n'aviez choisir votre ville de destination .")
        elif not destination.isdigit():
            print("Erreur veuillez n'entrer que le chiffre correspondant a la ville .")
        elif int(destination) not in ville:#si le chiffre ne fait pas parti du dictionnaire
            print("Erreur ce numero ne figure pas dans la liste ")
        else:
            numero_destination = int(destination)
            print(f"destination sélectionnée: {ville[numero_destination]}")
            return numero_destination
#afficher la ville
code_destination = Destination()
print()

# 5. Dictionnaire et choix du moyen de déplacement
print("*****************************************")
Deplacement = {
    1: "Taxie",
    2: "Zemidjan"
}

for numero_moyen, moyen in Deplacement.items():
    print(f"{numero_moyen}-{moyen}")


def deplacement():
    while True:
        Moyen = input("Veuillez choisir votre moyen : ").strip()
        if Moyen.isdigit() and int(Moyen) in Deplacement:
            numero_moyen = int(Moyen)
            print(f"moyen choisie : {Deplacement[numero_moyen]}")
            return numero_moyen
        print("Erreur : veuillez choisir un numero valide de la liste")

code_moyen = deplacement()

print()
c_taxie = 150
c_zemidjan = 200

# 6. Calcul du tarif du trajet
def cout(code_depart, code_destination, code_moyen):
    distance = abs(code_destination - code_depart)
    
    # 1 correspond à Taxie, 2 à Zemidjan
    if code_moyen == 1:
        prix = distance * c_taxie
    else:
        prix = distance * c_zemidjan
    return prix

# 7. Affichage du résultat final
prix_total = cout(code_depart, code_destination, code_moyen)
print(f"             BIENVENUE  {nom} !                            ")
print(f"votre cout de trajet: {prix_total} FCFA ")
print()