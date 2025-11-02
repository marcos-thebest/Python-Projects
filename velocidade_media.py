#Languages available
def portuguese():
    print('Simulador de computador de bordo!')
    distancia = float(input('Por favor, informe a distância percorrida: '))
    tempo = float(input('Por favor, informe o tempo da viagem: '))

    velocidade_media = distancia / tempo

    print(f'\nA velocidade média é: {velocidade_media:.2f} km/h!')
def english():
    print('On-board computer simulator!')
    distance = float(input('Please enter the distance traveled: '))
    time = float(input('Please enter the travel time: '))

    average_speed = distance / time

    print(f'\nThe average speed is: {average_speed:.2f} km/h!')
def spanish():
    print('¡Simulador de computadora a bordo!')
    distancia = float(input('Por favor, ingrese la distancia recorrida: '))
    tiempo = float(input('Por favor, ingrese el tiempo de viaje: '))

    velocidad_media = distancia / tiempo

    print(f'\n¡La velocidad media es de: {velocidad_media:.2f} km/h!')
print('''𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝕥𝕙𝕖 𝕆𝕟-𝔹𝕠𝕒𝕣𝕕 ℂ𝕠𝕞𝕡𝕦𝕥𝕖𝕣 𝕊𝕚𝕞𝕦𝕝𝕒𝕥𝕠𝕣❕''')
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
