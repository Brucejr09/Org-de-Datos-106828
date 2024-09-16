import matplotlib.pyplot as plt

def tipo_transferencia(numero) -> str:
    if numero == 0:
        return "Legal"
    else:
        return "Fraude"

def cantidad_producto(letra) -> int:
    if letra == 'C' or letra == 'H' or letra == 'R' or letra == 'S' or letra == 'W':
        return 1
    else:
        return 0

def ids(lista_1, lista_2):
    lista = []
    for id in lista_2:
        try:
            lista_1.remove(id)
            lista.append(True)
        except ValueError:
            lista.append(False)
    return lista

def unicidad_sistema(string) -> str:
    lista = ["WINDOWS", "MOTO", "SAMSUNG", "LG", "SM", "GT", "RV", "ZTE", "HUAMWI", "IOS DEVICE","MACOS", "NOKIA", "ALCATEL", "IPHONE" ,"BUILD"]
    for sistema in lista:
        match string.upper().find(sistema):
            case -1:
                continue
            case _:
                return sistema
    return "OTRO"

def unicidad_modelo(string) -> str:
    lista = ["CHROME", "SAFARI", "FIREFOX", "SAMSUNG", "OPERA", "EDGE", "ANDROID"]
    for modelo in lista:
        match string.upper().find(modelo):
            case -1:
                continue
            case _:
                return modelo
    return "OTRO"

def segundo(tiempo) -> int:
    return tiempo - 86400

def minuto_hora(tiempo) -> int:
    minuto_hora = tiempo / 60
    if minuto_hora > round(minuto_hora):
        return int(round(minuto_hora) + 1)
    else:
        return int(round(minuto_hora))
    
def dia(tiempo) -> int:
    dia = tiempo / 24
    if dia > round(dia):
        return int(round(dia) + 1)
    else:
        return int(round(dia))
    
def semana(tiempo) -> int:
    semana = tiempo / 7
    if semana > round(semana):
        return int(round(semana) + 1)
    else:
        return int(round(semana))

def mes(tiempo) -> int:
    mes = tiempo / 4
    if mes > round(mes):
        return int(round(mes) + 1)
    else:
        return int(round(mes))

def barplot(eje_x, barras, titulo: str, nombre_x: str, nombre_y: str, con_legal: bool):
    fraude = plt.bar(eje_x, barras[0], color='red')
    fraude.set_label("Fraude")
    legal = plt.bar(eje_x, barras[1], bottom=barras[0], color='green')
    legal.set_label("Legal")
    plt.xticks(rotation=90)
    plt.title(titulo)
    plt.xlabel(nombre_x)
    plt.ylabel(nombre_y)
    if con_legal:
        plt.bar_label(legal)
    plt.bar_label(fraude)
    plt.legend()
    plt.show()