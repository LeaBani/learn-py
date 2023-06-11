MAX_LINES = 3 # Pour déclarer une const j'écris en lettres capitales (convention Python)

# Je déclare une fonction 
def deposit() : 
    # Je créé une boucle et je teste les différentes conditions. 
    while True: 
        amount = input("What would you like to deposit? ") # input permet à l'utilisateur d'intégrer une donnée
        # je vérifie que l'entrée de l'utilisateur est un nombre
        if amount.isdigit():
            amount = int(amount) # je passe ma valeur en nb entier
            # je vérifie que l'entrée de l'utilisateur est un nb positif, si ok, je sors de la boucle et je retourne amount
            if amount > 0: 
                break # on sort de la boucle
            else: 
                print("Amount must be greater than 0.") # prompt si la valeur est négative
        else: 
            print("Please enter a number")

    return amount # ma fonction retourne la valeur entrée par l'utilisateur

# j'appelle ma fonction
# deposit()

def get_number_of_lines():
    while True: 
        lines = input("Enter the number of lines (1-" + str(MAX_LINES) + ")? ") # syntaxe pour afficher entre 1 et MAX_LINES
        if lines.isdigit():
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES: # lines doit être compris entre 1 et MAX_LINES
                break
            else: 
                print("Enter a valid number of lines") 
        else: 
            print("Please enter a number")

    return lines 

# je créé une fonction principale pour exécuter mon script
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()