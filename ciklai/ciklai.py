my_array = [9, 10]

def print_each_second_element():
    """
    nepaibagtas!!!
    """
    tekstas = "Special cases aren't special enough to break the rules."
    # for i in range(0, len(tekstas), 2):
    #     print(tekstas[i])
    counter = 1  
    for i in tekstas:
        print(i)
        print(tekstas[counter::1], end="")
        counter += 1
 
    
def random_array_gen():
    """
    Funkcija atlieka saraso sugenaravima is 
    atsitiktiniu skaiciu, kuriu reziai yra apibreziami kintamuosiuse 
    """
    import random
    reziu_pradzia = 1
    reziu_pabaiga = 10
        
    random_suformuotas_sarasas = []

    for skaicius in range(reziu_pradzia, reziu_pabaiga):
        skaicius = random.randrange(0, 15)
        random_suformuotas_sarasas.append(skaicius)
    print(random_suformuotas_sarasas)


def average_from_list(a):
    """
    Randa saraso vidurki su for ciklo pagalba

    Args:
        a (array): skaiciu sarasas
    """
    suma = 0
    for j in a:
        suma = suma + j
    vidurkis = suma / len(a)
    print(f"Suformuoto saraso vidurkis: {vidurkis}")


def maxValue_from_list(a):
    maksikamali_reiksme = a[0]
    for i in a:
        if i > maksikamali_reiksme:
            maksikamali_reiksme = i
    print(f"max reiksme yra: {maksikamali_reiksme}")
        

def min_value_from_list(skaiciu_sarasas):
    """Funkcija randa skaiciu sarase min reiksme

    Args:
        skaiciu_sarasas (array): skaiciu sarasas
    """    
    min_value = skaiciu_sarasas[0]
    for number in skaiciu_sarasas:
        if min_value > number:
            min_value = number


def pazymiu_vidurkio_skaiciuotuvas():
    """
    Funkcija suskaiciuoja pazymiu vidurkis ir jeigu vidurkis yra maziau nei 4.5
    atspausdina vidurki ir atspausdina kad reikia laikyti egzamina
    """    
    import random
    suma = 0
    pazymiu_sarasas = []
    ivedimas = ""
    while ivedimas != "b":

        pazymis = int(input("Iveskite pazymi:"))
        if pazymis <= 0:
            print("Sukciaujate, ivesta maziau uz 0,")
            ivedimas = "b"
        elif pazymis > 10:
            print("Sukciaujate, ivesta daugiau uz 10")
            ivedimas = "b"
        else:
            pazymiu_sarasas.append(pazymis)
            vidurkis = sum(pazymiu_sarasas) / len(pazymiu_sarasas)
    
            ivedimas = str(input("Jei norite testi spauskite bet koki klavisa, b jei pabaigti suvedineti , jei norite gauti vidurkį spauskite a:"))
            if ivedimas == "a":
                if vidurkis < 4.5:
                    print(f"Jums reikia laikyti egzamina, jūsų balo vidurkis yra: {vidurkis}")
                if vidurkis >= 4.5:
                    print(f"Jusu vidurkis yra {vidurkis +1}")
                print("Vidurkis yra : %0.0f"%(vidurkis))  
                print("this line for testing purposes", pazymiu_sarasas)


