#Pandas es la librería básica para la manipulación y análisis de datos
import pandas as pd

#Numpy es la biblioteca para crear vectores y matrices, además de un conjunto grande de funciones matemáticas
import numpy as np

#Seaborn es una librería que usamos para graficar
import seaborn as sns

#Leo los datos del '.parquet'
df_parquet = pd.read_parquet(r"D:\DATA_Analysis\Arkon_TEST\data2 (1).parquet")
# Mostrar datos e info del DataFrame
#print(df_parquet)
print(df_parquet.info())

#Leo los datos del '.csv'
df_data1 = pd.read_csv(r"D:\DATA_Analysis\Arkon_TEST\Data1.csv")
#Ver datos e info del segundo dataframe
#print(df_data1)
print(df_data1.info())

print("------Unificar los 2 conjuntos de datos en un solo dataset--------")
#concat() permite unir los dataset, podemos indicar si es horizontal con axis=1
#en este caso ambos conjuntos tienen las mismas columnas la union se realiza vertical
df_union = pd.concat([df_parquet, df_data1])
df_union.index = range(df_union.shape[0])
print(df_union)
print(df_union.info())

#Aquí elimino los datos NAN y los duplicados
df_union_dna = df_union.dropna()
df_union_dna = df_union_dna.drop_duplicates()
print(df_union_dna)

#Para la unión también se utiliza el metodo merge() indicando la columna para la unión.
#print("\n\n Union con el método merge()")
#print(pd.merge(df_parquet, df_data1, on='name', suffixes=('_1', '_2')))

print("---------2 Generar una tabla de valores únicos de “Starships” --------")
valores_unicos = df_union["starships"].unique()
#imprimo los valores únicos en un data frame de la columna 'starships'
df_unicos = pd.DataFrame(valores_unicos, columns=['starships'])
print(df_unicos)

print("--------3 Generar un conteo de registros sobre el grupo [Skin_color, eye_color]-----")
count_s_e = df_union.groupby(['skin_color', 'eye_color']).size().reset_index(name='Count')

print(count_s_e)

print("-----4. Generar una tabla con los Name duplicados y cuantas veces se repiten------")
name_counts = df_union['name'].value_counts().reset_index()
name_counts.columns = ['Name', 'Count']
duplicates = name_counts[name_counts['Count'] > 1]
print(duplicates)

