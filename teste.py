n1 = float(input("Informe um numero: "))
n2 = float(input("Informe um numero: "))
soma = n1 + n2
multiplicaçao = n1 * n2

escolha = float(input("Escolha 1 para somar e 2 para multiplicar "))
if escolha == 1:
    print("Aqui esta a soma: ", soma)
elif escolha == 2:
    print("Aqui esta a multiplicação: ", multiplicaçao)
else:
    print("Opção inexistente")   