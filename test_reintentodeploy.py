#import pytest
from app import tiempo_total_espera
# Caso 1: Tu prueba original (Happy Path + Filtros)
def test_procesar_reintento_exito():
    assert tiempo_total_espera(3,2,3) == 26

# Caso 2: Caso borde con lista completamente vacía
def test_procesar_reintento_vacia():
    assert tiempo_total_espera(0,0,0) == 0