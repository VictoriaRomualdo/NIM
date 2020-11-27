# Jogo do NIM em Python
## História:
### O Nim é um jogo que foi originado na antiga China para dois jogadores. Foi o primeiro jogo a ser estudado matematicamente. 
## Em que consiste o jogo?
### Consiste em ir tirando peças (de 1 até m peças por jogada) até que um jogador retire a ultima peça, vencendo o jogo. O jogo foi desenvolvido de forma que o computador ganhará sempre. Para isso ele deverá seguir a estratégia vencedora. 
## Qual é a estratégia vencedora?
### Sejam **n** o número de peças inicial e **m** o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
#### Se **n** é múltiplo de **(m+1)**, o computador deve ser "generoso" e convidar o jogador a iniciar a partida. Caso contrário, o computador toma a inciativa de começar o jogo. Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de **(m+1)** ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
