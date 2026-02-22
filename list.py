def english():
    list = []
    # This program aims to create a list with the user's information, such as name, age, height, cpf and dream. The program will also calculate the user's age based on the year of birth informed.

    # Requesting the user's information
    name = input("\nEnter your name: ")
    yearOfBirth = int(input("\nEnter the year you were born: "))
    height = float(input("\nEnter your height: "))
    cpf = input("\nEnter your CPF: ")

    # Listing the dream options for the user to choose
    print("\n1. Travel the world\n2. Have a family\n3. Live in another country\n4. Be rich")
    dream = int(input("\nWhich of these options is your dream: "))

    # Validating the dream option
    while dream < 1 or dream > 4:
        print("\nError - Invalid option - Try again!")
        dream = int(input("\nWhich of these options is your dream: "))

    # Calculating the user's age
    userAge = 2026 - yearOfBirth

    # Adding the user's information to the list
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # Adding the user's dream to the list
    if dream == 1:
        list.append("Travel the world")
    elif dream == 2:
        list.append("Have a family")
    elif dream == 3:
        list.append("Live in another country")
    else:
        list.append("Be rich")

    # Printing the user's information
    print(f"\n\tNAME: {list[0]}\n\tAGE: {list[1]} years\n\tHEIGHT: {list[2]} meters\n\tCPF: {list[3]}\n\tDREAM: {list[4]}")

    # Success message
    print("\nRegistration successful!")

def portuguese():
    list = []
    # Este programa tem como objetivo criar uma lista com as informações do usuário, como nome, idade, altura, cpf e sonho. O programa também irá calcular a idade do usuário com base no ano de nascimento informado.

    # Solicitando as informações do usuário
    nome = input("\nDigite o seu nome: ")
    anoNascimento = int(input("\nDigite o ano em que voce nasceu: "))
    altura = float(input("\nDigite a sua altura: "))
    cpf = input("\nDigite o seu CPF: ")

    # Listando as opções de sonho para o usuário escolher
    print("\n1. Viajar o mundo\n2. Ter uma família\n3. Morar em outro país\n4. Ser rico")
    sonho = int(input("\nQual dessas opcoes é o seu sonho: "))

    # Validando a opção do sonho
    while sonho < 1 or sonho > 4:
        print("\nError - Opcao inválida - Tente novamente!")
        sonho = int(input("\nQual dessas opcoes é o seu sonho: "))
    
    # Calculando a idade do usuário
    idadeUsuario = 2026 - anoNascimento

    # Adicionando as informações do usuário na lista
    list.append(nome)
    list.append(idadeUsuario)
    list.append(altura)
    list.append(cpf)

    # Adicionando o sonho do usuário na lista
    if sonho == 1:
        list.append("Viajar o mundo")
    elif sonho == 2:
        list.append("Ter uma família")
    elif sonho == 3:
        list.append("Morar em outro país")
    else:
        list.append("Ser rico")

    # Imprimindo as informações do usuário
    print(f"\n\tNOME: {list[0]}\n\tIDADE: {list[1]} anos\n\tALTURA: {list[2]} metros\n\tCPF: {list[3]}\n\tSONHO: {list[4]}")

    # Mensagem de sucesso
    print("\nCadastro feito com sucesso!")

def spanish():
    list = []
    # Este programa tiene como objetivo crear una lista con la información del usuario, como nombre, edad, altura, cpf y sueño. El programa también calculará la edad del usuario en función del año de nacimiento informado.

    # Solicitando la información del usuario
    nombre = input("\nIngrese su nombre: ")
    anoNacimiento = int(input("\nIngrese el año en que nació: "))
    altura = float(input("\nIngrese su altura: "))
    cpf = input("\nIngrese su CPF: ")

    # Listando las opciones de sueño para que el usuario elija
    print("\n1. Viajar por el mundo\n2. Tener una familia\n3. Vivir en otro país\n4. Ser rico")
    sueño = int(input("\n¿Cuál de estas opciones es tu sueño: "))

    # Validando la opción de sueño
    while sueño < 1 or sueño > 4:
        print("\nError - Opción inválida - ¡Inténtalo de nuevo!")
        sueño = int(input("\n¿Cuál de estas opciones es tu sueño: "))
    
    # Calculando la edad del usuario
    edadUsuario = 2026 - anoNacimiento

    # Agregando la información del usuario a la lista
    list.append(nombre)
    list.append(edadUsuario)
    list.append(altura)
    list.append(cpf)

    # Agregando el sueño del usuario a la lista
    if sueño == 1:
        list.append("Viajar por el mundo")
    elif sueño == 2:
        list.append("Tener una familia")
    elif sueño == 3:
        list.append("Vivir en otro país")
    else:
        list.append("Ser rico")

    # Imprimiendo la información del usuario
    print(f"\n\tNOMBRE: {list[0]}\n\tEDAD: {list[1]} años\n\tALTURA: {list[2]} metros\n\tCPF: {list[3]}\n\tSUEÑO: {list[4]}")

    # Mensaje de éxito
    print("\n¡Registro exitoso!")

