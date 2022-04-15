
def konvertuoti_skaicius():
    """konvertuoti juos į sveikuosius ir realiuosius. Realieji skaičiai 4 skaitmenys po
        kablelio
    """
    pirmasSkaicius = int(input("Iveskite pirmas skaiciu(sveikaji):"))
    antrasSkaicius = float(input("Iveskite antra skaiciu(realuji su kableliu):"))
    print("Pirmas skaicius konvertuotas i sveikaji %1d ,antras skaicius i realuji %1.4f"%(pirmasSkaicius,antrasSkaicius))
    
  
def skaiciu_pavertimas_string():
    """
        atlikti veiksmus, kad būtų sudedami visi skaitmenys vienas šalia kito (tai nėra
        aritmetinės sudėties veiksmas) 
    """
    pirmasSkaicius = int(input("Iveskite pirma skaiciu:"))
    antrasSkaicius = float(input("Iveskite antra skaiciu:"))
    print(str(pirmasSkaicius) + str(antrasSkaicius))
    
       
def sudaryti_skaiciu_kintamuosius():
    import math
    """
    Input pagalba sudaryti nelyginių skaičių sąrašą pradedant -1 iki 5
    """
    pirmasSkaicius = int(input("Iveskite pirma skaiciu:"))
    antrasSkaicius = int(input("Iveskite antra skaiciu:"))
    treciasSkaicius = int(input("Iveskite trecia skaiciu:"))
    ketvirtaskaicius = int(input("Iveskite ketvirta skaiciu:"))
    suma = pirmasSkaicius + antrasSkaicius + treciasSkaicius + ketvirtaskaicius
    pirmasSkaicius = 4
    daugiklis = int(input("Iveskite laipnsio daugikli:"))
    skaiciusPakeltasLaipsniu = pirmasSkaicius ** daugiklis
    antrasSkaicius = math.sqrt(skaiciusPakeltasLaipsniu)
    print(antrasSkaicius)
    suapvalintas_skaicius = round(antrasSkaicius)
    print(suapvalintas_skaicius)
    
    
