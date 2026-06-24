import numpy as np
import matplotlib.pyplot as plt

# Parámetros del AG
TAM_POBLACION = 10
LONGITUD_CROMOSOMA = 8
PC = 0.8 # Probabilidad de cruce
PM = 0.05 # Probabilidad de mutación
GENERACIONES = 50

# 1. Generación inicial
def generar_poblacion(tam, longitud):
    return np.random.randint(0, 2, (tam, longitud))

# 2. Función de fitness
def fitness(individuo):
    return np.sum(individuo)

# 3. Selección por torneo
def seleccion_torneo(poblacion, k=2):
    indices = np.random.choice(len(poblacion), k)
    mejor = max(indices, key=lambda i: fitness(poblacion[i]))
    return poblacion[mejor]

# 4. Cruce de un punto
def cruce(padre1, padre2, pc=PC):
    if np.random.rand() < pc:
        punto = np.random.randint(1, len(padre1))
        hijo = np.concatenate([padre1[:punto], padre2[punto:]])
        return hijo
    return padre1.copy()

# 5. Mutación por inversión de bit
def mutar(individuo, pm=PM):
    for i in range(len(individuo)):
        if np.random.rand() < pm:
            individuo[i] = 1 - individuo[i]
    return individuo

