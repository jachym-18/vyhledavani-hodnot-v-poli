# 1. Seznam čísel
seznam = [5, 12, 33, 44, 56, 78, 9, 3, 11, 67]
print("Seznam čísel:", seznam)

# 2. Uživatelský vstup pro hledané číslo
hledane_cislo = int(input("Zadej číslo které chceš v seznamu najít: "))

# 3. Hledání čísla v seznamu
found = False #nepobiram jak tohle funguje
for index, cislo in enumerate(seznam):
    if cislo == hledane_cislo:
        print(f"Našel jsem tuto hodnotu na pozici {index}!")
        found = True
        break #huh??

# 4. Číslo nebylo nalezeno
if not found:
    print("Zadaná hodnota tady není.")

#pardon pancelko ale fakt nepobiram