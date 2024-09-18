#                   FUNCIONES   INVOLUCRADAS    PARA    LAS     VISUALIZACIONES

import matplotlib.pyplot as plt

def tipo_transferencia(numero) -> str:
    if numero == 0:
        return "Legal"
    else:
        return "Fraude"

def monto_en_rangos(numero) -> int:
    rangos = list(range(0, 1001, 100))

    for rango in rangos:
        if numero < rango:
            return rango
    return rangos[len(rangos) - 1]

def cargar_rango(rango) -> str:
    rangos = list(range(0, 1001, 100))
    indice = rangos.index(rango)

    return f"({rangos[indice - 1]} - {rangos[indice]}]"

def cantidad_producto(letra) -> int:
    if letra == 'C' or letra == 'H' or letra == 'R' or letra == 'S' or letra == 'W':
        return 1
    else:
        return 0

def dia(tiempo) -> int:
    dia = (tiempo - 86400) / 86400
    if dia > round(dia):
        return int(round(dia) + 1)
    else:
        return int(round(dia))
    
def scatter(x1, x2, y1, y2):
    legal = plt.scatter(x=x1, y=y1, c="green", s=7)
    fraude = plt.scatter(x=x2, y=y2, c="red", s=30, marker="^", edgecolors="black", linewidths=1)
    legal.set_label("Legal")
    fraude.set_label("Fraude")
    plt.title("Transacciones a lo largo del Tiempo")
    plt.xlabel("Tiempo en Dias")
    plt.ylabel("Monto en $")
    plt.legend()
    plt.show()