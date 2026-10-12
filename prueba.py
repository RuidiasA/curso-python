import pandas as pd
import numpy  as np

# Ejercicios: Día 25
# 11. Excluye las filas con tema Python y ordena por votos.

df = pd.read_csv("./data/hacker_news.csv")

print(df[~(df["title"].str.contains("python", case=False))].sort_values(by="num_points", ascending=False))