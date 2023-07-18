# Este código solicita ao usuário que insira dois números e uma operação.
# O código então usa a operação para calcular o resultado e imprimi-lo.

# Entrada de informações nas variáveis.
x = float(input("Ensira o primeiro valor: "))
# Esta linha solicita ao usuário que insira o primeiro valor.
# A variável `x` é usada para armazenar o valor inserido pelo usuário.

print("+ - * /")
# Esta linha imprime os símbolos de adição, subtração, multiplicação e divisão.

oper = (input("Ensira a operação: "))
# Esta linha solicita ao usuário que insira a operação.
# A variável `oper` é usada para armazenar a operação inserida pelo usuário.

y = float(input("Ensira o segundo valor: "))
# Esta linha solicita ao usuário que insira o segundo valor.
# A variável `y` é usada para armazenar o valor inserido pelo usuário.

print (type(oper))
# Este print mostra o tipo da variável `oper`.
# (Utilizado para saber que tipo de informação está retornando)

# Se `oper` for igual a `+`, `-`, `*` ou `/`, o código calculará o resultado da operação e o imprimi-lo.
if oper == ('+'):
    print("{}+{}= {}".format(x, y), x + y)
# Esta linha imprime o resultado da adição dos dois números.
elif oper == ('-'):
    print("{}-{}= {}".format(x, y), x - y)
# Esta linha imprime o resultado da subtração dos dois números.
elif oper == ('*'):
    print("{}*{}= {}".format(x, y), x * y)
# Esta linha imprime o resultado da multiplicação dos dois números.
elif oper == ('/'):
    print("{}/{}= {}".format(x, y), x / y)
# Esta linha imprime o resultado da divisão dos dois números.

'''
Observação: A sintaxe `.format(x, y)` informa o formato que os colchetes ({}) devem seguir. No entanto, os colchetes não precisam ser usados em todas as chamadas `.format()`. Por exemplo, a chamada `print("{}+{}= {}".format(x, y), x + y)` é equivalente à chamada `print("{}+{}= {}".format(x + y))`.
'''

# BY: Gustavo Amaral Guimarães
# GitHub: https://github.com/gustavoamaral21