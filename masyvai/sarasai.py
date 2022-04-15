
def min_values_change():
    """
    funkcija pakeiciai minreiksmes 
    is skaiciu saraso musu norimu simboliu
    ir atspausdina mmin.reiksme ir sarasa
    """    
    import random
    replace_symbol = str(input("Ivesk pakeitimo simboli: "))
    skaiciu_sarasas = []
    for skaicius in range(0, 20):
        skaiciu_sarasas.append(random.randint(0, 10))
    
    min_value = skaiciu_sarasas[0]
    for number in skaiciu_sarasas:
        if min_value > number:
            min_value = number
            
    print(min_value)
    count = skaiciu_sarasas.count(min_value)
    for i in range(len(skaiciu_sarasas)):
        if skaiciu_sarasas[i] == min_value:
            skaiciu_sarasas[i] = replace_symbol
            
    print(skaiciu_sarasas)


def max_values_change_with_try_and_catch():
    """
    bandymas rasti su try and catch metodu rasti skaiciu max reiksmes
    ir jas pakeisti skaiciumi is inputo
    Nepabaigta yra klaidos !!!
    """    
    import random
    skaiciu_sarasas = [random.randint(-5,5) for x in range(10)]
    print(skaiciu_sarasas)
    ivestis = input("Iveskite pakeitimo symboli:")
    while True:
        if ivestis =="X":
            print('Bye, bye')
            break
        try:
            ivestis = int(input("Iveskite pakeitimo symboli:"))
        except Exception as error:
            print(f"Klaida: {error}, bandykite dar karta")
        else:
            break
        finally:
            print("----")
    maximumas = max(skaiciu_sarasas)
    rezultatas = [ivestis if x == maximumas else x for x in skaiciu_sarasas]
    print(rezultatas)


def atsityktiniu_skaiciu_masyvo_generatorius():
    """
    funkcija skirta generuoti atsityktiniu 
    skaiciu masyva
    """
    import random    
    atsityktiniu_skaiciu_masyvas = [random.randrange(0, 10) for i in range(10, 20)]
    print(atsityktiniu_skaiciu_masyvas)