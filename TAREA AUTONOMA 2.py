from vpython import *
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# FUNCIONES MATEMÁTICAS
# ============================================================

def h(t):
    """Altitud del dron."""
    return -0.1*t**4 + 1.6*t**3 - 7.2*t**2 + 10*t + 5


def v(t):
    """Velocidad vertical h'(t)."""
    return -0.4*t**3 + 4.8*t**2 - 14.4*t + 10


def T(t):
    """Temperatura del motor."""
    return 0.2*t**3 - t**2 + 4*t + 22


def D(t):
    """Transferencia de datos en MB/s."""
    return 3*t**2 + 2*t + 5


def integral_datos(t):
    """
    Integral acumulada desde t=1 hasta t.
    Para t < 1 se considera acumulación 0.
    """
    if t < 1:
        return 0

    return t**3 + t**2 + 5*t - 7


# ============================================================
# CONFIGURACIÓN DE LA SIMULACIÓN 3D
# ============================================================

scene.title = "Simulación 3D - Telemetría de Dron"
scene.width = 1100
scene.height = 700
scene.background = color.black

scene.camera.pos = vector(18, 15, 25)
scene.camera.axis = vector(-12, -8, -18)

# Suelo
ground = box(
    pos=vector(5, 0, 0),
    size=vector(25, 0.2, 15),
    color=color.green
)

# ============================================================
# DRON
# ============================================================

drone_body = box(
    pos=vector(0, h(0), 0),
    size=vector(2, 0.5, 1.2),
    color=color.gray(0.7)
)

# Brazos
arm1 = cylinder(
    pos=vector(-0.9, h(0), 0),
    axis=vector(1.8, 0, 0),
    radius=0.08,
    color=color.white
)

arm2 = cylinder(
    pos=vector(0, h(0), -0.6),
    axis=vector(0, 0, 1.2),
    radius=0.08,
    color=color.white
)

# Hélices
propellers = []

for x, z in [
    (-0.9, -0.6),
    (-0.9, 0.6),
    (0.9, -0.6),
    (0.9, 0.6)
]:
    prop = cylinder(
        pos=vector(x, h(0) + 0.3, z),
        axis=vector(0, 0.08, 0),
        radius=0.35,
        color=color.cyan
    )
    propellers.append(prop)


# ============================================================
# HUD DE TELEMETRÍA
# ============================================================

telemetry = label(
    pos=vector(0, 12, 0),
    text="",
    height=18,
    box=False,
    line=False,
    color=color.white
)

# ============================================================
# SIMULACIÓN
# ============================================================

t = 0
dt = 0.05
tiempos = []
altitudes = []
velocidades = []
datos_acumulados = []

while t <= 10:

    rate(30)

    altura = h(t)
    velocidad = v(t)
    datos = integral_datos(t)

    # Movimiento vertical
    nueva_posicion = vector(0, altura, 0)

    drone_body.pos = nueva_posicion

    # Mover brazos
    arm1.pos = vector(-0.9, altura, 0)
    arm2.pos = vector(0, altura, -0.6)

    # Mover hélices
    for i, prop in enumerate(propellers):

        if i == 0:
            prop.pos = vector(-0.9, altura + 0.3, -0.6)
        elif i == 1:
            prop.pos = vector(-0.9, altura + 0.3, 0.6)
        elif i == 2:
            prop.pos = vector(0.9, altura + 0.3, -0.6)
        else:
            prop.pos = vector(0.9, altura + 0.3, 0.6)

    # Guardar información
    tiempos.append(t)
    altitudes.append(altura)
    velocidades.append(velocidad)
    datos_acumulados.append(datos)

    # HUD
    telemetry.text = (
        f"TELEMETRÍA DEL DRON\n\n"
        f"Tiempo: {t:.2f} s\n"
        f"Altitud: {altura:.2f} m\n"
        f"Velocidad vertical: {velocidad:.2f} m/s\n"
        f"Temperatura: {T(t):.2f} °C\n"
        f"Datos acumulados: {datos:.2f} MB"
    )

    t += dt


# ============================================================
# RESULTADOS ANALÍTICOS
# ============================================================

print("\n==========================================")
print(" RESULTADOS ANALÍTICOS")
print("==========================================")

print(f"Velocidad en t=2: {v(2):.2f} m/s")
print(f"Velocidad en t=6: {v(6):.2f} m/s")

print("\nPuntos críticos:")

print("t1 = 1.0000 s")
print(f"h(t1) = {h(1):.4f} m")

t2 = (11 - np.sqrt(21)) / 2
t3 = (11 + np.sqrt(21)) / 2

print(f"t2 = {t2:.4f} s")
print(f"h(t2) = {h(t2):.4f} m")

print(f"t3 = {t3:.4f} s")
print(f"h(t3) = {h(t3):.4f} m")

print("\nTemperatura inicial:")
print(f"T(0) = {T(0):.2f} °C")

print("\nDatos transferidos entre t=1 y t=4:")
print("93 MB")


# ============================================================
# GRÁFICAS FINALES
# ============================================================

t_graf = np.linspace(0, 10, 500)

h_graf = h(t_graf)
v_graf = v(t_graf)
d_graf = D(t_graf)

# Punto máximo global
t_max = t3
v_max = v(t_max)

# Recta tangente de la gráfica de velocidad
# Pendiente = v'(t) = h''(t)
pendiente = -1.2*t_max**2 + 9.6*t_max - 14.4

tangente = v_max + pendiente * (t_graf - t_max)


plt.figure(figsize=(15, 5))

# ------------------------------------------------------------
# GRÁFICA 1: ALTITUD
# ------------------------------------------------------------

plt.subplot(1, 3, 1)

plt.plot(
    t_graf,
    h_graf,
    label="h(t)"
)

plt.scatter(
    [t_max],
    [h(t_max)],
    label="Altura máxima"
)

plt.xlabel("Tiempo (s)")
plt.ylabel("Altitud (m)")
plt.title("Posición / Altitud del Dron")
plt.grid(True)
plt.legend()


# ------------------------------------------------------------
# GRÁFICA 2: VELOCIDAD
# ------------------------------------------------------------

plt.subplot(1, 3, 2)

plt.plot(
    t_graf,
    v_graf,
    label="v(t) = h'(t)"
)

plt.plot(
    t_graf,
    tangente,
    linestyle="--",
    label="Recta tangente"
)

plt.scatter(
    [t_max],
    [v_max],
    label="Punto máximo"
)

plt.axhline(
    0,
    linestyle=":"
)

plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Velocidad Instantánea")
plt.grid(True)
plt.legend()


# ------------------------------------------------------------
# GRÁFICA 3: TRANSFERENCIA DE DATOS
# ------------------------------------------------------------

plt.subplot(1, 3, 3)

plt.plot(
    t_graf,
    d_graf,
    label="D(t)"
)

# Área entre t=1 y t=4
t_area = np.linspace(1, 4, 200)
d_area = D(t_area)

plt.fill_between(
    t_area,
    d_area,
    alpha=0.3,
    label="Área = 93 MB"
)

plt.xlabel("Tiempo (s)")
plt.ylabel("Transferencia (MB/s)")
plt.title("Transferencia de Datos")
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()