def french():

    list = []
    # Ce programme a pour objectif de créer une liste avec les informations de l'utilisateur, telles que le nom, l'âge, la taille, le cpf et le rêve. Le programme calculera également l'âge de l'utilisateur en fonction de l'année de naissance informée.

    # Demander les informations de l'utilisateur
    nom = input("\nEntrez votre nom: ")
    anneeNaissance = int(input("\nEntrez l'année de votre naissance: "))
    taille = float(input("\nEntrez votre taille: "))
    cpf = input("\nEntrez votre CPF: ")

    # Lister les options de rêve pour que l'utilisateur puisse choisir
    print("\n1. Voyager dans le monde\n2. Avoir une famille\n3. Vivre dans un autre pays\n4. Être riche")
    reve = int(input("\nQuelle de ces options est votre rêve: "))

    # Valider l'option de rêve
    while reve < 1 or reve > 4:
        print("\nErreur - Option invalide - Essayez à nouveau!")
        reve = int(input("\nQuelle de ces options est votre rêve: "))
    
    # Calculer l'âge de l'utilisateur
    ageUtilisateur = 2026 - anneeNaissance

    # Ajouter les informations de l'utilisateur à la liste
    list.append(nom)
    list.append(ageUtilisateur)
    list.append(taille)
    list.append(cpf)

    # Ajouter le rêve de l'utilisateur à la liste
    if reve == 1:
        list.append("Voyager dans le monde")
    elif reve == 2:
        list.append("Avoir une famille")
    elif reve == 3:
        list.append("Vivre dans un autre pays")
    else:
        list.append("Être riche")

    # Imprimer les informations de l'utilisateur
    print(f"\n\tNOM: {list[0]}\n\tÂGE: {list[1]} ans\n\tTAILLE: {list[2]} mètres\n\tCPF: {list[3]}\n\tRÊVE: {list[4]}")

    # Message de succès
    print("\nEnregistrement réussi!")

def italian():
    list = []
    # Questo programma ha lo scopo di creare una lista con le informazioni dell'utente, come nome, età, altezza, cpf e sogno. Il programma calcolerà anche l'età dell'utente in base all'anno di nascita informato.

    # Richiedere le informazioni dell'utente
    nome = input("\nInserisci il tuo nome: ")
    annoNascita = int(input("\nInserisci l'anno in cui sei nato: "))
    altezza = float(input("\nInserisci la tua altezza: "))
    cpf = input("\nInserisci il tuo CPF: ")

    # Elencare le opzioni di sogno per l'utente da scegliere
    print("\n1. Viaggiare per il mondo\n2. Avere una famiglia\n3. Vivere in un altro paese\n4. Essere ricco")
    sogno = int(input("\nQuale di queste opzioni è il tuo sogno: "))

    # Validare l'opzione del sogno
    while sogno < 1 or sogno > 4:
        print("\nErrore - Opzione non valida - Riprova!")
        sogno = int(input("\nQuale di queste opzioni è il tuo sogno: "))
    
    # Calcolare l'età dell'utente
    etaUtente = 2026 - annoNascita

    # Aggiungere le informazioni dell'utente alla lista
    list.append(nome)
    list.append(etaUtente)
    list.append(altezza)
    list.append(cpf)

    # Aggiungere il sogno dell'utente alla lista
    if sogno == 1:
        list.append("Viaggiare per il mondo")
    elif sogno == 2:
        list.append("Avere una famiglia")
    elif sogno == 3:
        list.append("Vivere in un altro paese")
    else:
        list.append("Essere ricco")

    # Stampare le informazioni dell'utente
    print(f"\n\tNOME: {list[0]}\n\tETÀ: {list[1]} anni\n\tALTEZZA: {list[2]} metri\n\tCPF: {list[3]}\n\tSOGNO: {list[4]}")

    # Messaggio di successo

