def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

while True:
    print("Menu da Calculadora:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '5':
        print("Saindo da calculadora...")
        break

    if escolha in ("1", "2", "3", "4"):
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(n1, "+", n2, "=", somar(n1, n2))
        elif escolha == '2':
            print(n1, "-", n2, "=", subtrair(n1, n2))
        elif escolha == '3':
            print(n1, "*", n2, "=", multiplicar(n1, n2))
        elif escolha == '4':
            if n2 == 0:
                print("Erro: Não é possível dividir por zero.")
            else:
                print(f"{n1} / {n2} = {dividir(n1, n2):.2f}")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")