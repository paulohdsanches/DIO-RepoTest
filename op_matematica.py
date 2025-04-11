# Solicitar dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Solicitar a operação matemática desejada
print("Escolha a operação matemática que deseja executar:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
operacao = input("Digite o número correspondente à operação: ")

# Executar a operação escolhida
if operacao == "1":
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "2":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "3":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")