def germany():
    list = []
    # Dieses Programm hat zum Ziel, eine Liste mit den Informationen des Benutzers zu erstellen, wie Name, Alter, Größe, CPF und Traum. Das Programm berechnet auch das Alter des Benutzers basierend auf dem angegebenen Geburtsjahr.

    # Anfordern der Informationen des Benutzers
    name = input("\nGeben Sie Ihren Namen ein: ")
    geburtsjahr = int(input("\nGeben Sie das Jahr ein, in dem Sie geboren wurden: "))
    groesse = float(input("\nGeben Sie Ihre Größe ein: "))
    cpf = input("\nGeben Sie Ihre CPF ein: ")

    # Auflisten der Traumoptionen für den Benutzer zur Auswahl
    print("\n1. Die Welt bereisen\n2. Eine Familie haben\n3. In einem anderen Land leben\n4. Reich sein")
    traum = int(input("\nWelche dieser Optionen ist dein Traum: "))

    # Validieren der Traumoption
    while traum < 1 or traum > 4:
        print("\nFehler - Ungültige Option - Versuchen Sie es erneut!")
        traum = int(input("\nWelche dieser Optionen ist dein Traum: "))
    
    # Berechnen des Alters des Benutzers
    alterBenutzer = 2026 - geburtsjahr

    # Hinzufügen der Informationen des Benutzers zur Liste
    list.append(name)
    list.append(alterBenutzer)
    list.append(groesse)
    list.append(cpf)

    # Hinzufügen des Traums des Benutzers zur Liste
    if traum == 1:
        list.append("Die Welt bereisen")
    elif traum == 2:
        list.append("Eine Familie haben")
    elif traum == 3:
        list.append("In einem anderen Land leben")
    else:
        list.append("Reich sein")

    # Drucken der Informationen des Benutzers

def janapese():
    list = []
    # このプログラムは、ユーザーの情報をリストに作成することを目的としています。名前、年齢、身長、CPF、夢などの情報が含まれます。プログラムは、入力された生年に基づいてユーザーの年齢も計算します。

    # ユーザーの情報を要求する
    name = input("\nあなたの名前を入力してください: ")
    birthYear = int(input("\nあなたが生まれた年を入力してください: "))
    height = float(input("\nあなたの身長を入力してください: "))
    cpf = input("\nあなたのCPFを入力してください: ")

    # ユーザーが選択できる夢のオプションをリストする
    print("\n1. 世界を旅行する\n2. 家族を持つ\n3. 他の国に住む\n4. 金持ちになる")
    dream = int(input("\nこれらのオプションのどれがあなたの夢ですか: "))

    # 夢のオプションを検証する
    while dream < 1 or dream > 4:
        print("\nエラー - 無効なオプション - もう一度やり直してください!")
        dream = int(input("\nこれらのオプションのどれがあなたの夢ですか: "))
    
    # ユーザーの年齢を計算する
    userAge = 2026 - birthYear

    # ユーザーの情報をリストに追加する
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # ユーザーの夢をリストに追加する
    if dream == 1:
        list.append("世界を旅行する")
    elif dream == 2:
        list.append("家族を持つ")
    elif dream == 3:
        list.append("他の国に住む")
    else:
        list.append("金持ちになる")

    # ユーザーの情報を印刷する

def korean():
    list = []
    # 이 프로그램은 사용자 정보(이름, 나이, 키, CPF, 꿈 등)를 리스트로 만드는 것을 목표로 합니다. 프로그램은 또한 입력된 출생 연도를 기반으로 사용자의 나이를 계산합니다.

    # 사용자 정보 요청
    name = input("\n이름을 입력하세요: ")
    birthYear = int(input("\n태어난 연도를 입력하세요: "))
    height = float(input("\n키를 입력하세요: "))
    cpf = input("\nCPF를 입력하세요: ")

    # 사용자가 선택할 수 있는 꿈 옵션 나열
    print("\n1. 세계 여행\n2. 가족 갖기\n3. 다른 나라에 살기\n4. 부자가 되기")
    dream = int(input("\n이 옵션 중 어떤 것이 당신의 꿈입니까: "))

    # 꿈 옵션 검증
    while dream < 1 or dream > 4:
        print("\n오류 - 잘못된 옵션 - 다시 시도하십시오!")
        dream = int(input("\n이 옵션 중 어떤 것이 당신의 꿈입니까: "))
    
    # 사용자의 나이 계산
    userAge = 2026 - birthYear

    # 사용자 정보를 리스트에 추가
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # 사용자의 꿈을 리스트에 추가
    if dream == 1:
        list.append("세계 여행")
    elif dream == 2:
        list.append("가족 갖기")
    elif dream == 3:
        list.append("다른 나라에 살기")
    else:
        list.append("부자가 되기")

    # 사용자 정보 인쇄

