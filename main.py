import random

MAX_LINES = 3 # Pour déclarer une variable j'écris en lettres capitales (convention Python)

MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# attribution des symboles 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    # sélectionner la ligne
    winnings = 0
    winning_lines = [] # sur quelle ligne on gagne
    for line in range(lines):
        symbol = columns[0][line] # on vérifie dans la première colonne, la line actuelle
    for column in columns: # vérifier que les symboles d'une colonne sont égaux
        symbol_to_check = column[line]
        if symbol != symbol_to_check:
            break # si le symbol est différent du symbole précédent, on sort du cas
    else:
        winnings += values[symbol] * bet
        winning_lines.append(lines + 1) # +1 car c'est un index, on veut afficher 

    return winnings, winning_lines
        

def get_slot_machine_spin(rows, cols, symbols):
    # algo aleatoire

    all_symbols = []
    for symbol, symbol_count in symbols.items(): # key, value => loop
        for _ in range(symbol_count): # "_" variable anonyme 
            all_symbols.append(symbol)# append = ajouter la donnée dans le tableai init


    columns = []
    for _ in range(cols):
        column = []
        # ici on retire le symbole déj) séléectionné pour ne pas dépasser la valeur par exemple max 2 fois le A
        # pour ça on copie la liste avec [:], on ne modifie par la source directement mais une copie
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# ici on cherche à afficher nos colonne sous le bon format, on transpose
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # on définit l'index max
                print(column[row], end=" | ") # on modifie la end line afin d'éviter le comportement par défaut (saut à la ligne)
            else: 
                print(column[row], end="")

        print()



# Je déclare une fonction 
def deposit() : 
    # Je créé une boucle et je teste les différentes conditions. 
    while True: 
        amount = input("What would you like to deposit? $ ") # input permet à l'utilisateur d'intégrer une donnée
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

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? ") 
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET: 
                break 
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}") # cette syntaxe converti directement mes nombres en string - f
        else: 
            print("Please enter a number")

    return amount


# je créé une fonction principale pour exécuter mon script
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance: 
            print(f"You do not have enought to bet that amount, your current balance is ${balance}")
        else: 
            break


    total_bet = bet * lines
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to :${total_bet}")
    # print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines: ", *winning_lines) # "*" spread operator en Python, on passe toutes les lignes dans le print

main()