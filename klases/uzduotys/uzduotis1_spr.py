class Automobilis():
    
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Automobilio metai : {metai}")
        print(f"Modelis : {modelis}")
        print(f"Autombilio kuro tipas: {kuro_tipas}")
             
    def vaziuoti(self):
        
        print("Automobilis vaziuoja")
        
    def stoveti(self):
        
        print("Priparkuota")
        
    def pildyti_degalu(self):
        
        print("Degalai įpilti")
        
    def __str__(self):
        return f"{self.metai} metai, {self.modelis}, kuras {self.kuro_tipas}"
    
    def __rpr__(self):
        return f"{self.metai} metai, {self.modelis}, kuras {self.kuro_tipas}"
    

class Elektromobilis(Automobilis):
    
    def __init__(self, metai, modelis, kuro_tipas):
        super().__init__(metai, modelis, kuro_tipas)
        print("Baterija ikrauta")
        
    def pildyti_degalu(self):
        print("Baterija ikrauta")
    
    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")
        
    
auto1 = Automobilis(2010, "VW", "vanduo" )
auto2 = Elektromobilis(2010, "VW", "Elektra")
auto1.vaziuoti()
auto1.stoveti()
auto1.pildyti_degalu()

auto2.vaziuoti()
auto2.stoveti()
auto2.pildyti_degalu()
auto2.vaziuoti_autonomiskai()

print(auto2)