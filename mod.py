import pandas as pd

# Cargar el archivo
file_path = r'C:\Users\alexa\Downloads\Proyecto_Electrico\Imagen\datos_curva11.txt'
data = pd.read_csv(file_path, delimiter='\t')

# Cambiar los valores de la columna 'CO' basado en la columna 't'
data['CO'] = data.apply(lambda row: 100 if 0 <= row['PV'] <= 65 else 0, axis=1)
data['t'] = range(len(data))

# Guardar el archivo modificado
output_path = r'C:\Users\alexa\Downloads\Proyecto_Electrico\Imagen\datos_curva11_modificado.txt'
data.to_csv(output_path, sep='\t', index=False)

print(f"Archivo modificado guardado en: {output_path}")
