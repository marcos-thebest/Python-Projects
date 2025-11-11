import os
def confirmName(name):
    #Function to confirm the user's name
    confirm = input(f'\nConfirm your name.\nName: {name}\nIs this correct? (y/n): ')
    
    if confirm == 'y':
        print('\nName successfully confirmed!')
    else:
        print('\nPlease enter your name again!\n')
        while True:
            name = input('Please enter your name: ')
            confirm = input(f'\nConfirm your name.\nName: {name}\nIs this correct? (y/n): ')
            if confirm == 'y':
                print('\nName successfully confirmed!')
                break
            else:
                print('\nPlease enter your name again!\n')
def english():
    name = input('Please provide your name: ')

    #Function call to confirm the name
    confirmName(name)

    #Options menu
    print(f'\nGreat, what kind of assistance are you looking for here at SmartAssist?😁')

    print('\n1. Professional Support')
    print('2. Academic Support')
    print('3. Exit the program...')

    #User choice / Choice validation
    first_option = int(input('\nChoose an option (1-3): '))
    while first_option < 1 or first_option > 3:
        print('Invalid option! Please try again.')
        first_option = int(input('\nChoose an option (1-3): '))

    if first_option == 1:
        print('\nProfessional Support selected!\nWhat is your technology question in a professional context?')
        print('\n1. How can I improve my profile for job openings?')
        print('2. Essential tools for DevOps.')
        
        career_choice = int(input('\nSelect an option (1-2): '))
        while career_choice < 1 or career_choice > 2:
            print('Invalid option! Please try again.')
            career_choice = int(input('Select an option (1-2): '))

        if career_choice == 1:
            print('First, I need you to choose a context so that I can help you better...')
            print('\n1. Professional (career, tools, best practices)')
            print('2. Academic (studies, languages, concepts)')

            context = int(input('\nSelect an option (1-2): '))
            while context < 1 or context > 2:
                print('Invalid option! Please try again.')
                context = int(input('Select an option (1-2): '))
            
            if context == 1:
                print('To improve your PROFESSIONAL profile, I suggest these three approaches:')
                print('\n1. Portfolio on GitHub: upload 2-3 projects with detailed README, documentation, and best practices.')
                print('2. Certifications and courses: obtain relevant certifications (AWS, Docker, Kubernetes) and showcase them on LinkedIn.')
                print('3. Networking and presence: participating in tech communities, events, and contributing to open source projects.')

                paths_option = int(input('\nChoose a path (1-3): '))
                while paths_option < 1 or paths_option > 3:
                    print('Invalid option! Please try again.')
                    paths_option = int(input('Choose a path (1-3): '))
                if paths_option == 1:
                    print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                elif paths_option == 2:
                    print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                else:
                    print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

        else:
            print('Essential tools for the PROFESSIONAL context:')
            print('\n1. Versioning and CI/CD: Git, GitHub/GitLab, GitHub Actions, or Jenkins for automation.')
            print('2. Containers and Cloud: Docker, Kubernetes, and at least one cloud provider (AWS, Azure, or GCP).')
            print('3. Monitoring and Logs: Prometheus, Grafana, ELK Stack for application observability.')

            options_tools = int(input('\nSelect a tool (1-3): '))
            while options_tools < 1 or options_tools > 3:
                    print('Invalid option! Please try again.')
                    options_tools = int(input('Select a tool (1-3): '))

            if options_tools == 1:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif options_tools == 2:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

    elif first_option == 2:
        print('\nAcademic Support selected!\nWhat is your question about technology in an academic context?')
        print('\n1. Where do I start with Java?')
        print('2. How should I organize my SQL studies?')

        academic_choice = int(input('\nSelect an option (1-2): '))
        while academic_choice < 1 or academic_choice > 2:
            print('Invalid option! Please try again.')
            academic_choice = int(input('Select an option (1-2): '))

        if academic_choice == 1:
            print('Here are three possible answers to your question in an ACADEMIC context (you choose):')
            print('\n1. Fundamentals: review basic concepts with short, practical exercises.')
            print('2. Guided practice: complete 2-3 small projects to apply your knowledge.')
            print('3. Routine: create a study plan of 30 minutes/day + flashcards of concepts.')

            academic_pathways_option = int(input('\nChoose a path (1-3): '))
            while academic_pathways_option < 1 or academic_pathways_option > 3:
                print('Invalid option! Please try again.')
                academic_pathways_option = int(input('Choose a path (1-3): '))

            if academic_pathways_option == 1:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif academic_pathways_option == 2:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
        else:
            print('Here are 3 tips for organizing your SQL studies in an ACADEMIC context:')
            print('\n1. From zero to practice: learn basic SQL commands and practice with daily exercises.')
            print('2. SQL for data analysis: master joins, analytical functions, and complex queries.')
            print('3. SQL for developers: focus on modeling, code integration, and performance optimization.')

            sql_paths_options = int(input('\nChoose a path (1-3): '))
            while sql_paths_options < 1 or sql_paths_options > 3:
                    print('Invalid option! Please try again.')
                    sql_paths_options = int(input('Choose a path (1-3): '))
            if sql_paths_options == 1:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif sql_paths_options == 2:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Understood. I will record this as your final decision. Thank you for using 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
    else: 
        os.system('cls')
        print('Leaving the program... See you later! 👋')

