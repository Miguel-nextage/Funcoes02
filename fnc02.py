# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def par(n):
    if n%2==0:
        return "É par!"
    else:
        return "É impar!"
    
num = int(input("Digite seu numero:"))
ver = par(num)

print(ver)
