from datetime import date, time, datetime
import math

tekstas = "Namespaces are One honking great idea1 -- let's2 do more of those3!"


class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas
        
    def backwards(self):
        return self.tekstas[::-1]

    def lowercase(self):
        return self.tekstas.lower()

    def uppercase(self):
        return self.tekstas.upper()

    def word_place(self, place):
        splitted_text = self.tekstas.split(" ")
        return splitted_text[place]
    
    def count_of_symbols(self, symbol):
        return self.tekstas.count(symbol)
    
    def replace_element(self, symbol, replacement):
        return self.tekstas.replace(symbol, replacement)
    
    def counter(self):
        num_array, lower_array, upper_array = [] , [], []
        num_count, upper_count, lower_count = 0, 0, 0
        splitted_text = self.tekstas.split(" ")
        words_sum = len(splitted_text)
        for i in self.tekstas:
            if i.isnumeric():
                num_array.append(i)
                num_count = len(num_array)                
            elif i.isupper():
                upper_array.append(i)
                upper_count = len(upper_array)
            elif i.islower():
                lower_array.append(i)
                lower_count = len(lower_array)
              
        print(f"""Jusu sakinyje yra {words_sum} zodziu,
    skaiciu {num_count},
    didziuju raidziu {upper_count},
    mazuju raidziu {lower_count}""")
  
             
class Sukaktis:
   
    def __init__(self, metai, menesis, diena):

        self.metai = metai
        self.menesis = menesis
        self.diena = diena
        self.data = date(metai, menesis, diena)
        
    def datos_isvedimas(self):
        return date.today() - self.data
    
    def sek_isvedimas(self):
        sekundes = date.today() - self.data
        return (sekundes).total_seconds()


class Plyta:    
    def __init__(self, ilgis, plotis, aukstis):
        self.ilgis = ilgis
        self.plotis = plotis
        self.aukstis = aukstis
    
    def __str__(self):
        return f"{self.ilgis}: {self.plotis}, {self.aukstis}"
        
    def __repr__(self):
        return f"{self.ilgis}, {self.plotis}, {self.aukstis}"

    
class Siena:
    def __init__(self, vidine_plyta, isorine_plyta, ilgis, aukstis):
        self.vidine_plyta = vidine_plyta
        self.isorine_plyta = isorine_plyta
        self.ilgis = ilgis
        self.aukstis = aukstis
        self.plotis = vidine_plyta.plotis + isorine_plyta.plotis
        self.vidiniu_plytu_suma = self.get_plytu_kiekis(vidine_plyta)
        self.isoriniu_plytu_suma = self.get_plytu_kiekis(isorine_plyta) 

    def __str__(self):
        return f"Plytos ismatavimai: {self.vidine_plyta}; {self.isorine_plyta}; sienos ismatavimai: {self.ilgis}, {self.plotis}, {self.aukstis}"
        
    def __repr__(self):
        return f"Plytos ismatavimai: {self.vidine_plyta}; {self.isorine_plyta}; sienos ismatavimai: {self.ilgis}, {self.plotis}, {self.aukstis}"
    
    def get_plytu_kiekis(self, plyta):
        plytu_i_auksti = math.ceil(self.aukstis / plyta.aukstis)
        plytu_i_ilgi = math.ceil(self.ilgis/ plyta.ilgis)
        return plytu_i_auksti * plytu_i_ilgi
    
    
# pirma_plyta = Plyta(0.2, 0.07, 0.13)
# antra_plyta = Plyta(0.18, 0.05, 0.09)
# pirma_siena = Siena(pirma_plyta, antra_plyta, 10, 3)
# antra_siena = Siena(pirma_plyta, antra_plyta, 18, 2.8)
# trecia_siena = Siena(pirma_plyta, antra_plyta, 9, 2.9)
# ketvirta_siena = Siena(pirma_plyta, antra_plyta, 16, 0.8)
        
# sienu_sarasas = [pirma_siena, antra_siena, trecia_siena, ketvirta_siena]
# vidiniu_plytu_suma = 0
# isorine_plytu_suma = 0

# for siena in sienu_sarasas:
#     vidiniu_plytu_suma += siena.vidiniu_plytu_suma
#     isorine_plytu_suma += siena.isoriniu_plytu_suma
#     print(siena.vidiniu_plytu_suma, isorine_plytu_suma)
#     print(siena)
    
# print(f"Namui reikes vidiniu {vidiniu_plytu_suma} plytu ir isoriniu {isorine_plytu_suma} plytu")

class Keliai:
    def __init__(self, pavadinimas, ilgis, greitis):
        self.pavadinimas = pavadinimas
        self.ilgis = ilgis
        self.greitis = greitis
        
    def laikas_keliui(self):
        laikas_keliui = self.ilgis / self.greitis
        return laikas_keliui
        
        
mano_kelias = Keliai("Kaunas-Vilnius", 105, 110)
mano_kelias1 = Keliai("Kaunas- Alytus", 65.6, 90)
mano_kelias2 = Keliai("Vilnius- Panevezys", 136, 120)
keliu_sarasiukas= []
keliu_sarasiukas.append(mano_kelias)
keliu_sarasiukas.append(mano_kelias1)
keliu_sarasiukas.append(mano_kelias2)

keliones_laikas = (mano_kelias.ilgis / mano_kelias.greitis)+(mano_kelias1.ilgis / mano_kelias1.greitis) + (mano_kelias2.ilgis / mano_kelias2.greitis)
keliu_dictas = {"Pavadinimas": "", "Atstumas": 0, "Greits": 0}

for kelias in keliu_sarasiukas:
    keliu_dictas.update({"Pavadinimas": mano_kelias.pavadinimas})
    keliu_dictas.update({"Atstumas": mano_kelias.ilgis})
    keliu_dictas.update({"Pavadinimas": mano_kelias.greitis})
    
    
print(keliu_dictas)