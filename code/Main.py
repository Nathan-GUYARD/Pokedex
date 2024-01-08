"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Permet de lancer et géré le pokedex

-----------------------------------------------------------------------------------------------------------------------"""

from pokepage import *
from Menu import * 
        
def main ():
    """ Gère le Pokedex """
    
    fenetre.fill(RED)
    
    # affiche le pokedex
    draw.polygon(fenetre, BLACK, [(0,sizefenetre[1]//2-100),(sizefenetre[0],sizefenetre[1]//2-100),(sizefenetre[0],sizefenetre[1]//2+100),(0,sizefenetre[1]//2+100)], 0) 
    draw.circle(fenetre, BLACK, (sizefenetre[0]//2, sizefenetre[1]//2), 200)
    draw.circle(fenetre, WHITE, (sizefenetre[0]//2, sizefenetre[1]//2), 110)
    
    # défini les animation
    roundtransi = Animation(0)
    transi2 = Animation(300)
    transi1 = Animation(0,None,transi2)
    anim4 = Animation(200,None,transi2)
    anim3 = Animation(255,None,anim4)
    anim2 = Animation(1100,-700,anim3)
    anim1 = Animation(200,200,anim2)
    
    
    # initialise toutes les variables
    pokemin = 1
    pokemax = 12
    mode = ["idpokemon ","asc","",""]
    refresh = True
    end = True
    InPokepage = False
    InMenu = False
    info = False
    InType = False
    InStart = True
    
    # initialise les variables des animations/transitions
    lastAnimIsStart = False
    FullTransi = False
    isTransiPart1 = False
    isTransiPart2 = False
    Poketransi = False
    
    
    while end == True:
        
        # récupère les input
        evente = event.poll()
        if evente.type == MOUSEBUTTONUP:
            pos_mouse = mouse.get_pos()
        
        if InStart:
            
            if evente.type == MOUSEBUTTONUP:
                pos_mouse = mouse.get_pos()
                anim1.isPlaying = True
            
            #execute les animations
            horizontalToTopAnim(anim1)
            topToVerticalAnim(anim2)
            blackToWhiteMiddleButtonAnim(anim3)
            horizontalSlideAnim(anim4)
            
            # vérifi si la derniere animation est fini
            if lastAnimIsStart:
                if not(transi2.isPlaying):
                    
                    lastAnimIsStart = False
                    InStart = False
            
            # vérifi si la derniere animation est lancé
            if transi2.isPlaying:
                lastAnimIsStart = True
                InMenu = True
         
        if (InMenu and (isTransiPart2 or refresh or lastAnimIsStart)):
            
            # récupère les pokemons le la page
            tabpokemon = Menu (pokemin,pokemax,mode,sizefenetre)
            
            # compte le nombre de pokemon au total
            curseur.execute("SELECT COUNT(idpokemon) from pokemon "+ mode[3])
            idmax = curseur.fetchall()[0][0]
            
            # affiche le boutton pour aller à la page suivante 
            nextpage = Button(sizefenetre[0]-215,sizefenetre[1]-115,200,100,"image\\next.png")
            if pokemax < idmax:
                nextpage.afficher()
            
            # affiche le boutton pour aller à la page précédente 
            oldpage = Button(15,sizefenetre[1]-115,200,100,"image\\old.png")
            if pokemin >1: 
                oldpage.afficher()
            
            ecart = (sizefenetre[0] - 300)/3
            
            # affiche les bouttons de trie
            alphacroi = Button(75 + 2*ecart,10,150,50,"image\\A-Z.png")
            alphacroi.afficher()
            alphadecroi = Button(75 + 3*ecart,10,150,50,"image\\Z-A.png")
            alphadecroi.afficher()
            idcroi = Button(75,10,150,50,"image\\1-N.png")
            idcroi.afficher()
            iddecroi = Button(75 + ecart,10,150,50,"image\\N-1.png")
            iddecroi.afficher()
            
            # affiche le boutton du Menu
            if InType:
                btnMenu = Button(500,800,200,100,"image\\Menu.png")
                btnMenu.afficher()
                
            refresh = False
            
        if InMenu and not(FullTransi):
                    
            if evente.type == MOUSEBUTTONUP:
                pos_mouse = mouse.get_pos()
                
                # si le boutton est presser passe à la page suivante
                if nextpage.IsClic(pos_mouse):
                    if pokemax < idmax:
                        pokemin += 12
                        pokemax += 12
                        
                        refresh = True
                
                # si le boutton est presser passe à la page précédente
                if oldpage.IsClic(pos_mouse):
                    if pokemin > 1:
                        pokemin += -12
                        pokemax += -12
                        
                        refresh = True
                
                # si le boutton est presser change de méthode de tri
                if idcroi.IsClic(pos_mouse):
                    mode[0] = "idpokemon "
                    mode[1] = "asc"
                    mode[2] = ""
                    
                    pokemin = 1
                    pokemax = 12
                    
                    refresh = True
                
                # si le boutton est presser change de méthode de tri
                if iddecroi.IsClic(pos_mouse):
                    mode[0] = "idpokemon "
                    mode[1] = "desc"
                    mode[2] = ""
                    pokemin = 1
                    pokemax = 12
                    
                    refresh = True
                
                # si le boutton est presser change de méthode de tri
                if alphacroi.IsClic(pos_mouse):
                    mode[0] = "nompokemon "
                    mode[1] = "asc"
                    mode[2] = ""
                    
                    pokemin = 1
                    pokemax = 12
                    
                    refresh = True
                
                # si le boutton est presser change de méthode de tri
                if alphadecroi.IsClic(pos_mouse):
                    mode[0] = "nompokemon "
                    mode[1] = "desc"
                    mode[2] = ""
                    
                    pokemin = 1
                    pokemax = 12
                    
                    refresh = True

                # si un pokemon est presser affiche la page de ce pokemon
                for poke in tabpokemon:
                    if poke.button.IsClic(pos_mouse):
                        
                        pokemonsel = PokePage (poke.id)
                        
                        FullTransi = True
                        Poketransi = True
                        transi1.restart()
                        
                        InMenu = False
                        InPokepage = True
                        info=False
                
                # si le boutton est presser retourne au menu de base
                if InType:
                    if btnMenu.IsClic(pos_mouse):
                        
                        pokemin = 1
                        pokemax = 12
                        
                        mode = ["idpokemon","asc","",""]
                        refresh = True
                        InType = False
            
                
        if InPokepage :
            
            if isTransiPart2:
                pokemonsel.afficher()
                
            if not(FullTransi):
                if evente.type == MOUSEBUTTONUP:
                    pos_mouse = mouse.get_pos()
                    
                    # change de pokemon vers le suivant
                    if pokemonsel.buttonnext.IsClic(pos_mouse):
                        pokemonsel = PokePage (pokemonsel.next)
                        pokemonsel.afficher()
                        
                        info=False
                    
                    # change de pokemon vers le précédent
                    if pokemonsel.buttonold.IsClic(pos_mouse):
                        pokemonsel = PokePage (pokemonsel.old)
                        pokemonsel.afficher()
                        
                        info=False
                    
                    # retourne au menu
                    if pokemonsel.menu.IsClic(pos_mouse):
                        FullTransi = True
                        transi1.restart()
                        
                        InPokepage = False
                        InMenu = True
                        info = False
                        InType = False
                        
                        pokemin = 1
                        pokemax = 12
                        
                        mode = ["idpokemon","asc","",""]
                    
                    # affiche les information du pokemon
                    if info:
                        if pokemonsel.close.IsClic(pos_mouse):
                            pokemonsel.afficherFicheInfo()
                            
                            info=False
                            
                    else:
                        # affiche la description de premier talent
                        if pokemonsel.infotalent1.IsClic(pos_mouse):
                            pokemonsel.afficherDescInfo(pokemonsel.talent1)
                            info=True
                        
                        # affiche la description de deuxième talent
                        if pokemonsel.talent2 != None:
                            if pokemonsel.infotalent2.IsClic(pos_mouse):
                                pokemonsel.afficherDescInfo(pokemonsel.talent2)
                                info=True
                    
                    if pokemonsel.btnswitch.IsClic(pos_mouse):
                        # affiche les évolutions du pokemon
                        if pokemonsel.switch:
                            pokemonsel.switch = False
                            pokemonsel.afficherevo()
                        
                        # affiche les Stats du Pokemon
                        else:
                            pokemonsel.switch = True
                            pokemonsel.afficherStat()
                    
                    if not(pokemonsel.switch):
                        # affiche la page de l'évolution du pokemon
                        for i in range (len(pokemonsel.imgevo)):
                            if pokemonsel.imgevo[i].IsClic(pos_mouse):
                                pokemonsel = PokePage (pokemonsel.idevo[i])
                                pokemonsel.afficher()
                                
                                info=False
                    else:
                        # affiche les pokemons triée par rapport au stats des pokemon
                        for i in range (len(pokemonsel.btnstat)):
                            if pokemonsel.btnstat[i][0].IsClic(pos_mouse):
                                mode = [pokemonsel.btnstat[i][1],"desc","inner join stat on pokemon.idpokemon = stat.idpokemon ",""]
                                
                                FullTransi = True
                                transi1.restart()
                                
                                InMenu = True
                                InType = True
                                InPokepage = False
                                
                                pokemin = 1
                                pokemax = 12
                        
                    # affiche tout les pokemon du premier type du pokemon
                    if pokemonsel.btntype1.IsClic(pos_mouse):
                        
                        mode = ["idpokemon","asc","","where type1 = '" + pokemonsel.type1 + "' or type2 = '" + pokemonsel.type1 + "'"]
                        FullTransi = True
                        transi1.restart()
                        
                        InMenu = True
                        InType = True
                        InPokepage = False
                        
                        pokemin = 1
                        pokemax = 12
                    
                    # affiche tout les pokemon du deuxieme type du pokemon
                    if pokemonsel.type2 != None:
                        if pokemonsel.btntype2.IsClic(pos_mouse):
                            
                            mode = ["idpokemon","asc","","where type1 = '" + pokemonsel.type2 + "' or type2 = '" + pokemonsel.type2 + "'"]
                            FullTransi = True
                            transi1.restart()
                            
                            InMenu = True
                            InType = True
                            InPokepage = False
                            
                            pokemin = 1
                            pokemax = 12
                    
                    # affiche tout les pokemon du certain type
                    for i in range (len(pokemonsel.tabbtntype)):
                        if pokemonsel.tabbtntype[i].IsClic(pos_mouse):
                            
                            mode = ["idpokemon","asc","","where type1 = '" + pokemonsel.alltype[i] + "' or type2 = '" + pokemonsel.alltype[i] + "'"]
                            
                            FullTransi = True
                            transi1.restart()
                            
                            InMenu = True
                            InType = True
                            InPokepage = False
                            
                            pokemin = 1
                            pokemax = 12
        
        # lance le fondu
        if lastAnimIsStart:
            fonduAnim(transi2,1)
            
            refresh = True
        
        if FullTransi:
            # joue les animations
            fonduAnim(transi1,-0.003)
            fonduAnim(transi2,1)
            roundLargestTransiAnim(roundtransi,2)
            
            # quand la premiere partie de la transition est fini
            if isTransiPart1 and not(transi1.isPlaying):
                # lance la transition avec un cercle
                if Poketransi:
                    roundtransi.restart()
                
                # lance la transition en fondu
                else:
                    transi2.restart()
                
                isTransiPart1 = False
            
            # quand la 1 partie de la transition est en train d'être joué
            if transi1.isPlaying:
                isTransiPart1 = True
                
            # quand la 2 partie de la transition est en train d'être joué
            if roundtransi.isPlaying or transi2.isPlaying:
                isTransiPart2 = True
            
            # quand la 2 partie est fini
            if isTransiPart2 and (not(roundtransi.isPlaying) and not(transi2.isPlaying)):
                isTransiPart2 = False
                FullTransi = False
                Poketransi = False
            
        display.flip()
        
        if evente.type == QUIT :
            # met fin a la boucle principale
            end = False
            # ferme la fenetre
            quit()
            
main()


