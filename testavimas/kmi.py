def kmi(svoris, ugis):
    try:
        svorisgeras = int(svoris)
        ugisgeras = int(ugis)
    except ValueError:
        raise ValueError
    if svoris <= 20 and ugis <= 1.40:
        raise ValueError
    elif svoris >= 240 and ugis <= 1.40:
        raise ValueError
    elif svoris <= 80 and ugis <= 0.40:
        raise ValueError
    elif svoris <= 80 and ugis >= 3.40:
        raise ValueError
    else:
        return svoris/(pow(ugis, 2))
    
    