def confirmarNome(nome):
    #Função para confirmar o nome do usuário
    confirmar = input(f'\nConfirme seu nome.\nNome: {nome}\nEstá correto? (s/n): ')
    
    if confirmar == 's':
        print('\nNome confirmado com sucesso!')
    else:
        print('\nPor favor, digite seu nome novamente!\n')
        while True:
            nome = input('Por gentileza, informe o seu nome: ')
            confirmar = input(f'\nConfirme seu nome.\nNome: {nome}\nEstá correto? (s/n): ')
            if confirmar == 's':
                print('\nNome confirmado com sucesso!')
                break
            else:
                print('\nPor favor, digite seu nome novamente!\n')
def portuguese():
    #Coleta do nome do usuário
    nome = input('Por gentileza, informe o seu nome: ')

    #Chamada da função para confirmar o nome
    confirmarNome(nome)

    #Menu de opções
    print(f'\nPerfeito, sou seu assistente de ideias em tecnologia. Prefere ajuda no contexto:😁')

    print('\n1. Profissional (carreira, ferramentas, boas práticas)')
    print('2. Acadêmico (estudos, linguagens, conceitos)')
    print('3. Sair do programa...')

    #Escolha do usuário / Validação da escolha
    primeira_opcao = int(input('\nEscolha uma opção (1-3): '))
    while primeira_opcao < 1 or primeira_opcao > 3:
        print('Opção inválida! Tente novamente.')
        primeira_opcao = int(input('Escolha uma opção (1-3): '))

    if primeira_opcao == 1:
        print('\nSuporte Profissional selecionado!\nQual é a sua dúvida de tecnologia dentro do contexto profissional?')
        print('\n1. Como melhorar meu perfil para vagas?')
        print('2. Ferramentas essenciais para DevOps.')
        
        escolha_profissional = int(input('\nEscolha uma opção (1-2): '))
        while escolha_profissional < 1 or escolha_profissional > 2:
            print('Opção inválida! Tente novamente.')
            escolha_profissional = int(input('Escolha uma opção (1-2): '))

        if escolha_profissional == 1:
            print('Primeiro, preciso que você escolha um contexto para que eu possa te ajudar melhor...')
            print('\n1. Profissional (carreira, ferramentas, boas práticas)')
            print('2. Acadêmico (estudos, linguagens, conceitos)')

            contexto = int(input('\nEscolha uma opção (1-2): '))
            while contexto < 1 or contexto > 2:
                print('Opção inválida! Tente novamente.')
                contexto = int(input('Escolha uma opção (1-2): '))
            
            if contexto == 1:
                print('Para melhorar seu perfil PROFISSIONAL, sugiro estes 3 caminhos:')
                print('\n1. Portfolio no GitHub: subir 2-3 projetos com README detalhado, documentação e boas práticas..')
                print('2. Certificações e cursos: fazer certificações relevantes (AWS, Docker, Kubernetes) e mostrar no LinkedIn.')
                print('3. Networking e presença: participar de comunidades tech, eventos e contribuir em projetos open source.')

                opcao_caminhos = int(input('\nEscolha uma caminho (1-3): '))
                while opcao_caminhos < 1 or opcao_caminhos > 3:
                    print('Opção inválida! Tente novamente.')
                    opcao_caminhos = int(input('Escolha uma caminho (1-3): '))
                if opcao_caminhos == 1:
                    print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                elif contexto == 2:
                    print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                else:
                    print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

        else:
            print('Ferramentas essenciais para o contexto PROFISSIONAL:')
            print('\n1. Versionamento e CI/CD: Git, GitHub/GitLab, GitHub Actions ou Jenkins para automação..')
            print('2. Containers e Cloud: Docker, Kubernetes e pelo menos 1 cloud provider (AWS, Azure ou GCP).')
            print('3. Monitoramento e Logs: Prometheus, Grafana, ELK Stack para observabilidade de aplicações.')

            opcoes_ferramentas = int(input('\nEscolha uma ferramenta (1-3): '))
            while opcoes_ferramentas < 1 or opcoes_ferramentas > 3:
                    print('Opção inválida! Tente novamente.')
                    opcoes_ferramentas = int(input('Escolha uma ferramenta (1-3): '))

            if opcoes_ferramentas == 1:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opcoes_ferramentas == 2:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

    elif primeira_opcao == 2:
        print('\nSuporte Acadêmico selecionado!\nQual é a sua dúvida de tecnologia dentro do contexto acadêmico?')
        print('\n1. Por onde começo em Java?')
        print('2. Como organizar meu estudo de SQL?')

        escolha_academica = int(input('\nEscolha uma opção (1-2): '))
        while escolha_academica < 1 or escolha_academica > 2:
            print('Opção inválida! Tente novamente.')
            escolha_academica = int(input('Escolha uma opção (1-2): '))

        if escolha_academica == 1:
            print('Eis 3 caminhos possíveis para sua dúvida no contexto ACADEMICO (você escolhe):')
            print('\n1. Fundamentos: revisar conceitos básicos com exercícios curtos e práticos.')
            print('2. Prática guiada: fazer 2-3 projetos pequenos para aplicar o conhecimento.')
            print('3. Rotina: criar um plano de estudo de 30 min/dia + flashcards de conceitos.')

            opcao_caminhos_academicos = int(input('\nEscolha uma caminho (1-3): '))
            while opcao_caminhos_academicos < 1 or opcao_caminhos_academicos > 3:
                print('Opção inválida! Tente novamente.')
                opcao_caminhos_academicos = int(input('Escolha uma caminho (1-3): '))

            if opcao_caminhos_academicos == 1:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opcao_caminhos_academicos == 2:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
        else:
            print('Aqui estão 3 dicas para organizar seu estudo de SQL no contexto ACADÊMICO:')
            print('\n1. Do zero à prática: aprenda os comandos básicos de SQL e pratique com exercícios diários.')
            print('2. SQL para análise de dados: domine junções, funções analíticas e consultas complexas.')
            print('3. SQL para desenvolvedores: foque em modelagem, integração com código e otimização de performance.')

            opcoes_caminhos_sql = int(input('\nEscolha uma dica (1-3): '))
            while opcoes_caminhos_sql < 1 or opcoes_caminhos_sql > 3:
                    print('Opção inválida! Tente novamente.')
                    opcoes_caminhos_sql = int(input('Escolha uma dica (1-3): '))
            if opcoes_caminhos_sql == 1:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opcoes_caminhos_sql == 2:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendi. Vou registrar como sua decisão final. Obrigado por usar o 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

    else: 
        os.system('cls')
        print('Saindo do programa... Até mais! 👋')

