def english():
    print('Welcome to the calculator!')
    first_value = int(input('Please enter the first value: '))
    second_value = int(input('Please enter the second value: '))
    while (first_value < 0):
        print('Please enter a valid number')
        first_value = int(input('Please enter the first value: '))
        while (second_value < 0):
            print('Please enter a valid number')
            second_value = int(input('Please enter the second value: '))

    sum = first_value + second_value
    subtraction = first_value - second_value
    multiplication = first_value * second_value
    division = first_value / second_value

    print(f'\n{first_value} + {second_value} = {sum}')
    print(f'{first_value} - {second_value} = {subtraction}')
    print(f'{first_value} * {second_value} = {multiplication}')
    print(f'{first_value} / {second_value} = {division:.2f}')
def portuguese():
    print('Bem-vindo(a) a sua calculadora!!')
    primeiro_valor = int(input('Por favor, informe o primeiro valor: '))
    segundo_valor = int(input('Por favor, informe o segundo valor: '))
    while (primeiro_valor < 0):
        print('Insira um número válido')
        primeiro_valor = int(input('Por favor, informe o primeiro valor: '))
        while (segundo_valor < 0):
            print('Insira um número válido')
            second_value = int(input('Por favor, informe o segundo valor: '))

    soma = primeiro_valor + segundo_valor
    subtracao = primeiro_valor - segundo_valor
    multiplicacao = primeiro_valor * segundo_valor
    divisao = primeiro_valor / segundo_valor

    print(f'\n{primeiro_valor} + {segundo_valor} = {soma}')
    print(f'{primeiro_valor} - {segundo_valor} = {subtracao}')
    print(f'{primeiro_valor} * {segundo_valor} = {multiplicacao}')
    print(f'{primeiro_valor} / {segundo_valor} = {divisao:.2f}')
def spanish():
    print('¡Bienvenido a la calculadora!')
    primer_valor = int(input('Por favor, ingrese el primer valor: '))
    segundo_valor = int(input('Por favor, ingrese el segundo valor: '))
    while (primer_valor < 0):
        print('Por favor, ingrese un número válido')
        primer_valor = int(input('Por favor, ingrese el primer valor: '))
        while (segundo_valor < 0):
            print('Por favor, ingrese un número válido')
            segundo_valor = int(input('Por favor, ingrese el segundo valor: '))

    suma = primer_valor + segundo_valor
    resta = primer_valor - segundo_valor
    multiplicacion = primer_valor * segundo_valor
    division = primer_valor / segundo_valor

    print(f'\n{primer_valor} + {segundo_valor} = {suma}')
    print(f'{primer_valor} - {segundo_valor} = {resta}')
    print(f'{primer_valor} * {segundo_valor} = {multiplicacion}')
    print(f'{primer_valor} / {segundo_valor} = {division:.2f}')
print('''𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕪𝕠𝕦𝕣 𝕔𝕒𝕝𝕔𝕦𝕝𝕒𝕥𝕠𝕣❕''')
print('\n1. English')
print('2. Portuguese')
print('3. Spanish')
choose_language = int(input('\nSelect your preferred language: '))
if choose_language == 1:
    english()
elif choose_language == 2:
    portuguese()
else:
    spanish()
