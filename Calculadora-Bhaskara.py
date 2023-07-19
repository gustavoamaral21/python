# Este código solicita ao usuário os valores de A, B e C para uma equação quadrática.
a = float(input('Ensira o valor de A: '))
b = float(input('Ensira o valor de B: '))
c = float(input('Ensira o valor de C: '))

# Este código calcula o discriminante, que é a diferença entre o quadrado de B e quatro vezes A vezes C.
delta = (b ** 2) - 4 * a * c
print('Valor de Delta é', delta)

# Se A for igual a zero, então a equação não tem raízes.
if a == 0:
    print("Não tem raiz")

# Se o discriminante for menor que zero, então a equação não tem raízes reais.
elif delta < 0:
    print("Valor invalido")

# Se o discriminante for maior ou igual a zero, então a equação tem duas raízes reais.
else:
    # O código abaixo calcula as duas raízes da equação.
    x = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    # O código abaixo imprime as duas raízes da equação.
    print('O valor de x1 é: ', x)
    print('O valor de x2 é: ', x2)

# BY: Gustavo Amaral Guimarães
# GitHub: https://github.com/gustavoamaral21
