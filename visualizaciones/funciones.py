import matplotlib.pyplot as plt
from seaborn import catplot

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


def redondeo(numero) -> int:
    return round(numero)

def hasta_mil(numero):
    if numero > 1000:
        return 1000
    return numero

def hasta_10_mil(numero):
    if numero > 10000:
        return 10000
    return numero

def hasta_100_mil(numero):
    if numero > 100000:
        return 100000
    return numero

def hasta_un_millon(numero):
    if numero > 1000000:
        return 1000000
    return numero

def hasta_10_milllones(numero):
    if numero > 10000000:
        return 10000000
    return numero

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

def barplot(df, monto):
    return catplot(data=df, x="Tipo de producto", y=monto, hue="Tarjeta", kind="bar", col="Transaccion")