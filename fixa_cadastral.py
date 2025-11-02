def english():
    print('=================================')
    print("Blood donor registration!")
    name = input('\nPlease enter your full name: ')
    weight = float(input('Please enter your weight in kg: '))
    height = int(input('Please enter your height in cm: '))
    year_of_birth = int(input('Enter your year of birth: '))

    age = 2025 - year_of_birth
    has_minimum_weight = weight > 50
    minimum_age = age >= 16

    output_text = (f'\tNAME: {name}\n\tWEIGHT: {weight:.2f} kg\n\tHEIGHT: {height}'
                   f' cm\n\tAGE: {age}\n\tTHERE IS A MINIMUM WEIGHT FOR DONATIONS: {has_minimum_weight}\n\t'
                   f'MINIMUM AGE TO DONATE: {minimum_age}')
    print(output_text)
    print('\n=================================')
    print('\n\tThank you for your time :)')
    print('''\tProgram created by: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
def spanish():
    print('=================================')
    print("¡Registro de donantes de sangre!")
    nombre = input('\nPor favor, indique su nombre completo: ')
    peso = float(input('Por favor, indique su peso en kg: '))
    altura = int(input('Por favor, indique su altura en cm: '))
    ano_nascimiento = int(input('Ingrese su año de nacimiento: '))

    edad = 2025 - ano_nascimiento
    tiene_peso_minimo = peso > 50
    edad_minima = edad >= 16

    texto_salida = (f'\tNOMBRE: {nombre}\n\tPESO: {peso:.2f} kg\n\tALTURA: {altura}'
                    f' cm\n\tEDAD: {edad}\n\t¿HAY UN PESO MÍNIMO PARA DONAR? {tiene_peso_minimo}\n\t'
                    f'¿TIENE EDAD MINIMA PARA DONAR?: {edad_minima}')

    print(texto_salida)
    print('\n=================================')
    print('\n\tGracias por su tiempo :)')
    print('''\tPrograma creado por: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
def portuguese():
    print('=================================')
    print("Registro de doadores de sangue!")
    nome = input('\nPor favor, informe o seu nome completo: ')
    peso = float(input('Por favor, informe o seu peso en kg: '))
    altura = int(input('Por favor, informe a sua altura em cm: '))
    ano_nascimento = int(input('Insira seu ano de nascimento: '))

    idade = 2025 - ano_nascimento
    tem_peso_minimo = peso > 50
    tem_idade_minima = idade >= 16

    saida_texto = (f'\tNOME: {nome}\n\tPESO: {peso:.2f} kg\n\tALTURA: {altura}'
                   f' cm\n\tIDADE: {idade}\n\tTEM PESO MÍNIMO PARA DOAR: {tem_peso_minimo}\n\t'
                   f'TEM IDADE MÍNIMA PARA DOAR: {tem_idade_minima}')

    print(saida_texto)
    print('\n=================================')
    print('\n\tObrigado pelo seu tempo :)')
    print('''\tPrograma criado por: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
print('''𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕪𝕠𝕦𝕣 𝕣𝕖𝕘𝕚𝕤𝕥𝕣𝕒𝕥𝕚𝕠𝕟 𝕗𝕠𝕣𝕞 𝕗𝕠𝕣 𝕕𝕠𝕟𝕒𝕥𝕚𝕟𝕘 𝕓𝕝𝕠𝕠𝕕❕''')
print('\n1. English')
print('2. Spanish')
print('3. Portuguese')
choose_language = int(input('\nSelect your preferred language: '))
if choose_language == 1:
    english()
elif choose_language == 2:
    spanish()
else:
    portuguese()
