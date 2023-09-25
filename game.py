import pygame as game

#Iniciando o jogo
game.init()
game.display.set_caption("Game")

# Config tela
largura, altura = 320, 480
tela = game.display.set_mode((largura,altura))
