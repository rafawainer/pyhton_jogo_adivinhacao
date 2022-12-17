# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
def jogar():
    print("*******************************************")
    print('    Bem vindo ao jogo de Adivinhacao!')
    print("*******************************************")


    tentativas_max = 0

    dificuldade_str = ''

    while (dificuldade_str not in ("1", "2", "3")):
        print("Selecione a dificuldade: ")
        dificuldade_str = input("(1) Fácil (2) Médio (3) Difícil: ")

    dificuldade = int(dificuldade_str)
    if (dificuldade == 1):
        tentativas_max = 20
    elif (dificuldade == 2):
        tentativas_max = 10
    else:
        tentativas_max = 5

    numero_secreto_min = int(input("Selecione o numero secreto minimo: "))
    numero_secreto_max = int(input("Selecione o numero secreto maximo: "))

    print(f"Minimo: {numero_secreto_min} <> Maximo: {numero_secreto_max}")
    numero_secreto = random.randrange(1, 101)
    # numero_secreto = random.randrange({numero_secreto_min}, {numero_secreto_max})

    pontos = 1000

    # while (tentativa_atual <= tentativas_max):
    for rodada in range (1, tentativas_max + 1):
        print(f'Tentativa {rodada} de {tentativas_max}')
        chute_str = int(input("Digite o seu numero: "))
        acertou = (numero_secreto == chute_str)
        maior   = (numero_secreto < chute_str)
        menor   = (numero_secreto > chute_str)

        print("Voce digitou o numero ", chute_str)

        if (acertou):
            print("Voce acertou !!")
            break
        elif (maior):
            print(f"Errou! Seu chute {chute_str} foi maior que o numero secreto")
        elif (menor):
            print(f"Errou! Seu chute {chute_str} foi menor que o numero secreto")

        pontos = pontos - abs(numero_secreto - chute_str)
    # print("Voce errou <", chute_str, "|", numero_secreto, ">")

    print("*******************************************")
    print("************ Fim do jogo! *****************")
    print('********* Hoje é {:02d}/{:02d}/{:04d} **************'.format(17, 12, 2022))
    print(f'********** O numero secreto é: {numero_secreto} ***********')
    print(f'********** Você fez: {pontos} pontos ***********')
    print("*******************************************")

if __name__ == '__main__':
    jogar()