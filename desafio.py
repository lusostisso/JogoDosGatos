
content = open('pontuacao.txt').read()    
jogador1_content, jogador2_content = content.split("Player 2:")

jogador1 = [int(i) for i in jogador1_content.strip().split("\n") if i!='Player 1:']
jogador2 = [int(i) for i in jogador2_content.strip().split("\n") if i!='Player 2:']

def calculoPontos (jogador):
    resultado = 0   
    for i, num in enumerate(jogador):
        resultado += num*(len(jogador)-i)
    print(resultado)

print("Números do jogador 1:", jogador1)
print("Números do jogador 2:", jogador2)

while len(jogador1) > 0 and len(jogador2) > 0:
    carta_jog_1 = jogador1[0]
    carta_jog_2 = jogador2[0]
    
    if(carta_jog_1>carta_jog_2):
        jogador1.append(carta_jog_1) #é obrigatório primeiro vir a carta vitoriosa
        jogador1.append(carta_jog_2) #depois concatenar a carta perdedora
        jogador1.pop(0)
        jogador2.pop(0)
    else:
        jogador2.append(carta_jog_2)
        jogador2.append(carta_jog_1)
        jogador1.pop(0)
        jogador2.pop(0)
        
     
if (len(jogador1) == 0):
    print ("Jogador 2 venceu! " + str(jogador2))
    calculoPontos(jogador2)
else:
    print("Jogador 1 venceu!" + str(jogador1))
    calculoPontos(jogador1)
        
    
