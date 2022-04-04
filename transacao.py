import time 
import sys
from banco import insert
from datetime import datetime

def transaction(range):
    tempo_inicial = (time.time())

    lista = []

    for item in range:
        lista.append(item)
        tempo_append = (time.time())

        tempo_final = (tempo_append - tempo_inicial)
        tamanho = sys.getsizeof(lista)
        values = (tempo_final, tamanho, datetime.today())
        insert(values)



transaction(range (100000, 600000, 100000))
transaction(range (1000, 6000, 100))
transaction(range (100, 600, 100) )
transaction(range (10, 60, 10))
transaction(range (1000000, 6000000, 1000000))