def guarani():
    list = []
    # Ko'ã programa ohechauka mba'eichapa ikatu ojapo petei lista oñembojoaju haguã usuario rehegua informasiones, oje'eva'erã hína: réra, ary, altura, cpf ha sueño. Ko'ã programa avei ohechauka mba'eichapa ikatu ojapo petei cálculo usuario rehegua edad rehegua año de nacimiento rehegua.

    # Oñepyrũ usuario rehegua informasiones
    name = input("\nEike nde réra: ")
    birthYear = int(input("\nEike ary nde raẽva: "))
    height = float(input("\nEike nde altura: "))
    cpf = input("\nEike nde CPF: ")

    # Oje'eva'erã hína sueño opción usuario rehegua elegir
    print("\n1. Viajar el mundo\n2. Tener una familia\n3. Morar en otro país\n4. Ser rico")
    dream = int(input("\nMba'éichapa ko'ã opción ohechauka hína nde sueño: "))

    # Validar sueño opción
    while dream < 1 or dream > 4:
        print("\nError - Opción inválida - ¡Inténtalo de nuevo!")
        dream = int(input("\nMba'éichapa ko'ã opción ohechauka hína nde sueño: "))
    
    # Cálculo usuario rehegua edad
    userAge = 2026 - birthYear

    # Oñembojoaju usuario rehegua informasiones lista
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # Oñembojoaju usuario rehegua sueño lista
    if dream == 1:
        list.append("Viajar el mundo")
    elif dream == 2:
        list.append("Tener una familia")
    elif dream == 3:
        list.append("Morar en otro país")
    else:
        list.append("Ser rico")

    # Imprimir usuario rehegua informasiones

def turkish():
    list = []
    # Bu program, kullanıcının bilgilerini içeren bir liste oluşturmayı amaçlamaktadır. Kullanıcının adı, yaşı, boyu, CPF'si ve hayali gibi bilgileri içerecektir. Program ayrıca, kullanıcının doğum yılına göre yaşını hesaplayacaktır.

    # Kullanıcının bilgilerini isteyin
    name = input("\nAdınızı girin: ")
    birthYear = int(input("\nDoğum yılınızı girin: "))
    height = float(input("\nBoyunuzu girin: "))
    cpf = input("\nCPF'nizi girin: ")

    # Kullanıcının seçebileceği hayal seçeneklerini listeleyin
    print("\n1. Dünyayı gezmek\n2. Bir aile kurmak\n3. Başka bir ülkede yaşamak\n4. Zengin olmak")
    dream = int(input("\nBu seçeneklerden hangisi hayaliniz: "))

    # Hayal seçeneğini doğrulayın
    while dream < 1 or dream > 4:
        print("\nHata - Geçersiz seçenek - Lütfen tekrar deneyin!")
        dream = int(input("\nBu seçeneklerden hangisi hayaliniz: "))

    # Kullanıcının yaşını hesaplayın
    userAge = 2026 - birthYear

    # Kullanıcının bilgilerini listeye ekleyin
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # Kullanıcının hayalini listeye ekleyin
    if dream == 1:
        list.append("Dünyayı gezmek")
    elif dream == 2:
        list.append("Bir aile kurmak")
    elif dream == 3:
        list.append("Başka bir ülkede yaşamak")
    else:
        list.append("Zengin olmak")

    # Kullanıcının bilgilerini yazdırın
    print("\nKullanıcı Bilgileri:")
    print(f"Ad: {list[0]}")
    print(f"Yaş: {list[1]} yaşında")
    print(f"Boyu: {list[2]} cm")
    print(f"CPF: {list[3]}")
    print(f"Hayal: {list[4]}")

    # Başarı mesajı
    print("\nKayıt başarılı!")

