# Je déclare une fonction 
def deposit() : 
    # Je créé une boucle et je teste les différentes conditions. 
    while True: 
        amount = input("What would you like to deposit? $") # $ permet à l'utilisateur d'intégrer une donnée
        # je vérifie que l'entrée de l'utilisateur est un nombre
        if amount.isdigit():
            amount = int(amount) # je passe ma valeur en nb entier
            # je vérifie que l'entrée de l'utilisateur est un nb positif
            if amount > 0: break
            else: 
                print("Amount must be greater than 0.") # prompt si la valeur est négative
        else: 
            print("Please enter a number")

    return amount # ma fonction retourne la valeur entrée par l'utilisateur