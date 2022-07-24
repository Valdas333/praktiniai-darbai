# Overriding
class Gyvunas():
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva
        
    def begti(self):
        print("Begu")
        
        
class Sou(Gyvunas):
    def begti(self):
        super().begti() # keiciam su super
        print("Bega greitai")
        

class Kate(Gyvunas):
    pass


class Karve(Gyvunas):
    pass


sou1 = Sou("Rikis", "pilka")
kate1 = Kate("Murkis", "rainas")
karve1 = Karve("Marge", "Ruda")

sou1.begti()
kate1.begti()
karve1.begti()


class Tevas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Vaikas(Tevas):
    def __init__(self, vardas, pavarde, mokykla):
        super().__init__(vardas, pavarde)
        self.mokykla = mokykla
    
    
tevas = Tevas("Gintautas", "Paskauskas")
vaikas = Vaikas("Gintare", "Lauciene", "KTU")

print(vaikas.mokykla)