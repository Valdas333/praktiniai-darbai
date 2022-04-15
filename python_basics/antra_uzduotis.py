# import this

tekstas = "Beautiful is better than ugly."


def pasktunis_teksto_simbolis(txt):
    """Atspausdina sakinio antro zodzio paskutini simboli

    Args:
        txt (stringas): sakinys
    """
    zodziai = txt.split(" ")
    zodziai = zodziai[-2]
    zodziai = zodziai[-1]
    print(zodziai)


def pirmas_trecio_zodzio_simbolis(txt):
    """Atspausdina pirmą trečio žodžio simbolį

    Args:
        txt (string): sakinys
    """
    txt = txt.split(" ")
    txt = txt[2]
    print(txt[0])
    

def atspausdina_pirma_zodi(txt):
    """Atspausdintų tik pirmą žodį 

    Args:
        txt (string): sakinys
    """
    txt = txt.split(" ")
    print(txt[0])
    
    
def atspausdina_paskutini_zodi(txt):
    """Atspausdintų tik paskutinį žodį

    Args:
        txt (string): sakinys
    """
    txt = txt.split(" ")
    print(txt[-1])
 
 
def atspausdina_fraze_atbulai(txt):
    """Atspausdintų visą frazę atbulai

    Args:
        txt (string): fraze
    """
    print(txt[::-1])
    

def atskiria_zodzius_ir_atspausdina(txt):
    """Atskiria žodžius ir juos atspausdintų

    Args:
        txt (string): sakinys
    """
    txt = txt.split(" ")
    for i in txt:
        print(i)
    

def pakeicia_zodi(txt, zodis):
    """Norima žodį pakeistų į "Programming" ir atspausdintų naują sakinį

    Args:
        txt (string): sakinis kuriam atliekama funkcija
        zodis (string): zodis kuri norime pakeisti
    """
    x = txt.replace(zodis, "Programming")
    print(x)
    

