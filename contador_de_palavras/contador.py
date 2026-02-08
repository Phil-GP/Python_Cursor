# Programa para contar palavras em um arquivo de texto.
# 1. Peça ao usuário o caminho para um arquivo de texto.
# 2. Leia o conteúdo do arquivo.
# 3. Separe em palavras.
# 4. Conte o número total de palavras.
# 5. Exibe as 10 palavras mais frequentes.

import re
from collections import Counter

def extrair_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("O arquivo especificado não existe.")
        return ""

if __name__ == "__main__":
    arquivo = input("Digite o caminho para o arquivo de texto: ")
    texto = extrair_palavras(arquivo)
    
    if texto:
        palavras = re.findall(r"\w+", texto.lower())
        total_palavras = len(palavras)
        print(f"O arquivo contém {total_palavras} palavras.")
        
        contador = Counter(palavras)
        top_10 = contador.most_common(10)
        
        print("\nAs 10 palavras mais frequentes são:")
        for palavra, freq in top_10:
            print(f"{palavra}: {freq}")
    else:
        print("Não foi possível processar o arquivo.")