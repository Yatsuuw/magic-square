def check_square_magic(square):
    # Récupère l'ordre du carré
    n = len(square)

    # Calcule la somme attendue pour chaque ligne, colonne et diagonale du carré
    expected_sum = n * (n**2 + 1) // 2

    # Vérifie si la somme de chaque ligne, colonne et diagonale est égale à la somme attendue
    for i in range(n):
        row_sum = sum(square[i])
        if row_sum != expected_sum:
            print("La ligne {} ne respecte pas la condition du carré magique.".format(i))
            return False

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += square[i][j]
        if col_sum != expected_sum:
            print("La colonne {} ne respecte pas la condition du carré magique.".format(j))
            return False

    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += square[i][i]
        diag_sum2 += square[i][n-i-1]
    if diag_sum1 != expected_sum or diag_sum2 != expected_sum:
        print("Les diagonales ne respectent pas la condition du carré magique.")
        return False

    # Si toutes les sommes sont égales à la somme attendue, le carré est magique
    return True

# Demande à l'utilisateur de saisir l'ordre du carré
n = int(input("Veuillez saisir l'ordre du carré : "))

# Initialise un tableau 2D pour stocker les valeurs du carré
square = []
for i in range(n):
    row = []
    for j in range(n):
        # Demande à l'utilisateur de saisir la valeur de chaque case
        val = int(input("Veuillez saisir la valeur de la case ({},{}) : ".format(i, j)))
        row.append(val)
    square.append(row)

# Vérifie si le carré est magique
if check_square_magic(square):
    print("Félicitations ! Votre carré est magique.")
else:
    print("Désolé, votre carré ne respecte pas la condition du carré magique.")
