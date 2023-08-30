from config import *
from modelo import *

import pygame
import random 
from pygame.locals import *

# tela do Jogo
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Cobrinha')
clock = pygame.time.Clock() #tempo de movimentação

# função de gerar um número aleatório nas coordenadas
def posicao_aleatoria():
    x = random.randint(0, 790) 
    y = random.randint(0, 790)
    return (x//10 * 10, y//10 * 10)

#função de colisão 
def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# criando direcoes
cima = 0
direita = 1
baixo = 2
esquerda = 3

direcao = esquerda

# criando a cobrinha
cobrinha = [(200,200), (210, 200), (220,200)] # segmentos da cobrinha nas posições 
cobrinha_skin = pygame.Surface((10,10)) # altura e largura
cobrinha_skin.fill((255, 255, 255)) # cor

# criando a maçã
maca_posicao = (random.randint(0, 790), random.randint(0, 790)) # limites da tela
maca = pygame.Surface((10,10)) # tamanho e largura da maçã
maca.fill((255, 0, 0)) # cor

fonte = pygame.font.Font('BlackOpsOne-Regular.ttf', 20)
pontuacao = 0

game_over = False
while not game_over:

    #velocidade de movimentação
    clock.tick(15)

    # eventos do jogo
    for evento in pygame.event.get():
        # quando aperta o botão de fechar, o jogo sai
        if evento.type == QUIT:
            pygame.quit()
            exit()

        # direção da cobrinha com o teclado 
        if evento.type == KEYDOWN:
            if evento.key == K_UP and direcao != baixo:
                direcao = cima
            if evento.key == K_DOWN and direcao != cima:
                direcao = baixo
            if evento.key == K_LEFT and direcao != direita:
                direcao = esquerda
            if evento.key == K_RIGHT and direcao !+ esquerda:
                direcao = direita

    #ação de colidir com a maçã         
    if colisao(cobrinha[0], maca_posicao):
        maca_posicao = posicao_aleatoria() # caso haja colisão, ela deve aparecer em um lugar aleatório da tela
        cobrinha.append((0,0)) # nova posição da cobra, ela aumenta
        pontuacao = pontuacao + 1

        # caso a cobrinha colidir com o canto do jogo
    if cobrinha[0][0] == 600 or cobrinha[0][1] == 600 or cobrinha[0][0] < 0 or cobrinha[0][1] < 0:
        game_over = True
        break

        # caso a cobrinha colidir com ela mesma
    for i in range(1, len(cobrinha) - 1):
        if cobrinha[0][0] == cobrinha[i][0] and cobrinha[0][1] == cobrinha[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(cobrinha) - 1, 0, -1):
        cobrinha[i] = (cobrinha[i-1][0], cobrinha[i-1][1]) # toma posição da cauda anterior

    # posicoes da cobrinha
    if direcao == cima: 
        # quando for pra cima, a posição y diminui
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] - 10)
    if direcao == baixo:
        # quando for pra baixo, a posição y aumenta
        cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)
    if direcao == direita:
        # quando for pra direita, a posição x aumenta 
        cobrinha[0] = (cobrinha[0][0]  + 10, cobrinha[0][1])
    if direcao == esquerda: 
        # quando for pra esquerda, a posição y diminui
        cobrinha[0] = (cobrinha[0][0] - 10, cobrinha[0][1])

    for x in range(0, 600, 10): # Desenha linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600)) #posição x 
        
    for y in range(0, 600, 10)
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y)) #posição y
    
    fonte_pontuacao = fonte.render('Pontuação: %s' % (pontuacao), True, (255, 255, 255))
    pontuacao_rect = pontuacao_rect.get_rect()
    pontuacao_rect.topleft = (800 - 120, 10)
    screen.blit(fonte_pontuacao, pontuacao_rect)
    
    for posicao in cobrinha:
        screen.blit(cobrinha_skin,posicao) # desenha a cobrinha em cada posição

    pygame.display.update()

while True:
    game_over_fonte = pygame.font.Font('BlackOpsOne-Regular.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255)) # desenha o game over na tela
    game_over_rect = game_over_screen.get_rect() # alinha o game over na tela do jogo
    game_over_rect.midtop = (800 / 2, 10) # posição do game over na telado jogo
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
        