def polish():
    list = []
    # Ten program ma na celu stworzenie listy z informacjami użytkownika, takimi jak imię, wiek, wzrost, CPF i marzenie. Program obliczy również wiek użytkownika na podstawie podanego roku urodzenia.

    # Prośba o informacje od użytkownika
    name = input("\nWprowadź swoje imię: ")
    birthYear = int(input("\nWprowadź rok swojego urodzenia: "))
    height = float(input("\nWprowadź swój wzrost: "))
    cpf = input("\nWprowadź swój CPF: ")

    # Wyświetlenie opcji marzeń do wyboru przez użytkownika
    print("\n1. Podróżować po świecie\n2. Mieć rodzinę\n3. Mieszkać w innym kraju\n4. Być bogatym")
    dream = int(input("\nKtóra z tych opcji jest twoim marzeniem: "))

    # Walidacja opcji marzenia
    while dream < 1 or dream > 4:
        print("\nBłąd - Nieprawidłowa opcja - Spróbuj ponownie!")
        dream = int(input("\nKtóra z tych opcji jest twoim marzeniem: "))
    
    # Obliczenie wieku użytkownika
    userAge = 2026 - birthYear

    # Dodanie informacji użytkownika do listy
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # Dodanie marzenia użytkownika do listy
    if dream == 1:
        list.append("Podróżować po świecie")
    elif dream == 2:
        list.append("Mieć rodzinę")
    elif dream == 3:
        list.append("Mieszkać w innym kraju")
    else:
        list.append("Być bogatym")

    # Wydrukowanie informacji o użytkowniku
    print(f"\n\tIMIĘ: {list[0]}\n\tWIEK: {list[1]} lat\n\tWZROST: {list[2]} cm\n\tCPF: {list[3]}\n\tMARZENIE: {list[4]}")

    # Komunikat o sukcesie
    print("\nRejestracja zakończona sukcesem!")

def russian():
    list = []
    # Эта программа предназначена для создания списка с информацией о пользователе, такой как имя, возраст, рост, CPF и мечта. Программа также будет рассчитывать возраст пользователя на основе указанного года рождения.

    # Запрос информации у пользователя
    name = input("\nВведите ваше имя: ")
    birthYear = int(input("\nВведите год вашего рождения: "))
    height = float(input("\nВведите ваш рост: "))
    cpf = input("\nВведите ваш CPF: ")

    # Перечисление вариантов мечты для выбора пользователем
    print("\n1. Путешествовать по миру\n2. Иметь семью\n3. Жить в другой стране\n4. Быть богатым")
    dream = int(input("\nКакой из этих вариантов является вашей мечтой: "))

    # Проверка варианта мечты
    while dream < 1 or dream > 4:
        print("\nОшибка - Неверный вариант - Попробуйте снова!")
        dream = int(input("\nКакой из этих вариантов является вашей мечтой: "))
    
    # Расчет возраста пользователя
    userAge = 2026 - birthYear

    # Добавление информации о пользователе в список
    list.append(name)
    list.append(userAge)
    list.append(height)
    list.append(cpf)

    # Добавление мечты пользователя в список
    if dream == 1:
        list.append("Путешествовать по миру")
    elif dream == 2:
        list.append("Иметь семью")
    elif dream == 3:
        list.append("Жить в другой стране")
    else:
        list.append("Быть богатым")

    # Печать информации о пользователе
    print(f"\n\tИМЯ: {list[0]}\n\tВОЗРАСТ: {list[1]} лет\n\tРОСТ: {list[2]} см\n\tCPF: {list[3]}\n\tМЕЧТА: {list[4]}")

    # Комментарий о завершении регистрации
    print("\nРегистрация завершена успешно!")

def main():
    print("\nSelect a language / Selecione um idioma / Seleccione un idioma / Sélectionnez une langue / Seleziona una lingua / Wählen Sie eine Sprache / 언어를 선택하세요 / 언어를 선택하세요 / Выберите язык:")
    print("\n1. English\n2. Portuguese\n3. Spanish\n4. French\n5. Italian\n6. German\n7. Japanese\n8. Korean\n9. Guarani\n10. Turkish\n11. Polish\n12. Russian")
    language = int(input("\nEnter the number corresponding to your language: "))

    if language == 1:
        english()
    elif language == 2:
        portuguese()
    elif language == 3:
        spanish()
    elif language == 4:
        french()
    elif language == 5:
        italian()
    elif language == 6:
        germany()
    elif language == 7:
        janapese()
    elif language == 8:
        korean()
    elif language == 9:
        guarani()
    elif language == 10:
        turkish()
    elif language == 11:
        polish()
    elif language == 12:
        russian()
    else:
        print("\nInvalid option - Please try again!")

if __name__ == "__main__":
    main()