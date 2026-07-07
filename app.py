import os
risk = 0.85
print("Calculate Risk :" + str(risk))

def tiempo_total_espera(reintentos_max:int, espera_inicial:int, razon:int) -> int:
    if reintentos_max <= 0:
        return 0
    return espera_inicial*(razon**reintentos_max-1)/(razon-1)