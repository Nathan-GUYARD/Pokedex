"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Gère le menu du Pokedex 

-----------------------------------------------------------------------------------------------------------------------"""

from Button import *

class PokemonMenu :
    
    def __init__ (self,x,y,idpoke,namepoke,img):
        """ Initialise un pokemon à afficher sur le menu """
        
        self.pos = (x,y)
        self.id = idpoke
        self.name = namepoke
        
        # crée un boutton
        self.button = Button(x,y,215,215,img)
        
        
    def afficher (self):
        """ Affiche le pokemon """
        
        # affiche un fond blanc
        fondBlanc = Surface((self.button.width,self.button.height))
        fondBlanc.set_alpha(255)
        fondBlanc.fill((235, 246, 253))
        
        fenetre.blit(fondBlanc, self.pos)
        
        # affiche l'image du pokemon
        self.button.afficher()
        
        # verifi si le pokemon est un nidoran pour afficher son sexe
        if self.name[0:len(self.name)-1] == "Nidoran":
            
            # affiche le nom de nidoran
            Name = font.render(self.name[0:len(self.name)-1], True, (0, 0, 0))
            
            # vérifi si c'est un male
            if self.name[len(self.name)-1] == "♂":
                genreNidoran = image.load("image\\male.png")
            
            # vérifi si c'est une femelle
            else:
                genreNidoran = image.load("image\\femelle.png")
            
            # affiche le sexe du nidoran
            fenetre.blit(genreNidoran,(self.pos[0]+5+Name.get_width(),self.pos[1]+195))
            
        else:
            # affiche le nom du pokemon 
            Name = font.render(self.name, True, (0, 0, 0))
        
        fenetre.blit(Name, (self.pos[0]+5, self.pos[1]+195))
        
        # affiche l'id du pokemon
        Id = font.render("N°"+str(self.id), True, (0, 0, 0))
        fenetre.blit(Id, (self.pos[0]+5, self.pos[1]+5))
        
        
def Menu (pokemin,pokemax,mode,sizefenetre):
    """ Récupère les pokemon présent dans la menu """
    
    fenetre.fill(RED)
    
    # envoi une requete qui selection les infos des pokemons
    curseur.execute("SELECT pokemon.idpokemon,nompokemon,image FROM pokemon "+ mode[2] + mode[3] + " order by "+ mode[0] + " " + mode [1])
    result = curseur.fetchall()
    
    tabpoke=[]
    
    n = pokemin - 1
    i = 0
    y = 75
    
    ecartx = (sizefenetre[0] - 415)/3
    ecarty = (sizefenetre[1] - 415)/2
    
    # récupere le nombre de pokemon qui a été récupéré
    curseur.execute("SELECT COUNT(idpokemon) from pokemon "+mode[3])
    idmax = curseur.fetchall()[0][0]
    
    # stock tout les pokemon dans un tableau
    while n < pokemax and n < idmax:
        elem = result[n]
        
        #defini la coordonné x
        x = (n % 4)*ecartx + 100
        
        # ajoute au tableau le pokemon
        tabpoke.append(PokemonMenu(x,y,elem[0],elem[1],elem[2]))
        tabpoke[i].afficher()
        
        i += 1
        n += 1
        
        # si 3 pokemon son passer augmente la coordonné y
        if (n) % 4 == 0:
            y += ecarty
    
    return tabpoke

