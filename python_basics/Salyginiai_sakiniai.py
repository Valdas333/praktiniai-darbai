import math 


def veiksmaiSuSkaiciais():
    """
    Įveskite skaičių (input). Jei jis yra teigiamas, ištraukti iš jo šaknį, 
    kitu atveju pakelti kvadratu. Skaičius gali būti ir realusis (float).
    """
    sk = float(input("Įveskite skaičių:"))
    if sk == 0:
        print("Ivestas 0")
    if sk < 0:
        print(f"Skaičius {sk} pakeltas kvadratu yra lygus {(math.pow(sk, 2))}")
    else: 
        print(f"Skaičiaus {sk} šaknis yra {(math.sqrt(sk))}")
            

def skaiciaus_diapozonas():
    """
    Įveskite skaičių (input). Jei skaičius patenka į diapazoną iki 0 skaičių pakelti kvadratu;
    Jei skaičius patenka iki 10 - kubu, visos kitos reikšmės - išvesti į ekraną “kitas diapazonas”
    """
    sk = float(input("Įveskite skaičių:"))
    if sk <=0:
        print(f"Skaičius {sk} pakeltas kvadratu yra lygus {(math.pow(sk, 2))}")
    elif sk <= 10:
        print(f"Skaičius {sk} pakeltas kubu yra lygus {(math.pow(sk, 3))}")
    else:
        print(f"Skaičiaus {sk} yra kitame diapozone")
        
    
def didziausias_skaicius():
    """
    Įveskite (input) tris skaičius. Reikia išrinkti didžiausią reikšmę. 
    Po to print pagalba išvesti atsakymą, nurodant konkrečias skaitines kintamųjų reikšmes.
    """
    sk = float(input("Įveskite pirmą skaičių:"))
    sk1 = float(input("Įveskite antrą skaičių:"))
    sk2 = float(input("Įveskite trečią skaičių:"))
    
    if sk > sk1 and sk > sk2:
        print(f"{sk}")
    elif sk1 > sk2 and sk1 < sk:
        print(f"{sk1}")
    else:
        print(f"{sk2}")


def alkoholio_istatymas():
    """
    Alkoholio įstatymas teigia, kad asmenims, jaunesniems nei 21 metai, alkoholis neparduodamas. 
    Įveskite savo amžių (input). Jeigu asmuo yra jaunesnis nei 21 metai išveskite print:
    pranešimą - alkoholis neparduodamas! Kitu atveju - pranešimą - gerkite saikingai!
    """
    age = int(input("Iveskite Jusu amziu:"))
    if age < 21:
        print("Esi per jaunas!")
    else:
        print("gerkite saikingai!")
            
    
def ugio_tikrinimas():
    """
    Vandens atrakcionų parke nuo raudonos kaskados gali leistis asmenys, ne žemesni nei 1,6 metro, o nuo juodos - ne žemesni nei 1,8 metro. 
    Įveskite savo ūgį - jeigu jūsų ūgis yra 1,8 metro ir daugiau spausdinkite pranešimą - Jūs galite leistis juodomis kaskadomis! Jei jūsų ūgis yra ne mažesnis nei 1,6 metro
    Jūs galite leistis raudonomis kaskadomis. Kitu atveju - Jūs esate per jauni šiai pramogai!
    """
    personHeigh = float(input("Iveskite savo ugi:"))
    personMinHeightForRedTrack = 1.60
    personMinHeightForBlackTrack = 1.80
    if personHeigh <= personMinHeightForRedTrack:
        print("Jūs esate per jauni šiai pramogai!")
    elif personHeigh >= personMinHeightForRedTrack:
        print("Jūs galite leistis raudonomis kaskadomis")
    else:
        print("Jūs galite leistis juodomis kaskadomis!")
        
   
def mano_funkcija():
    user_name = input("Iveskite varda")
    print(user_name)
    
    
