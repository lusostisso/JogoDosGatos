# JogoDosGatos

Uma vez meu amigo Paulo estava no Japão e ele resolveu ir em um desses tais de "Neko Café"
para saber como que funciona. Obviamente ele sabiaque iria encontrar café e gatos (provavelmente muitos gatos).

Porém ele achou estranho que haviam dois gatos em uma mesa com cartas em suas mãos.
Ele nunca viu gatos jogarem cartas na vida, até achou que estava sonhando. Porém havia pessoas assistindo
o jogo como se aquilo fosse algo super normal naquele ambiente.

Ele surpreso foi perguntar para uma pessoa de lá como o jogo funcionava e ela disse o seguinte:

Antes do jogo começar, eles dividem as cartas para que cada gato tenha seu
próprio baralho (o input do problema). Então, o jogo consiste em
uma série de rodadas: ambos os "jogadores" tiram sua carta do topo e o
jogador com a carta de maior valor ganha a rodada. O vencedor fica com as
duas cartas, colocando-as no fundo de seu próprio baralho, de modo que a carta do vencedor fique acima da outra.

Se isso fizer com que um jogador tenha todas as cartas, ele vence e o jogo termina.

Por exemplo, considere os seguintes decks iniciais:

Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10

Essa disposição significa que o baralho do jogador 1 contém 5 cartas,
com um "9" em cima e um "1" embaixo; o baralho do jogador 2 também contém 5 cartas,
sendo o "5" a primeira carta e "10" a última.

A primeira rodada começa com ambos os jogadores comprando a carta do topo
de seus baralhos: 9 e 5. O jogador 1 tem a carta mais alta, então ambas as cartas
se movem para o fundo do baralho do jogador 1, onde que o "9" fique acima do "5".
No total, são necessárias 29 rodadas antes que um jogador tenha todas as cartas:

-- Round 1 --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins the round!

-- Round 2 --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins the round!

-- Round 3 --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins the round!

-- Round 4 --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins the round!

-- Round 5 --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins the round!

...muitos rounds se passam...

-- Round 27 --
Player 1's deck: 5, 4, 1
Player 2's deck: 8, 9, 7, 3, 2, 10, 6
Player 1 plays: 5
Player 2 plays: 8
Player 2 wins the round!

-- Round 28 --
Player 1's deck: 4, 1
Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
Player 1 plays: 4
Player 2 plays: 9
Player 2 wins the round!

-- Round 29 --
Player 1's deck: 1
Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins the round!


== Post-game results ==
Player 1's deck: 
Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1

Quando o jogo terminar, você poderá calcular a pontuação do jogador vencedor.
A carta de baixo do baralho vale o valor da carta multiplicada por 1,
a segunda carta de baixo vale o valor da carta multiplicada por 2 e assim por diante.
Com 10 cartas, a carta de cima vale o valor da carta multiplicado por 10.
Neste exemplo, a pontuação do jogador vencedor é:

   3 * 10
+  2 *  9
+ 10 *  8
+  6 *  7
+  8 *  6
+  5 *  5
+  9 *  4
+  4 *  3
+  7 *  2
+  1 *  1
= 306

Assim, uma vez que o jogo termina, a pontuação do jogador vencedor é 306!!

Então, para seu input: Qual é a pontuação do jogador vencedor?
