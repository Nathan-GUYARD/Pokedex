"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée la class animation  

-----------------------------------------------------------------------------------------------------------------------"""

class Animation:
    def __init__(self,x,y=None,animationnext = None):
        """ Initailise les parametre de l'animation """
        
        # défini l'animation suivante
        self.next = animationnext
        
        # initialise les valeurs
        self.value1 = x
        self.value2 = y
        self.defaultvalue1 = self.value1
        self.defaultvalue2 = self.value2
        
        # l'animation n'est pas en train d'etre jouer mais peux etre lancer
        self.canPlay = True
        self.isPlaying = False
        
        
    def finishAnim (self):
        """ Change les parametres de l'animation quand elle est fini """
        
        # change les parametres de l'animation
        self.isPlaying = False
        self.canPlay = False
        
        # réinitialise les valeur
        self.value1 = self.defaultvalue1
        self.value2 = self.defaultvalue2
        
        # lance l'animation suivante si elle existe
        if self.next != None:
            if self.next.canPlay:
                self.next.restart()
                
    
    def restart(self):
        """ reinitialise l'animation """
        
        self.canPlay = True
        self.isPlaying = True
        