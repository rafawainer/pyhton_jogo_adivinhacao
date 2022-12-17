import adivinhacao
import forca

print("Opcoes de jogo:")
print("(1) Forca (2) Adivinhacao")
jogo = int(input("Selecione seu jogo: "))

if (jogo == 1):
    forca.jogar()
else:
    adivinhacao.jogar()
