# Importa o módulo `re`, que contém funções para trabalhar com expressões regulares.
import re

# Define uma função chamada `valida_email()` que leva um endereço de e-mail como entrada e retorna `True` se o endereço de e-mail for válido, ou `False` se não for.


def valida_email(email):

    # Define uma variável chamada `email_valido` que contém uma expressão regular que corresponde a um endereço de e-mail válido.
    email_valido = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'

    # Verifica se o endereço de e-mail corresponde à expressão regular. Se corresponder, a função retorna `True`. Caso contrário, a função retorna `False`.
    if re.search(email_valido, email):
        return 'e-mail valido'
    else:
        return 'e-mail invalido'


# Solicita ao usuário que insira um endereço de e-mail.
email = input("Ensira o e-mail: ")

# Imprime o resultado da função `valida_email()`.
print(valida_email(email))

# BY: Gustavo Amaral Guimarães
# GitHub: https://github.com/gustavoamaral21
