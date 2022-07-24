import datetime

class Darbuotojas:
   
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        self.esamas_laikas = datetime.datetime.today()       
        
    def __nudirbta_valandu(self):
        dirbta_valandu = self.esamas_laikas - self.dirba_nuo
        dirbta_valandu = dirbta_valandu.days
        return dirbta_valandu
    
    def atlyginimo_skaciuokle(self):
        atlyginimas = self.__nudirbta_valandu() * 8
        return atlyginimas * self.valandos_ikainis

  
class NormalusDarbuotojas(Darbuotojas):
    
    def atlyginimo_skaciuokle(self):
        valandu_kiekis = super().__nudirbta_valandu()
        atlyginimas = valandu_kiekis
   
        return atlyginimas * self.valandos_ikainis
    
    
    
          
darbuotojas1 = Darbuotojas("Petras", 8, datetime.datetime(2022, 4, 20))
print(darbuotojas1.atlyginimo_skaciuokle())
darbuotojas2 = NormalusDarbuotojas("Kestas", 8, datetime.datetime(2022, 4, 20))
print(darbuotojas2.atlyginimo_skaciuokle())