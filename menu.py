import calculadora
a = 2
b = 3
def menu():
    while True:
        print("\nMenu")
        print("1. Somar")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f'{a} + {b} = {calculadora.somar(a, b)}')
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()