import pygame
import random
import sys
#importamos sys para que funcione quit por si no va con el de pygame

class Runner():
    __customes = ("turtle", "fish", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = " "
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        

class Game():
    
    runners = []
    __posY = (50, 150, 250, 350)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
    __startLine = -5
    __finishLine = 620
    
    def __init__(self): #esta es la parte de construccion , pantalla , del nombre y de lo que tendrá el fondo
        self.__screen = pygame.display.set_mode((640, 480)) #creación de la pantalla
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range (4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
        #runners.append(Runner(self.__startLine, 240))   
        #primera version hemos probado con una pelota:
        #self.runner = pygame.image.load("images/smallball.png")
    
    def close(self):
        pygame.quit()
        sys.exit()
    
    
    def competir(self): #esta es la parte dónde lo ejecuto
        gameOver = False
        while not gameOver:
            #comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                  #hasta aquí es para comprobar los eventos
                    
            for activeRunner in self.runners:
                activeRunner.avanzar()  #comando para que tortuga avance
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
                    
            #ahora vamos a ver como hacemos el renderizado de la pantalla:
            self.__screen.blit(self.__background, (0, 0)) #blit es un nombre en pygame para Pintar, pintar la pantalla muy rápido
            
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()
        #comando de pygame que es REFRESCA RENDERIZAR LA PANATALLA
        #estas dos instrucciones son para que al darle a la x de la ventana salgas del juego y cierre
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                
              
        
                  
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()