# Día 25
# Importar Pandas
import pandas as pd # importar pandas como pd
import numpy  as np # importar numpy como np



#Series
# Crear serie de Pandas con índice por defecto
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# Crear serie de Pandas con índice personalizado
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Crear serie de Pandas a partir de un diccionario
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)

# Crear serie de Pandas constante
s = pd.Series(10, index = [1, 2, 3])
print(s)

# Crear serie de Pandas con Linspace
s = pd.Series(np.linspace(5, 20, 10)) # linspace(inicio, fin, número_de_elementos)
print(s)



# DataFrames
# Crear DataFrame a partir de una lista de listas
data = [
    ['Asabeneh', 'Finland', 'Helsinki'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(df)

# Crear DataFrame a partir de un diccionario
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsinki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Crear DataFrame a partir de una lista de diccionarios
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)



# Leer archivos CSV con Pandas
df = pd.read_csv('./data/weight-height.csv')
print(df.head()) # head() por defecto muestra las primeras 5 filas
print(df.tail()) # últimas 5 filas

# Exploración de datos
print(df.shape) # número de filas y columnas

# Más información sobre los datos
print(df.columns) # nombres de las columnas
print(df.head(10)) # primeras 10 filas
print(df.tail(10)) # últimas 10 filas
print(df['Gender'].value_counts()) # contar cuántos hay de cada uno
print(df.describe()) # resumen estadístico de los datos


# Modificar DataFrame
# Primero, creemos un DataFrame usando lo que aprendimos anteriormente
# datos
data = [
    {"Name": "Juan Pérez", "Country":"China", "City":"Shanghái"},
    {"Name": "Luis", "Country":"China", "City":"Pekín"},
    {"Name": "Carlos", "Country":"China", "City":"Cantón"}]
# crear DataFrame
df = pd.DataFrame(data)
print(df)

# Añadir nueva columna
# datos
weights = [74, 78, 69]
# añadir columna al DataFrame
df['Weight'] = weights
print(df)


# Modificar valores de una columna
# Podemos modificar una columna de tres maneras:

# 1. Asignación directa:
df['Name'] = ['Miguel', 'Ana', 'Sofía']
print(df)

# 2. Modificando con loc:
df.loc[1, 'Name'] = 'Lucía'
print(df)

# 3. Modificando con iloc:
print('Datos originales:\n', df)
df.iloc[1, 0] = 'Paco' # --> 1, 0 es la posicion del elemento en la fila y columna respectivamente
print('Datos modificados:\n', df)


# Formatear columnas del DataFrame
# Añadir la columna Height
heights = [175, 168, 172]
df['Height'] = heights

# añadir columna BMI: peso(kg) / altura^2(m). Redondear a 2 decimales.
df['BMI'] = np.round(df['Weight'] / ((df['Height'] * 0.01) ** 2), 2)
print(df)


# Comprobar tipos de datos de columnas
print(df.dtypes)


# Indexación booleana
# crear DataFrame
df = pd.DataFrame({
    'name': ['Juan', 'Luis', 'Carlos', 'Pedro'],
    'country': ['China', 'Estados Unidos', 'Reino Unido', 'España'],
    'age': [25, 15, 22, 28],
    'empleado': [True, False, True, False]
})

print(df)

# Filtrando edad > 20 y empleado == True
print(df[(df['age'] > 20) & (df['empleado'] == True)])



# Ejercicios: Día 25
# 1. Lee el archivo hacker_news.csv y muestra las primeras cinco filas.
df = pd.read_csv("./data/hacker_news.csv")
print(df.head())

# 2. Obtén la columna de títulos.
print(df["title"])

# 3. Obtén el número de filas y columnas.
print(df.shape)

# 4. Obtén las primeras diez y las últimas diez filas.
print(df.head(10))
print(df.tail(10))

# 5. Obtén la segunda y cuarta fila, columnas 2 a 4.
print(df.iloc[[1, 3], 1:4])

# 6. Filtra las filas cuyo tema sea Python.
print(df[df["title"].str.contains("python", case=False)])

# 7. Cuenta cuántas filas tienen tema Python.
rows = df[df["title"].str.contains("python", case=False)]
print(len(rows))
# Tambien puede usarse shape[0]
print(df[df["title"].str.contains("python", case=False)].shape[0])

# 8. Filtra las filas con votos mayores a 200.
print(df[(df["num_points"] > 200)])

# 9. Ordena el DataFrame por votos (ascendente).
print(df.sort_values(by="num_points"))

# 10. Ordena el DataFrame por votos (descendente).
print(df.sort_values(by="num_points", ascending=False))

# 11. Excluye las filas con tema Python y ordena por votos.
filt_not_python = df[~(df["title"].str.contains("python", case=False))]
print(filt_not_python.sort_values(by="num_points", ascending=False))