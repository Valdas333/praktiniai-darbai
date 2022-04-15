# 1. susikurti zurnala (sarasas)
# 2. vartotojo meniukas, pirmas punkas iseiti #while, kad uzdarytu pasidaryti arba testi
# 3. galimybe itraukti irasa i zurnala
# 4. galimybe isspausdinti zurnala

# 5. suskaiciuoti balansa (suma viso zurnalo nariu)
# 6. galimybes redaguoti konkretu zurnalo irasa
# 7. galimybe trinti konkretu zurnalo irasa 
#100 eiluciu
#pirmus 4 jis padare


zurnalas = []
while True:
    ivedimas = input("""### Balansas ###
    0: iseiti,
    1: suskurti irasa
    2: isspasudinti zurnala,
    3: suskaiciuoti balanasa,
    4: keisti
    pasirinkite: """)
    zurnalo_ilgis = len(zurnalas)
    if ivedimas == "0":
        break
    elif ivedimas == "1":
        try:
            zurnalas.append(float(input("iveskite pajamas arba islaidas: ")))
        except ValueError:
            print("klaida: skaicius neteisingas")
    elif ivedimas == "2":
        print(zurnalas)
    elif ivedimas == "3":
        print(sum(zurnalas))
    elif ivedimas == "4" and zurnalo_ilgis == 0:
        print("Tuscias zurnalas")
    elif ivedimas == "4":
        print(zurnalas)
        keiciamas_zurnalo_irasas = int(input("iveskite, kuri irasa norite pakeisti: "))
        naujas_irasas = int(input("irasykite nauja: "))
        zurnalas[keiciamas_zurnalo_irasas] = naujas_irasas
    else:
        print(f"klaida: {ivedimas} neatpazinta komanda")
    
