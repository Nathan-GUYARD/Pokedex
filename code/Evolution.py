"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée la class evolutions

-----------------------------------------------------------------------------------------------------------------------"""

class Evolution:
    
    def __init__(self,idpoke,img="image\\001.png"):
        """ Initialise l'evolution du pokemon """
        self.img = img
        self.id = idpoke
        self.fils = []
        
        