#Antiguedad del sistema
def unicidad_sistema(string) -> str:
    lista = [("WINDOWS", 1985),
    ("MOTO", 1928),
    ("SAMSUNG", 1938),
    ("LG", 1995),
    ("SM", 1938),
    ("GT", 1928),
    ("RV", 1960),
    ("ZTE", 1985),
    ("HUAMWI", 1987),
    ("IOS DEVICE", 2007),
    ("MACOS", 2001),
    ("NOKIA", 1871),
    ("ALCATEL", 2004),
    ("IPHONE", 2007),
    ("BUILD", 1970)]

    for sistema in lista:
        match string.upper().find(sistema[0]):
            case -1:
                continue
            case _:
                return sistema[1]
    return 1970

#Antiguedad del modelo
def unicidad_modelo(string) -> str:
    lista = [("CHROME", 2008),
    ("SAFARI", 2003),
    ("FIREFOX", 2004),
    ("SAMSUNG", 1938),
    ("OPERA", 1995),
    ("EDGE", 2015),
    ("ANDROID", 2007)]
    
    for modelo in lista:
        match string.upper().find(modelo[0]):
            case -1:
                continue
            case _:
                return modelo[1]
    return 1996