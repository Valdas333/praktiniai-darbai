
# s1 = int(input("Iveskite pradzios intervala: "))
# s2 = int(input("Iveskite pabaigos intervala: "))
# s3 = int(input("Iveskite zingsni:"))


# for i in range(s1, s2, s3):
#     bilietu_sarasas.append(i)


def elektroninesParduotuvesLoterija():
    """
    Funkcija is skaiciu masyvo atrenka pagal salygas 
    laimingus skaicius.
    Salygos:
    Laimingi bus bilietai, kurie be
    liekanos dalijasi iš trijų ir kurių bent vienas skaitmuo taip pat dalijasi iš trijų be liekanos
    (skaitmenys negali būti lygūs nuliui).
    Reikia dar patobulinti, nes tinkamas tik masyvas kurio skaicio simboliu kiekis yra 3
    Salyga faile "loterijos_uzduotis_apr"
    """
    
    bilietu_sarasas = []
    for i in range(100, 999):
        bilietu_sarasas.append(i)
    print(bilietu_sarasas)
    laimingu_bilietu_sarasas = []
    for i in range(0, len(bilietu_sarasas), 1):
        z = str(bilietu_sarasas[i])
        digit0, digit1, digit2 = 0, 0, 0
        digit0 = int(z[0])
        digit1 = int(z[1])
        digit2 = int(z[2])
        digit3 = int(z)
        if digit0 != 0 and digit1 != 0 and digit2 != 0:
            if digit0 %3 != 0 and digit1 %3 == 0 and digit2 %3 != 0 or digit3 %3 == 0:
                laimingu_bilietu_sarasas.append(z) 
    print(laimingu_bilietu_sarasas)
        
        

elektroninesParduotuvesLoterija()