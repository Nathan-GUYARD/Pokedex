"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée la class boutton

-----------------------------------------------------------------------------------------------------------------------"""

from FenetrePygame import *

class Button:
    
    def __init__ (self,x,y,width,height,img = None,scale=1):
        """ Initialise le boutton """
        
        # stock la position et la largeur du boutton+
        self.pos = (x,y)
        self.height = int(height * scale)
        self.width = int(width * scale)
        
        #verifi si il le boutton a une image
        if img != None:
            # stock l'image
            self.img = image.load(img)
            self.img = transform.scale(self.img, (self.width,self.height))
        else:
            self.img = None
        
    def IsClic (self,pos):
        """ Vérifie si le boutton est cliquer """
        clic = False
        
        # vérifi la colision avec le boutton
        if pos[0] >= self.pos[0] and pos[0] <= self.pos[0] +self.width and pos[1] >= self.pos[1] and pos[1] <= self.pos[1] + self.height:
            clic = True
        
        return clic
    
    
    def afficher (self):
        """ Affiche le boutton """
        
        if self.img != None:
            # affiche le boutton
            fenetre.blit(self.img,self.pos)
            
            
            