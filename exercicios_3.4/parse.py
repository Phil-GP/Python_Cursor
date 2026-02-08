# leia o CSV e calcule estatísticas simples: média, mediana, desvio padrão para cada coluna

import pandas as pd
import matplotlib.pyplot as plt

def estatisticas():
    df = pd.read_csv("arquivo.csv", sep=";")
    print("Média:")
    print(df.mean())
    print("\nMediana:")
    print(df.median())
    print("\nDesvio padrão:")
    print(df.std())
    return df

def grafico(df):
    # Gráfico de dispersão: col1 vs col2
    plt.figure(figsize=(7, 5))
    plt.scatter(df["col1"], df["col2"])
    plt.xlabel("col1")
    plt.ylabel("col2")
    plt.title("Dispersão: col1 vs col2")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = estatisticas()
    grafico(df)