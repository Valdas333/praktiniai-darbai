# import datetime

# while True:
#     now=datetime.datetime.now()
#     edited=now.strftime('%H:%M:%S')
#     print(' ',edited,end='\r')


# class Gyvunas():
#     def __init__(self,vardas,spalva):
#         self.vardas=vardas
#         self.spalva=spalva

#         print('Gyvuno klase.Ivykdyta')
    
#     def miaukseti(self,zinute='miau miau'):
#         print(zinute)

# class Kate(Gyvunas):
#     def __init__(self,vardas,spalva,pomegiai):
#         super().__init__(vardas,spalva)
#         self.pomegiai=pomegiai

#         print('Kates klase.Ivykdyta')

#     def miaukseti(self):
#         super().miaukseti(zinute='miau')
          
        
# class Suo(Gyvunas):
#     pass


# kate1=Kate('Zirnis','juoda','miegoti')
# kate1.miaukseti()

# topas=Suo('TOPAS','JUODA')
# topas.miaukseti()


# print(isinstance())



# class Automobilis():
#     def __init__(self,metai,modelis,kuro_tipas):
#         self.metai=metai
#         self.modelis=modelis
#         self.kuro_tipas=kuro_tipas
         
#         print(self.metai,self.modelis,self.kuro_tipas)

#     def vaziuoti(self,zinute='Vaziuoja'):
#         print(zinute)
#     def stoveti(self):
#         print('Priparkuota')
#     def pildyti_degalu(self):
#         print('Degalai ipilti')



# class Elektromobilis(Automobilis):
#     def pildyti_degalu(self):
#         print('Baterija ikrauta')
#     def vaziuoti(self):
#         super().vaziuoti(zinute='Vaziuoja autonomiskai')
       
    

# masina1=Automobilis(1860,'gaz','dyzelis')
# masina2=Elektromobilis(2022,'Tesla','elektra')

# masina1.vaziuoti()
# masina2.vaziuoti()

# masina1.stoveti()
# masina2.stoveti()


# masina1.pildyti_degalu()
# masina2.pildyti_degalu()


import datetime

class Darbuotojas():
    def __init__(self,vardas,valandos_ikainis,dirba_nuo):
        self.vardas=vardas
        self.valandos_ikainis=valandos_ikainis
        self.dirba_nuo=datetime.datetime.strptime(dirba_nuo,'%d-%m-%Y')
    
    def nudirbo(self):
        siandien=datetime.datetime.now()

        dirba=siandien-self.dirba_nuo

        print(f'Isviso dirbo {dirba.days} dienu')
        return dirba.days
        
    def apskaiciuoti_atlyginima(self,dirba):
        valandos=dirba*8
        alga=valandos*self.valandos_ikainis

        print(f'Atlyginimas  {alga}')


darbuotojas1=Darbuotojas('Tadas',15,'19-04-2022')

valandos=darbuotojas1.nudirbo()
darbuotojas1.apskaiciuoti_atlyginima(valandos)


class NormalusDarbuotojas(Darbuotojas):
    def apskaiciuoti_atlyginima(self, dirba):
        alga=0
        valandos=0
        for i in range(dirba):
            data=self.dirba_nuo +datetime.timedelta(days=i)
            data=data.strftime('%A')
            if data=='Saturday' or data== 'Sunday':
                pass
            else:
                valandos+=8
                alga+=self.valandos_ikainis*8

        print(f'Atlyginimas uz {valandos} valandas yra {alga}')
      

darbuotojas2=NormalusDarbuotojas('Tadas',15,'05-04-2022')
dirba=darbuotojas2.nudirbo()
darbuotojas2.apskaiciuoti_atlyginima(dirba)



