from time import sleep
import random



while True:
    print('Olá seja bem vindo ao jogo do...')
    sleep(2)
    print('Pedra 🗿')
    sleep(1)
    print('Papel 📄')
    sleep(1)
    print('Tesoura ✂️')
    sleep(2)
    print('-=-'*7)
    print()

    nome = input('Digite seu nickname -> ').upper().strip()
    sleep(2)
    print('Guardando na memória...')
    sleep(2)
    print('Computando...')
    sleep(1)
    print(f'Seja bem vindo {nome}')
    sleep(1)

    print('ESCOLHA SUA JOGADA')
    print('[1] PEDRA')
    print('[2] PAPEL')
    print('[3] TESOURA')
    print('[4] SAIR')
    print('=================================')

    escolha = int(input('Digite a sua escolha -> '))

    if escolha == 4:
        print('Saindo do jogo...')
        break

    computador = random.randint(1,3)

    opcoes = ['PEDRA 🗿', 'PAPEL 📄', 'TESOURA ✂️']

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(1)

    print(f'{nome} escolheu {opcoes[escolha-1]}')
    print(f'Computador escolheu {opcoes[computador-1]}')

    if escolha == computador:
        print('🤝 EMPATE!')
    
    elif (escolha == 1 and computador == 3) or \
         (escolha == 2 and computador == 1) or \
         (escolha == 3 and computador == 2):
        print(f'🏆 {nome} VENCEU!')
    
    else:
        print('💻 COMPUTADOR VENCEU!')

    print('-='*20)
    sleep(2)