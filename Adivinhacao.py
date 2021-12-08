print("***************************************")
print("BEM VINDO AO JOGO DA ADIVINHAÇÃO!")
print("***************************************", "\n")

tentativas_str = input("Digite quantas tentativas você deseja para acertar o numero:")
tentativas = int(tentativas_str)
total_tentativas = tentativas
print("\n", "VAMOS COMEÇAR!!!", "\n")
rodadas = int(1)

while(tentativas > 0):

    print("Tentativa ", rodadas, " de ", total_tentativas, ". \n")
    secreto = int(20)
    chute_str = input("O número secreto é... ")
    chute = int(chute_str)

    acertou = chute == secreto
    menor = chute > secreto
    maior = chute < secreto

    if(acertou):
        print("Parabéns! Você acertou o numero secreto. \n")
        break
    else:
        if(menor):
            print("Você errou! O número secreto é menor. \n")
        elif(maior):
            print("Você errou! O número secreto é maior. \n")

    rodadas = rodadas + 1
    tentativas = tentativas - 1