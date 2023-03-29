print("Bem-vindo ao sistema de busca de personagens, vamos começar!")
personagem = []
elemento = []
arma = []
resposta = "S"
while resposta == "S":
    personagem.append(input("Personagem: "))
    elemento.append(input("Elemento: "))
    arma.append(input("Arma: "))
    resposta = input("\nDigite \"S\" para continuar, mas se quiser procurar sobre um personagem já ditado pressione qualquer outra tecla: ").upper()

busca=input("\n Digite o personagem que você deseja saber sobre: ")
for boneco in range(0,len(personagem)):
    if busca==personagem[boneco]:
        print("elemento: ", elemento[boneco])
        print("arma: ", arma[boneco])
        print("Obrigado por participar desse sistema!")


