class Gyvunas():
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva
        
    def begti(self):
        print("Begu")
        
    
class Kate(Gyvunas):
    def miaukseti(self):
        print("Miaukseti")
        
        
class Sou(Gyvunas):
    def loti(self):
        print("Loti")
        

class Karve(Gyvunas):
    def mukia(self):
        print("Mukia")
        
        
vezlys = Gyvunas("Toto", "Ruda") 
vezlys.begti()
       
kate1 = Kate("Murkis", "rainas")
kate1.begti()