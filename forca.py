def jogar():
    print("*******************************************")
    print('    Bem vindo ao jogo de Forca !           ')
    print("*******************************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):

        chute = input("Digite a letra para chute: ").upper().strip()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    print("Encontrei a letra {} na posicao {}".format(chute, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Erro numero: {}".format(erros))

        print(letras_acertadas)
        enforcou = erros == 6

        acertou = "_" not in letras_acertadas


    if acertou:
        print("****************")
        print("VOCE GANHOU !!!")
        print("****************")
        print()
    else:
        print("PERDEU HEIN, QUE MERDA!")

    print("***********")
    print("Fim do jogo")
    print("***********")

if __name__ == '__main__':
    jogar()