def portuguese():
    print('\n=================================')
    nome = input('\nQual é o seu nome: ')
    print('Bem-vindo(a), querido(a) ' + nome + '!\n')

    opcao = int(input('Você está animado(a) para aprender a programar em Python? (1 - Sim, 0 - Não): '))
    while opcao < 0 or opcao > 1:
        print('Insira uma opção válida')
        opcao = int(input('Você está animado(a) para aprender a programar em Python? (1 - Sim, 0 - Não): '))

    if opcao == 1:
        print('''\nＶａｍｏｓ ｐｒａ ｃｉｍａ ｄｏ ｆｕｔｕｒｏ， ｍａｎｏ！''')
    elif opcao == 0:
        print('\nＮａｏ！ Ｖａｍｏｓ ｌａ， ｖｏｃｅ ｃｏｎｓｅｇｕｅ！ ：）')

    print('\n===============================================================================')
    print('\n\tObrigado pelo seu tempo :)')
    print('''\tPrograma criado por: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
def english():
    print('\n=================================')
    name = input('''\nWhat's is your name: ''')
    print('Welcome, Dear ' + name + '!\n')

    option = int(input('Are you excited to learn how to program in Python? (1 - Yes, 0 - No): '))
    while option < 0 or option > 1:
        print('Please enter a valid option!')
        option = int(input('Are you excited to learn how to program in Python? (1 - Yes, 0 - No): '))

    if option == 1:
        print('''Ｌｅｔ＇ｓ ｒｏｃｋ ｔｈｅ ｆｕｔｕｒｅ ｂｒｏｏｏｏ！''')
    else:
        print('''Ｎｏｏｏｏｏ． Ｃｏｍｅ ｏｎ ｂｒｏ， ｙｏｕ ｃａｎ ｄｏ ｉｔ！ ：）''')

    print('\n===============================================================================')
    print('\n\tThank you for your time :)')
    print('''\tProgram created by: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
def spanish():
    print('\n=================================')
    nombre = input('\n¿Cómo te llamas? ')
    print('Bienvenido(a), estimado(a) ' + nombre + '!\n')

    opcion = int(input('¿Estás animado para aprender a programar en Python? (1 - Sí, 0 - No): '))
    while opcion < 0 or opcion > 1:
        print('Por favor, ingrese una opción válida.')
        opcion = int(input('¿Estás animado para aprender a programar en Python? (1 - Sí, 0 - No): '))

    if opcion == 1:
        print('''¡Ｖａｍｏｓ ａ ｒｏｍｐｅｒ ｅｌ ｆｕｔｕｒｏ， ｈｅｒｍａｎｏ！''')
    else:
        print('''¡Ｎｏｏｏｏｏ！ ¡Ｖａｍｏｓ， ｈｅｒｍａｎｏ， ｔｕ ｐｕｅｄｅｓ！ :)''')

    print('\n===============================================================================')
    print('\n\tGracias por su tiempo :)')
    print('''\tPrograma creado por: 🄼🄰🅁🄲🄾🅂 🅅🄸🄽🄸🄲🄸🅄🅂 🄳🄴 🄹🄴🅂🅄🅂 🄰🄻🄼🄴🄸🄳🄰''')
print('''𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 𝕨𝕖𝕝𝕔𝕠𝕞𝕖 𝕡𝕣𝕠𝕘𝕣𝕒𝕞!''')
print('\n1. Portuguese')
print('2. English')
print('3. Spanish')
choose_language = int(input('\nSelect your preferred language: '))
if choose_language == 1:
    portuguese()
elif choose_language == 2:
    english()
else:
    spanish()