def confirmarNombre(nombre):
    #Función para confirmar el nombre de usuario
    confirmar = input(f'\nConfirme su nombre.\nNombre: {nombre}\n¿Es correcto? (s/n): ')
    
    if confirmar == 's':
        print('\n¡Nombre confirmado con éxito!')
    else:
        print('\nPor favor, ¡vuelva a escribir su nombre!\n')
        while True:
            nombre = input('Por favor, indique su nombre: ')
            confirmar = input(f'\nConfirme su nombre.\nNombre: {nombre}\n¿Es correcto? (s/n): ')
            if confirmar == 's':
                print('\n¡Nombre confirmado con éxito!')
                break
            else:
                print('\nPor favor, ¡vuelva a escribir su nombre!\n')
def spanish():
    #Recopilación del nombre de usuario
    nombre = input('Por favor, indique su nombre: ')

    #Llamada a la función para confirmar el nombre
    confirmarNombre(nombre)

    #Menú de opciones
    print(f'\nPerfecto, ¿qué tipo de asistencia busca aquí en SmartAssist?😁')

    print('\n1. Soporte Profesional')
    print('2. Soporte Académico')
    print('3. Salir del programa...')

    #Elección del usuario / Validación de la elección
    primera_opcion = int(input('\nElija una opción (1-3): '))
    while primera_opcion < 1 or primera_opcion > 3:
        print('¡Opción inválida! Inténtelo de nuevo.')
        primera_opcion = int(input('Elija una opción (1-3): '))

    if primera_opcion == 1:
        print('\n¡Soporte profesional seleccionado!\n¿Cuál es su duda tecnológica en el contexto profesional?')
        print('\n1. ¿Cómo puedo mejorar mi perfil para las ofertas de trabajo?')
        print('2. Herramientas esenciales para DevOps.')
        
        eleccion_profesional = int(input('\nElija una opción (1-2): '))
        while eleccion_profesional < 1 or eleccion_profesional > 2:
            print('Opción no válida. Inténtelo de nuevo.')
            eleccion_profesional = int(input('Elija una opción (1-2): '))

        if eleccion_profesional == 1:
            print('Primero, necesito que elijas un contexto para poder ayudarte mejor...')
            print('\n1. Profesional (carrera, herramientas, buenas prácticas)')
            print('2. Académico (estudios, lenguages, conceptos)')

            contextoSpa = int(input('\nElija una opción (1-2): '))
            while contextoSpa < 1 or contextoSpa > 2:
                print('Opción no válida. Inténtelo de nuevo.')
                contextoSpa = int(input('Elija una opción (1-2): '))
            
            if contextoSpa == 1:
                print('Para mejorar su perfil PROFESIONAL, le sugiero estas tres opciones:')
                print('\n1. Portafolio en GitHub: subir 2-3 proyectos con README detallado, documentación y buenas prácticas...')
                print('2. Certificaciones y cursos: obtener certificaciones relevantes (AWS, Docker, Kubernetes) y mostrarlas en LinkedIn.')
                print('3. Redes y presencia: participar en comunidades tecnológicas, eventos y contribuir en proyectos de código abierto.')

                opciones_caminos = int(input('\nElige una opción (1-3): '))
                while opciones_caminos < 1 or opciones_caminos > 3:
                    print('Opción no válida. Inténtelo de nuevo.')
                    opciones_caminos = int(input('Elige una opción (1-3): '))
                if opciones_caminos == 1:
                    print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                elif contextoSpa == 2:
                    print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
                else:
                    print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

        else:
            print('Herramientas esenciales para el contexto PROFESIONAL:')
            print('\n1. Control de versiones y CI/CD: Git, GitHub/GitLab, GitHub Actions o Jenkins para la automatización.')
            print('2. Contenedores y nube: Docker, Kubernetes y al menos un proveedor de servicios en la nube (AWS, Azure o GCP).')
            print('3. Monitoreo y registros: Prometheus, Grafana, ELK Stack para la observabilidad de aplicaciones.')

            opciones_herramientas = int(input('\nElija una herramienta (1-3): '))
            while opciones_herramientas < 1 or opciones_herramientas > 3:
                    print('Opción no válida. Inténtelo de nuevo.')
                    opciones_herramientas = int(input('Elija una herramienta (1-3): '))

            if opciones_herramientas == 1:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opciones_herramientas == 2:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')

    elif primera_opcion == 2:
        print('\n¡Apoyo académico seleccionado!\n¿Cuál es su duda sobre tecnología en el contexto académico?')
        print('\n1. ¿Por dónde empiezo en Java?')
        print('2. ¿Cómo organizar mi estudio de SQL?')

        opciones_caminos = int(input('\nElija una opción (1-2): '))
        while opciones_caminos < 1 or opciones_caminos > 2:
            print('Opción no válida. Inténtelo de nuevo.')
            opciones_caminos = int(input('Elija una opción (1-2): '))

        if opciones_caminos == 1:
            print('Aquí tienes tres posibles respuestas a tu pregunta en el contexto ACADÉMICO (tú eliges):')
            print('\n1. Fundamentos: repasar conceptos básicos con ejercicios cortos y prácticos.')
            print('2. Práctica guiada: realizar 2-3 proyectos pequeños para aplicar los conocimientos adquiridos.')
            print('3. Rutina: crear un plan de estudio de 30 minutos al día + tarjetas didácticas con conceptos.')

            opcion_caminos_academicos = int(input('\nElige una opción (1-3): '))
            while opcion_caminos_academicos < 1 or opcion_caminos_academicos > 3:
                print('Opción no válida. Inténtelo de nuevo.')
                opcion_caminos_academicos = int(input('Elige una opción (1-3): '))

            if opcion_caminos_academicos == 1:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opcion_caminos_academicos == 2:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
        else:
            print('Aquí tienes tres consejos para organizar tu estudio de SQL en el contexto ACADÉMICO:')
            print('\n1. De cero a la práctica: aprenda los comandos básicos de SQL y practique con ejercicios diarios.')
            print('2. SQL para el análisis de datos: domine las uniones, las funciones analíticas y las consultas complejas.')
            print('3. SQL para desarrolladores: enfóquese en el modelado, la integración con el código y la optimización del rendimiento.')

            opciones_rutas_sql = int(input('\nElige un consejo (1-3): '))
            while opciones_rutas_sql < 1 or opciones_rutas_sql > 3:
                    print('Opción no válida. Inténtelo de nuevo.')
                    opciones_rutas_sql = int(input('Elige un consejo (1-3): '))
            if opciones_rutas_sql == 1:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            elif opciones_rutas_sql == 2:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
            else:
                print('Entendido. Lo registraré como su decisión final. ¡Gracias por utilizar 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !')
    else: 
        os.system('cls')
        print('Saliendo del programa... ¡Hasta luego! 👋')

#Start of the program
print('''\nWelcome to 🅢 🅜 🅐 🅡 🅣 🅐 🅢 🅢 🅘 🅢 🅣 !''')

print('\n1. 🇪​​​​​🇳​​​​​🇬​​​​​🇱​​​​​🇮​​​​​🇸​​​​​🇭​​​​​ - 🇪​​​​​🇳​​​​​')
print('2. 🇵​​​​​🇴​​​​​🇷​​​​​🇹​​​​​🇺​​​​​🇬​​​​​🇺​​​​​🇪​​​​​🇸​​​​​🇪​​​​​ - 🇵​​​​​🇹​​​​​')
print('3. 🇸​​​​​🇵​​​​​🇦​​​​​🇳​​​​​🇮​​​​​🇸​​​​​🇭​​​​​ - 🇪​​​​​🇸​​​​​')
choose_language = int(input('\nSelect your preferred language: '))
if choose_language == 1:
    english()
elif choose_language == 2:
    portuguese()
else:
    spanish()
