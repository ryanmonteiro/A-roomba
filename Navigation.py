#  Modulo de localização e navegação
# 
  
#Autor: Ryan Monteiro
#Ultimo update: 15/11/2021 - 11:34

import grid_map_lib
import sweepplanner
#import numpy

#TO DO LIST

#Declarar variavel para armazenar a direção de movimento
#tipo direction

#Declarar matriz para armazenar o grid

#definição do robo
class Robot:
    def __init__(self, locationX, locationY, moveDirection):
        self.locationX = locationX
        self.locationY = locationY
        self.moveDirection = moveDirection

grid_map = grid_map_lib.GridMap(100, 120, 0.5, 10.0, -0.5)

actualRobot = Robot(0,0,0)

#De acordo com o movimento do robo e bussola irá decidir o local no grid

#if direction = 0 (direção N ou para cima no grid)
    #a cada deslocamento de bloco (x, y-1)

#if direction = 90 (direção L ou para direita no grid)
    #a cada deslocamento de bloco (x+1, y)

#if direction = 180 (direção S ou pra baixo no grid)
    #a cada deslocamento de bloco (x, y+1)

#if direction = 270 (direção O ou pra esquerda no grid)
    #a cada deslocamento de bloco (x-1, y)

#função getitem para buscar item da matriz

#função setitem para imputar valor na matriz