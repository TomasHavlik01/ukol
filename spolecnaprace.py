jidloJedna = int(input("Kolik kalorií mělo jidloJedna?"))
jidloDva = int(input("Kolik kalorií mělo jidloDva?"))
jidloTri = int(input("Kolik kalorií mělo cisloTri?"))
celkove_kalorie = (jidloJedna + jidloDva + jidloTri)
print(celkove_kalorie)
sportovníAktivita1 = input("co jste dělal za sport: ")
sportovníAktivita2 = input("co jste dělal za druhý sport: ")
čas1 = int(input("kolik minut první sport: "))
čas2 = int(input("kolik minut druhý sport: "))
celkovy_vydej = ((čas1 + čas2) * 5)
print(celkovy_vydej)

součetKalorií = (celkove_kalorie - celkovy_vydej)
if součetKalorií > 0:
    print("přebytek kalorií")
elif součetKalorií < 0: 
    print("nedostatek kalorií")


