add = int(input("Quel est le montant de l'addition ? : "))
pourb = int(input("Quel est le pourcentage du pourboire ?: "))

print(f"Le pourboire fait : {pourb/100 * add:.2f} , le total fait donc : {add + (pourb/100 * add):.2f}")