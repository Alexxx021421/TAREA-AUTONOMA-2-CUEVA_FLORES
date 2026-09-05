# TAREA-AUTONOMA-2-CUEVA_FLORES
Proyecto de Matemática Aplicada para simular en 3D el movimiento de un dron de entregas y relacionarlo con cálculo diferencial e integral.

# Simulación 3D y Telemetría Analítica de Renderizado y Física de un Dron de Entregas 🛸

**Carrera:** Desarrollo de Software  1A
**Asignatura:** Matemática Aplicada  
**Docente:** Ing. Andrés Cangui H.  
**Estudiantes:** Alexander Cueva, Emily Flores.   
**Periodo:** Tercer Bimestre 
---
##  Descripción del Proyecto
Este proyecto consiste en un **motor de simulación 3D en tiempo real** desarrollado en Python que modela matemáticamente el comportamiento de un vehículo aéreo no tripulado (Dron) durante un vuelo de prueba de 10 segundos. Se aplican conceptos clave de **Cálculo Diferencial e Integral** para procesar la telemetría, identificar puntos críticos de optimización y calcular la acumulación de datos en un buffer de transmisión.
---
## Modelos Matemáticos Utilizados
### Fase 1: Altitud y Velocidad Instantánea (Derivadas)
*   **Función de Altitud:**  
    $$h(t) = -0.1t^4 + 1.6t^3 - 7.2t^2 + 10t + 5$$
*   **Modelo de Velocidad Instantánea ($h'(t)$):**  
    $$v(t) = -0.4t^3 + 4.8t^2 - 14.4t + 10$$
*   **Optimización Vuelo:**  
    Resolviendo  $h'(t) = 0$ y mediante el criterio de la segunda derivada ($h''(t) = -1.2t^2 + 9.6t - 14.4$), se determinó que la **altura máxima absoluta** se alcanza en **$t \approx 7.79\text{ s}$** con **$h(7.79) \approx 34.09\text{ m}$**.

### Fase 2: Reconstrucción de Temperatura (Problema de Valor Inicial)
*   **Tasa de Calentamiento:** $T'(t) = 0.6t^2 - 2t + 4$
*   **Ecuación de Temperatura Reconstruida:**  
    $$T(t) = 0.2t^3 - t^2 + 4t + 22$$ *(donde la constante de integración $C=22^\circ\text{C}$ corresponde a la temperatura ambiente inicial).*

### Fase 3: Transmisión en Buffer (Integral Definida)
*   **Tasa de Transferencia:** $D(t) = 3t^2 + 2t + 5$
*   **Cálculo de Carga Total:**  
    A través del Teorema Fundamental del Cálculo en el intervalo $t \in [1, 4]$, se obtuvo:
    $$\text{Datos Totales} = \int_{1}^{4} (3t^2 + 2t + 5) \, dt = [t^3 + t^2 + 5t]_1^4 = 100 - 7 = \mathbf{93\text{ MB}}$$
---
## Requisitos Técnicos e Instalación
El proyecto se programó sobre **Python 3.x**. Clona este repositorio e instala las dependencias de la biblioteca matemática y gráfica:
```bash
git clone https://github.comAlex021421/TAREA-AUTONOMA-2-CUEVA_FLORES.git
cd TAREA-AUTONOMA-2-CUEVA_FLORES
pip install vpython numpy matplotlib
```
##  Ejecución de la Simulación
Para iniciar el renderizado de la escena tridimensional en el navegador y visualizar el HUD de telemetría dinámica en tiempo real, ejecuta:
```bash
python TAREA AUTONOMA 2.py
```
### Características del Sistema:
1.  **Escena 3D:** Un entorno tridimensional interactivo con trazado de estela de la trayectoria física del dron.
2.  **HUD de Telemetría Dinámica:** Muestra segundo a segundo el cambio instantáneo de altura, velocidad y almacenamiento acumulado del buffer.
3.  **Matplotlib Post-Vuelo:** Al concluir el ciclo, se autogenera una ventana comparativa con 3 subplots analíticos mostrando curvas y la región integrada del buffer.
### Capturas
### 1. Interfaz del Entorno de Simulación 3D y HUD en Tiempo Real
Aquí se puede observar el renderizado tridimensional del dron siguiendo la trayectoria física de la ecuación junto al panel de control analítico.

<img width="1406" height="924" alt="image" src="https://github.com/user-attachments/assets/76d4ceb9-19d1-46dd-946d-8590e247a8dc" />

### 2. Gráficas Estadísticas de Resumen Analítico (Matplotlib)
Al finalizar los 10 segundos, el sistema despliega el comportamiento vectorial, los puntos de optimización crítica y la acumulación del buffer de datos (región sombreada).

<img width="1873" height="706" alt="image" src="https://github.com/user-attachments/assets/16aa2102-d1c9-4e0c-9339-425b6d60d8c2" />

### 3. Resultados Analíticos Impresos en Consola
El script incluye una rutina de validación que imprime en la terminal los valores exactos calculados analíticamente, sirviendo como contraparte de verificación para los cálculos manuales del informe.

<img width="477" height="492" alt="image" src="https://github.com/user-attachments/assets/9791086d-adf0-4f8b-869a-e379f391cd3a" />





