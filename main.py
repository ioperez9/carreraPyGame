import pygame
import sys
#importamos sys para que funcione quit por si no va con el de pygame

class Game():
    
    corredores = []
    
    def __init__(self): #esta es la parte de construccion , pantalla , del nombre y de lo que tendrá el fondo
        
        self.__screen = pygame.display.set_mode((640, 480)) #creación de la pantalla
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        self.runner = pygame.image.load("images/smallball.png")
        
    
    def competir(self): #esta es la parte dónde lo ejecuto
        
        x = 0
        hayGanador = False
        
        while not hayGanador:
            #comprobación de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    #hasta aquí es para comprobar los eventos
                    
            #ahora vamos a ver como hacemos el renderizado de la pantalla:
            self.__screen.blit(self.background, (0,0)) #blit es un nombre en pygame para Pintar, pintar la pantalla
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip() #comando de pygame que es REFRESCA RENDERIZAR LA PANATALLA
            
            x += 3
            if x >= 250:
                hayGanador = True
        
        pygame.quit()
        sys.exit()
        
            
            
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()