

from ast import arg


def pasisveikinimas(miestas, vardas, pavarde):
    return (f"Labas {vardas} {pavarde}, esate is {miestas}")    


def kelimas_kubu(skaicius):
    return pow(skaicius)


def skaicius_laipsniu(skaicius, laipsnis):
    return (f"{skaicius} pakeltas laipsniu {laipsnis} yra {pow(skaicius, laipsnis)}")


def ploto_skaiciavimas():
    """
    Sukurkite funkcija kuri apskaiciuotu staciakampio plota ir perimetra.
    vartotojas turi ivesti input staciakampio krastiniu ilgi.
    atsakyma isvesti i ekrana print
    """
    krastine_a = int(input("Iveskite krastines a ilgi:"))
    krastine_b = int(input("Iveskite krastinb_b ilgi:"))
    print(f"Plotas yra {krastine_a * krastine_b}")
    

def kvadrato_skaiciavimas(skaicius):
    kvadratu = skaicius**2
    return kvadratu
    

def triju_skaiciu_suma(skaicius_a, skaicius_b, skaicius_c):
    """
    Apsirasome funkcija kuri suskaiciuoja triju jai nurodytu argumentais skaiciu suma ir ta suma padaugina is paskutinio skaiciaus argumento.
    Atspausdina viena funkcija trys eilutes : suma, daugyba, grazina - return daugyba
    """
    suma = skaicius_a + skaicius_b + skaicius_c
    suma = suma * skaicius_c


def skaiciu_suma(sk1, sk2, sk3):
    rezultatas = sk1 + sk2 + sk3
    return rezultatas


def daug_argumentu_kvadratu(*args):
    for eiles_nr, skaicius in enumerate(args):
        print(eiles_nr+1, skaicius ** 2)


def teksto_skaidymas_ir_numeracija(*args):
    """
    Funkcijos su neribotais argumentais - isvedanti i ekrana nurodyta simboli ir jo eiles numeri.
    """
    skaidytas_tekstas = []
    for simbol in args:
        print(simbol)
        for i in simbol:
            skaidytas_tekstas.append(i)

    for eiles_nr, simbolis in enumerate(skaidytas_tekstas):
        print(eiles_nr + 1, simbolis)
  
        
def spausdinti_reiksmes(**kwargs):
    for raktazodis, reiksme in kwargs.items():
        print(raktazodis, reiksme)


def skaiciu_suma_su_neribotais_argumentais(*args):
    """
    Grazina is paduoto skaičių sąrašo, sumą ir skaiciu kieki 
    atliekama su neribotais argumentais
    Returns:
        integer : skaiciu suma ir saraso ilgi
    """
    return f"Saraso skaiciu suma yra - {sum(args)}, ilgis - {len(args)}"


def spausdinti_reiksmes(sk1, sk2, *args):
    print("Skaiciu suma:", sk1 + sk2)
    for vienas in args:
        print(vienas)
        

def daugyba_is_saves_su_lambda():
    "Neveikia !!!"
    daugyba_is_saves = [lambda i = skaicius: i*i for skaicius in range(1, 6)]
    print(daugyba_is_saves)



def didziausias_is_paduotu_skaiciu(*args):
    """
    Atspausdina didžiausią iš kelių paduotų skaičių (panaudojant *args).

    Returns:
        integer: max reiksme is saraso
    """
    maksikamali_reiksme = args[0]
    for i in args:
        if i > maksikamali_reiksme:
            maksikamali_reiksme = i
    return (f"Maksimali reiksme yra: {maksikamali_reiksme}")



def atspausdina_kiek_sakinyje_didziuju_raidziu():
    tekstas = """111Flat is better than nested.
                Sparse is better than dense.
                Readability counts.
                """

    didziosios_raides = []
    mazosios_raides =[]
    skaiciai = []
    for raide in tekstas:
        if raide.isupper():
            didziosios_raides.append(raide)
        elif raide.islower():
            mazosios_raides.append(raide)
        elif raide.isnumeric():
            skaiciai.append(raide)
            
            
          
    print(len(didziosios_raides))
    print(len(mazosios_raides))
    print(len(skaiciai))
    
    

def pirminiai_skaiciai(skaicius):
    """
    Gražintų, ar paduotas skaičius yra pirminis.
    Pirminis skaičius– bet kuris natūralusis skaičius, didesnis nei 1, 
    kuris dalinasi tik iš savęs ir vieneto.
    
    """
    counter = 0 
    for daliklis in range(1,skaicius):
        if skaicius % daliklis == 0 :
            counter += 1
    
    if counter < 2:
        print(f"Skaicius {skaicius} yra pirminis")
    else:
        print(f"Skaicius {skaicius} yra nepirminis")




