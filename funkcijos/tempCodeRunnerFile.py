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
        
