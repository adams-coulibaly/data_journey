nb_min = int(input("Donnez un nombre de minutes entier !: "))
h = nb_min // 60
m = nb_min % 60

if nb_min >= 60:
    print(f"{h} h {m} min")
else:
    print(f"{m} min")
