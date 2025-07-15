import numpy as np
import matplotlib.pyplot as plt

#constantes
g = 9.81  # Aceleración de la gravedad en m/s^2

#esntradas de usuario
masa = float(input("Ingrese la masa del objeto en kg: "))
fuerza_motor= float(input("fuerza del motor (N): "))
tiempo_impulso= float(input("duracion del impulso (s): "))
angulo = float(input("angulo de lanzamiento (grados): "))

# conversion de angulo
theta = np.radians(angulo)


#aceleracion durante el impulso
a = fuerza_motor / masa

#velocidades al final del impulso
vx_inpulso = a * tiempo_impulso * np.cos(theta)
vy_inpulso = a * tiempo_impulso * np.sin(theta)

#posiciones al final del impulso
x_impulso = 0.5 * a * np.cos(theta) * tiempo_impulso**2
y_impulso = 0.5 * a * np.sin(theta)* tiempo_impulso**2

#tiempo en la fase balistica
tiempo_caida = 2 * vy_inpulso / g

#tiempo total
t_total = tiempo_impulso + tiempo_caida
t= np.linspace(0, t_total, 500)

#inicializacion
x = []
y = []

for ti in t:
    if ti <= tiempo_impulso:
        #fase de impulso
        xi = 0.5 * a * np.cos(theta) * ti**2
        yi = 0.5 * a * np.sin(theta) * ti**2
    else:
        #fase balistica
        ti_b = ti - tiempo_impulso
        xi = x_impulso + vx_inpulso * ti_b
        yi = y_impulso + vy_inpulso * ti_b - 0.5 * g * ti_b**2
    x.append(xi)
    y.append(yi)

#graficar
plt.plot(x, y)
plt.title("trayectoria de un cohete con fase de impulso")
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.grid(True)
plt.ylim(bottom=0)  # Evitar que la gráfica muestre valores negativos en el eje y
plt.show()