def elementu_skaicuotuvas():
    """
    Funkcija atlieka trys veiksmus, 
    generuoja atsitiktinius skaicius pagal vartotojo reikalavimus 
    reiketu dar patobulinti ivedamos komandos patikrinimas ar yra ivesta 
    teisingo formato simbolis
    """    
    import random
    choice = str(input("""Iveskite koki norite buda pasirinkti 
                       r - tai random,
                       m - tai rankiniu,
                       visi kiti klavisa - kol bus duota 
                       sustabdymo komanda yra klavisas e
                       Jusu pasirinkimas: """))

    end_symbol = ""
    skaiciu_sarasas = []
    lyginiai_skaiciai = []
    nelyginiai_skaiciai = []
    
    if choice == "r":
        a = int(input("Iveskite generatoriaus pradzios intervala: "))
        b = int(input("Iveskite skaiciu generatoriaus pabaigos intervala: "))
        c = int(input("Iveskite diapozono pradzia: "))
        d = int(input("Iveskite diapozono pabaiga: "))
        for i in range(c, d, 1):
            i = skaiciu_sarasas.append(random.randrange(a,b))
        
        for skaicius in skaiciu_sarasas:
            if skaicius % 2:
                nelyginiai_skaiciai.append(skaicius)
            else:
                lyginiai_skaiciai.append(skaicius)
                
        print(f"Lyginiai skaiciai yra {lyginiai_skaiciai}")
        print(f"Nelyginiai skaiciai yra {nelyginiai_skaiciai}")
    
    elif choice == "m":
        while end_symbol != "e":     
            ivedamas_skaicius = input("Jei norite nutraukti automatini ivedima, spauskite e klavisa:")
            if ivedamas_skaicius == "e":
                for skaicius in skaiciu_sarasas:
                    if skaicius % 2:
                        nelyginiai_skaiciai.append(skaicius)
                        
                    else:
                        lyginiai_skaiciai.append(skaicius)
                print(f"Lyginiai skaiciai yra {lyginiai_skaiciai}")
                print(f"Nelyginiai skaiciai yra {nelyginiai_skaiciai}")
                end_symbol = "e"
            if ivedamas_skaicius != "e":
                ivedamas_skaicius = int(ivedamas_skaicius)            
                skaiciu_sarasas.append(ivedamas_skaicius)
                      
    else:
        while end_symbol != "e":       
            skaiciu_sarasas.append(random.randint(1, 10))
            end_symbol = str(input("Jei norite nutraukti automatini ivedima, spauskite e klavisa:"))
            if end_symbol == "e":
                for skaicius in skaiciu_sarasas:
                    if skaicius % 2:
                        nelyginiai_skaiciai.append(skaicius)
                        
                    else:
                        lyginiai_skaiciai.append(skaicius)
                print(f"Lyginiai skaiciai yra {lyginiai_skaiciai}")
                print(f"Nelyginiai skaiciai yra {nelyginiai_skaiciai}")
            
            
def lyginiu_nelyginiu_skaiciu_filtravimas_su_list_compr():
    import random
    skaiciu_sarasas = [random.randint(-5,5) for x in range(10)]
    # nelyginiai_skaiciai = [x for x in skaiciu_sarasas if x %2]
    # lyginiai_skaiciai = [j for j in skaiciu_sarasas if j not in nelyginiai_skaiciai]
    
    # for skaicius in skaiciu_sarasas:
    #     if skaicius % 2:
    #         nelyginiai_skaiciai.append(skaicius)
    #     else:
    #         lyginiai_skaiciai.append(skaicius)
    lyginiai_skaiciai = []
    nelyginiai_skaiciai = []
    [lyginiai_skaiciai.append(x) if x%2==0 else nelyginiai_skaiciai.append(x) for x in skaiciu_sarasas]
    print(f"Lyginiai_skaiciai yra: \n {lyginiai_skaiciai}")
    print(f"Nelyginiai skaiciai yra: \n {nelyginiai_skaiciai}")
    

def matricu_skaiciavimas_su_numpy():
    """
    Duota matrica A. 
    Matricos kopijoje išrinkite visus lyginius elementus. 
    Kitus elementus paverskite nuliais
    """    
    import numpy as np
    A = np.array([[4 ,5 ,2 ,1 ,8 ,4],
                [6 ,1 ,1 ,4 ,5 ,2],
                [2 ,2 ,1 ,7 ,2 ,3],
                [7 ,9 ,6 ,1 ,7 ,2],
                [1 ,7 ,1 ,7 ,4 ,7],
                [7 ,3 ,4 ,3 ,8 ,2]])
    
    A_Copy = []
    
    for element in A:
        if element %2 != 0:
            A_Copy.append(0)
    
    filtered_array = A[A_Copy]
    print(filtered_array)
    
