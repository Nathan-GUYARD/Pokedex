"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée les fonctions qui permet de faire des animation 

-----------------------------------------------------------------------------------------------------------------------"""

from FenetrePygame import *
from AnimationClass import*
from math import*

def horizontalToTopAnim (animation):
    """ Bouge le trait de l'orizontal au coin de l'ecran"""
    
    if animation.isPlaying and animation.canPlay:
        
        fenetre.fill(RED)
        
        # affiche un ligne noir qui bouge vers le haut
        draw.polygon(fenetre, BLACK, [(0,(sizefenetre[1]-animation.value1)//2),(sizefenetre[0],(sizefenetre[1]-animation.value2)//2),
                                                (sizefenetre[0],(sizefenetre[1]+animation.value1)//2),(0,(sizefenetre[1]+animation.value2)//2)])
        
        
        # affiche un rond noir et un rond blnc au centre de l'image
        draw.circle(fenetre, BLACK, (sizefenetre[0]//2, sizefenetre[1]//2), 200)
        draw.circle(fenetre, WHITE, (sizefenetre[0]//2, sizefenetre[1]//2), 110)
        
        # change les valeurs
        animation.value1 += 10
        animation.value2 += -10
        
        # si l'animation est fini change ces parametres
        if (sizefenetre[1]+animation.value2)//2+(sizefenetre[1]-animation.value1)//2 == -200:
            animation.finishAnim()
                


def topToVerticalAnim(animation):
    """ Bouge le trait du coin à la verticale de l'ecran """
    
    if animation.isPlaying and animation.canPlay:
        
        fenetre.fill(RED)
        # affiche un ligne noir qui bouge vers le la droite 
        draw.polygon(fenetre, BLACK, [((sizefenetre[0]-animation.value1)//2,0),((sizefenetre[0]+animation.value2)//2,0),
                                                ((sizefenetre[0]+animation.value1)//2,sizefenetre[1]),
                                                ((sizefenetre[0]-animation.value2)//2,sizefenetre[1])])
        
        # affiche un rond noir et un rond blnc au centre de l'image
        draw.circle(fenetre, BLACK, (sizefenetre[0]//2, sizefenetre[1]//2), 200)
        draw.circle(fenetre, WHITE, (sizefenetre[0]//2, sizefenetre[1]//2), 110)
        
        # change les valeur
        animation.value1 += -10
        animation.value2 += 10
        
        # si l'animation est fini change ces parametres
        if animation.value1 <= 190 :
            animation.finishAnim()
                


def blackToWhiteMiddleButtonAnim (animation):
    """ Change la couleur du rond blanc en un rond noir """
    
    if animation.isPlaying and animation.canPlay:
        # affiche le cercle de plus en plus noir
        draw.circle(fenetre, (animation.value1,animation.value1,animation.value1), (sizefenetre[0]//2, sizefenetre[1]//2), 110)
        
        # change la valeur
        animation.value1 += -1
        
        # si l'animation est fini change ces parametres
        if animation.value1 < 20:
            animation.finishAnim()
                
            
def horizontalSlideAnim (animation):
    """ Ouvre le Pokedex """
    
    if animation.isPlaying and animation.canPlay:
        fenetre.fill(RED)
        # affiche un ligne noir vretical qui grossi
        draw.polygon(fenetre, BLACK, [((sizefenetre[0]-animation.value1)//2,0),((sizefenetre[0]+animation.value1)//2,0),
                                                ((sizefenetre[0]+animation.value1)//2,sizefenetre[1]),
                                                ((sizefenetre[0]-animation.value1)//2,sizefenetre[1])])
        
        # affiche 2 rond qui vont vers les 2 cotés oposer de l'ecran
        draw.circle(fenetre, BLACK, ((sizefenetre[0]-animation.value1)//2, sizefenetre[1]//2), 200)
        draw.circle(fenetre, BLACK, ((sizefenetre[0]+animation.value1)//2, sizefenetre[1]//2), 200)
        
        # change la valeur
        animation.value1 += 12
        
        # si l'animation est fini change ces parametres
        if (sizefenetre[0]-animation.value1)//2 < -10:
            animation.finishAnim()
            
def fonduAnim (animation,streght):
    """ Cree un fondu """
    
    if animation.isPlaying and animation.canPlay:
        
        # cree une surface noir avec une certaine opacité qui augmente ou diminu
        transi = Surface(sizefenetre)
        transi.set_alpha(animation.value1)
        transi.fill(BLACK)
        fenetre.blit(transi,(0,0))
        
        # change la valeur
        animation.value1 += -50*streght
        
        # selon le sens de l'animation change la condition de fin d'animation
        if streght > 0:
            if animation.value1 < 0 :
                animation.finishAnim()
            
        else:
            if animation.value1 > 100 :
                animation.finishAnim()
                
            elif animation.value1 > 20:
                animation.value1 += 1
                
                
    
def roundLargestTransiAnim(animation,streght):
    """ Cree une transition avec un rond """
    
    if animation.isPlaying and animation.canPlay:
        
        # crée une surface noire
        blackSurf = Surface(sizefenetre,SRCALPHA)
        blackSurf.fill(BLACK)
        # ajoute a la surface noir un cercle transparent qui grandi
        draw.circle(blackSurf, (0,0,0,0), ((sizefenetre[0]//2,sizefenetre[1]//2)), animation.value1)
        fenetre.blit(blackSurf,(0,0))
        
        # change la valeur
        animation.value1 += 20*streght
        
        # si l'animation est fini change ces parametres
        if animation.value1 > sqrt((sizefenetre[0]//2+50)**2+(sizefenetre[1]//2)**2+50):
            animation.finishAnim()
    
    
    
    
    
    
    
    
    
