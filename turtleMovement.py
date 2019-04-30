import pygame, sys
from pygame.locals import *
import random

class Runner():
    __customes = ("turtle", "fish", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = " "
        

class Game():
    def __init__(self): 
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320,240) #crear jugador y las coordenadas dónde estará
        
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():                      
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN: #si ha pulsado una tecla
                    if event.key == K_UP:
                        #mover hacia arriba runner
                        runnerY = self.runner.position[1]#extraigo la posicion Y de mi corredor
                        runnerY -= 5 #le añado 1 a ese valor
                        self.runner.position[1] = runnerY #vulevo a poner ese valor en su posición Y , es lo mismo que poner esto otro:
                        
                        #self.runner.position[1] = self.runner.position[1] + 5 o poner esto otro
                        #self.runner.position[1] += 5 , movemos 5 posiciones
                        
                    elif event.key == K_DOWN:
                        #mover hacia abajo
                        self.runner.position[1] += 5
                    elif event.key == K_LEFT:
                        #mover hacia izquierda
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:
                        #mover hacia derecha
                        self.runner.position[0] += 5
                    else:
                        pass
            
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
        

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.start()
              

                
                
                
            
                
           
                