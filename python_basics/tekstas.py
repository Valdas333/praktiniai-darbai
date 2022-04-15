
def teksto_isvedimas():
    tekstas = str(input("Iveskite teksta: "))
    """išveda tekstą ivesta rezultatų lange

    Args:
        nera
    """
    print("Jusu ivestas tekstas:", tekstas)
    
 
def teksto_ilgis():
    """
    Grazina ivesto teksto ilgi
    """
    tekstas = str(input("Iveskite teksta: "))
    print("Ivesto teksto ilgis:", len(tekstas))   
    
    
def teksto_isvedimas_didziosiomis():
    """
    Grazina tekstą didžiosiomis raidėmis
    """
    tekstas = str(input("Iveskite teksta: "))
    print(tekstas.upper())
    
    
def rasti_simbolio_fragmento_vieta():
    """
    Input pagalba surasti tekste simbolio ar fragmento vietą
    """
    tekstas = str(input("Iveskite teksta: "))
    fragmentas = str(input("Iveskite ieskoma fragmenta: "))
    print(tekstas.index(fragmentas))
    

def simboliu_skaiciu_kiekis():
    """
    Input pagalba rasti įvesto simbolio skaičių tekste
    """
    tekstas = str(input("Iveskite teksta: "))
    fragmentas = str(input("Iveskite ieskoma fragmenta: "))
    print(tekstas.count(fragmentas))
    
        
def pakeisti_teksto_fragmenta():
    """
    Input pagalba pakeisti teksto fragmentą kitu tekstu
    """
    tekstas = str(input("Iveskite teksta: "))
    fragmentas = str(input("Iveskite norima pakeisti fragmenta: "))
    fragmentas_pakeisti = str(input("Iveskite i koki norima pakeisti fragmenta: "))
    print(tekstas.replace(fragmentas, fragmentas_pakeisti))    


def istrinti_pasirinkta_elementa():
    """
    Input pagalba ištrinti pasirinktą teksto fragmentą
    """
    tekstas = str(input("Iveskite teksta: "))
    fragmentas = str(input("Iveskite norima istrinti fragmenta: "))
    print(tekstas.replace(fragmentas,"")) 
    
    
                    # SKAICIAI
               
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
    


