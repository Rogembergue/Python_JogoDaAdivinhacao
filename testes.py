import random

print("***************************************")
print("BEM VINDO AO JOGO DA ADIVINHAÇÃO!")
print("*************************************** \n")

total_tentativas = int(input("Digite quantas tentativas você deseja para acertar o numero:"))
print("\n", "ATENÇÃO!!! \n", "O número a ser adivinhado está entre 1 e 100.", "\n", "****************************")
print("\n", "VAMOS COMEÇAR!!!", "\n")
secreto = random.randrange(1, 101)
pontos = 1000

for rodadas in range(1, total_tentativas + 1):

    print("Tentativa {} de {} .".format(rodadas, total_tentativas),secreto,"\n")

    chute_str = input("O número secreto é... ")
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("O número que você digitou não esta entre 1 e 100. Digite novamente.","\n")
        continue

    acertou = chute == secreto
    menor = chute > secreto
    maior = chute < secreto

    if(acertou):
        print("Parabéns! Você acertou o numero secreto e fez {} pontos.".format(pontos), "\n")
        break
    else:
        if(menor):
            print("Você errou! O número secreto é menor. \n")
            pontos_perdidos = abs(secreto - chute)
            pontos = pontos - pontos_perdidos
            if(rodadas == total_tentativas):
                print("O numero secreto era {}. Você fez {}".format(secreto,pontos))
                break
        elif(maior):
            print("Você errou! O número secreto é maior. \n")
            pontos_perdidos = abs(secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodadas == total_tentativas):
                print("O numero secreto era {}. Você fez {}".format(secreto, pontos))
                break

print("Fim do jogo!")