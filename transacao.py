import time 
import sys
import matplotlib.pyplot as plt

def transaction(range):
    tempo_inicial = (time.time())
    x_points = []
    y_points = []

    lista = []

    for item in range:
        lista.append(item)
        tempo_append = (time.time())

        tempo_final = (tempo_append - tempo_inicial)
        x_points.append(tempo_final*100)
        y_points.append(sys.getsizeof(lista))

    print(lista)
    plt.plot(x_points,y_points)


# transaction(range (100000, 600000, 100000))
transaction(range (1000, 6000, 100))
# transaction(range (100, 600, 100) )
# transaction(range (10, 60, 10))
# transaction(range (1000000, 6000000, 1000000))

plt.show() 