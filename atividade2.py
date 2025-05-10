def pertence_fibonacci(numero): #função que vai ser percorrida
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0


num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))


if pertence_fibonacci(num):# verificação e saída
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
