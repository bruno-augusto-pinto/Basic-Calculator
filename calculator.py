print("Bem-vindo ao projeto Calculadora de adição")


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('0. Finalizar')
    op = input('Qual operação deseja realizar? ')

    if op in ('0', '1', '2', '3', '4'):
        if op == '0':
            break
        try:
            num1 = float(input('Digite o primeiro valor: '))
            num2 = float(input('Digite o segundo valor: '))
            if op == '1':
                res = adicao(num1, num2)
            elif op == '2':
                res = subtracao(num1, num2)
            elif op == '3':
                res = multiplicacao(num1, num2)
            elif op == '4':
                res = divisao(num1, num2)
            print('Resultado: ', res)
            print(" ")
        except:
            print("Você digitou um valor inválido, tente novamente")
            print('')
            continue
    else:
        print("Você digitou um valor inválido, tente novamente")
        print('')
