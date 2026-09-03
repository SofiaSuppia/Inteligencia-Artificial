import numpy as np

mu_h0 = 3.0
alfa = 0.05
nivel_confianza = 1 - alfa

print(f"Nivel de confianza: {nivel_confianza*100}%")

ej1 = np.array([3.8,3.7,3.9,2.8])
ej2 = np.array([2.9,3.1,3.1,4.9])
ej3 = np.array([1.9,3.1,3.1,4])

print(f"muestra1: {ej1} promedio: {np.mean(ej1):.2f}")
print(f"muestra2: {ej2} promedio: {np.mean(ej2):.2f}")
print(f"muestra3: {ej3} promedio: {np.mean(ej3):.2f}")

def calculo_estadistico(muestra, mu_teorico):
    x_bar = np.mean(muestra)
    s = np.std(muestra, ddof=1)
    n = len(muestra)
    t = (x_bar - mu_teorico) / (s / np.sqrt(n))
    return t

t1 = calculo_estadistico(ej1, mu_h0)
t2 = calculo_estadistico(ej2, mu_h0)
t3 = calculo_estadistico(ej3, mu_h0)

print(f"Estadístico de prueba para muestra1: {t1:.2f}")
print(f"Estadístico de prueba para muestra2: {t2:.2f}")
print(f"Estadístico de prueba para muestra3: {t3:.2f}")