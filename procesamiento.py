import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image_path = r'C:\Users\alexa\Downloads\Proyecto_Electrico\Imagen\RespPlanta_copy.jpg'  # Cambia esto por la ruta correcta
image = cv2.imread(image_path)

# Convertir la imagen a espacio de color HSV para facilitar la detección de colores
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir rangos de colores para las curvas azul y verde
blue_lower = np.array([100, 150, 0])
blue_upper = np.array([140, 255, 255])
green_lower = np.array([40, 50, 50])
green_upper = np.array([80, 255, 255])

# Crear máscaras para los colores
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
green_mask = cv2.inRange(hsv, green_lower, green_upper)

# Encontrar contornos de las máscaras
blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear listas para almacenar los datos de las curvas azul y verde
data_blue = []
data_green = []

# Procesar cada contorno azul
for contour in blue_contours:
    if len(contour.shape) == 3:
        contour = contour.reshape(-1, 2)
    for (x, y) in contour:
        t = x
        CO = 100 - (y * 100 / image.shape[0])
        PV = 0
        data_blue.append((t, CO, PV))

# Procesar cada contorno verde
for contour in green_contours:
    if len(contour.shape) == 3:
        contour = contour.reshape(-1, 2)
    for (x, y) in contour:
        t = x
        PV = 100 - (y * 100 / image.shape[0])
        CO = 0 if PV < 23.8 or PV > 70 else 100
        data_green.append((t, CO, PV))

# Ordenar los datos por tiempo t
data_blue.sort()
data_green.sort()

# Guardar los datos en el archivo .txt
output_txt_file = 'datos_curva11.txt'
with open(output_txt_file, 'w') as f:
    f.write("t\tCO\tPV\n")
    for t, CO, PV in data_blue:
        f.write(f"{t}\t{CO}\t{PV}\n")
    for t, CO, PV in data_green:
        f.write(f"{t}\t{CO}\t{PV}\n")

# Mostrar la imagen original con los contornos detectados
cv2.drawContours(image, blue_contours, -1, (255, 0, 0), 2)
cv2.drawContours(image, green_contours, -1, (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
