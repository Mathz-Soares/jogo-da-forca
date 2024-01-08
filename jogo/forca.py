palavra = "jogo"
letras_chute = []
chances = 10
ganhou = False

while True:
    for letra in palavra:
        if letra in letras_chute:
            print(letra, end= " ")
        else:
            print("_", end= " ")
    chute=input(f"chute uma letra: ")
    letras_chute.append(chute)
    if chute not in palavra:
        chances = chances -1
        print("você ainda tem",chances," chances")
    ganhou = True
    for letra in palavra:
        if letra not in letras_chute:
            ganhou = False

    if chances == 0 or ganhou:
        print(" ")
        break
if ganhou:
        print("Parabéns, você ganhou! A palavra era: ",palavra)
else:
        print("Você perdeu! A palavra era: ",palavra)