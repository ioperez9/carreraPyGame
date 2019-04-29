import pygame
import random
import sys
#importamos sys para que funcione quit por si no va con el de pygame

class Runner():
    
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/turtle.png")
        self.position = [x, y]
        self.name = "Tortuga"
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        

class Game():
    
    runners = []
    __startLine = 5
    __finishLine = 620
    
    def __init__(self): #esta es la parte de construccion , pantalla , del nombre y de lo que tendrá el fondo
        self.__screen = pygame.display.set_mode((640, 480)) #creación de la pantalla
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        firstRunner = Runner(self.__startLine, 240)
        firstRunner.name = "Speedy"
        self.runners.append(firstRunner)
        
        #runners.append(Runner(self.__startLine, 240))   
        #primera version hemos probado con una pelota:
        #self.runner = pygame.image.load("images/smallball.png")
    
    def competir(self): #esta es la parte dónde lo ejecuto
        gameOver = False
        while not gameOver:
            #comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                  #hasta aquí es para comprobar los eventos
            
            self.runners[0].avanzar()  #comando para que tortuga avance
            
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True
                    
            #ahora vamos a ver como hacemos el renderizado de la pantalla:
            self.__screen.blit(self.__background, (0, 0)) #blit es un nombre en pygame para Pintar, pintar la pantalla muy rápido
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            
            pygame.display.flip()
        #comando de pygame que es REFRESCA RENDERIZAR LA PANATALLA
        #estas dos instrucciones son para que al darle a la x de la ventana salgas del juego y cierre
        pygame.quit()
        sys.exit()
            
            
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()