# Solicita ao usuário uma operação (adição, subtração, multiplicação, divisão) e dois números.
# Realiza a operação e exibe o resultado.
# Repita até que o usuário digite "saída".

def main():
    while True:
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        escolha = input("Digite a opção: ")
        if escolha in ("saída", "sair", "exit", "quit", "saida"):
            break
        if escolha not in ("1", "2", "3", "4"):
            print("Erro: Operação inválida.\n")
            continue
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Digite um número válido.\n")
            continue
        if escolha == "1":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif escolha == "2":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif escolha == "3":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif escolha == "4":
            print(f"{num1} / {num2} = {num1 / num2}")
        print("\n")
        
if __name__ == "__main__":
    main()