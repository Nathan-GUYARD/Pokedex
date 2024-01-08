"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée la page pokedex du pokemon

-----------------------------------------------------------------------------------------------------------------------"""

from Evolution import *
from AnimationStart import *
from Button import *

class PokePage :
    
    def __init__ (self,pokeid):
        """ Initialise la page Pokedex du pokemon"""
        
        self.id = pokeid
        
        # récupère les iformation du pokemon
        curseur.execute("SELECT idpokemon,nompokemon,description,image,taille,masse,male,femelle FROM pokemon where idpokemon = "+str(self.id))
        result = curseur.fetchall()[0]
        
        # stock les information
        self.name = result[1]
        self.describe = result[2]
        self.size = result[4]
        self.masse = result[5]
        self.img = image.load(result[3])
        self.img = transform.scale(self.img, (int(215*1.5),int(215*1.5)))

        # stock le sexe du pokemon
        if result[6] == 0 and result[7] == 0:
            self.genre = "inconnue"
        
        else:
            self.genre = [None,None]
            if result[6] == 1:
                self.genre[0] = image.load("image\\male.png")
            if result[7] == 1:
                self.genre[1] = image.load("image\\femelle.png")
        
        
        # récupère le premier talent et la description
        curseur.execute("SELECT talent1,talent.description,talent2 FROM pokemon inner join talent on pokemon.talent1 = talent.nomtalent where idpokemon = "+str(self.id))
        result = curseur.fetchall()[0]
        
        # stock le premier talent du pokemon
        self.talent1 = (result[0],result[1])
        self.talent2 = None
        
        if result[2] != None:
            # récupère le deuxieme talent et la description
            curseur.execute("SELECT talent2,talent.description FROM pokemon inner join talent ON pokemon.talent2 = talent.nomtalent where idpokemon = "+str(self.id))
            result = curseur.fetchall()[0]
            # stock le deuxieme talent du pokemon
            self.talent2 = (result[0],result[1])
        
        # récupère le premier type du pokemon
        curseur.execute("SELECT type1,type.Acier,type.Combat,type.Dragon,type.Eau,type.Electrique,type.Fee,type.Feu,type.Glace,type.Insecte,type.Normal,type.Plante,type.Poison,type.Psy,type.Roche,type.Sol,type.Spectre,type.Tenebre,type.Vol,type2 FROM pokemon inner join type on pokemon.type1 = type.nomtype where idpokemon = "+str(self.id))
        result = curseur.fetchall()[0]
        
        # stock le premier type
        self.type1 = result[0]
        tabtype1 = result
        
        self.faiblesse = []
        
        if result[19] != None:
            # stock le deuxieme type
            self.type2 = result[19]
            
            # récupère les faiblesse du deuxieme type du pokemon
            curseur.execute("SELECT type2,type.Acier,type.Combat,type.Dragon,type.Eau,type.Electrique,type.Fee,type.Feu,type.Glace,type.Insecte,type.Normal,type.Plante,type.Poison,type.Psy,type.Roche,type.Sol,type.Spectre,type.Tenebre,type.Vol FROM pokemon inner join type on pokemon.type2 = type.nomtype where idpokemon = "+str(self.id))
            result = curseur.fetchall()[0]
            
            tabtype2 = result
            
            # stock les faiblesse/résistances du pokemon
            for i in range (len(tabtype2)-1):
                self.faiblesse.append(tabtype1[i+1]*tabtype2[i+1])
            
        else:
            self.type2 = None
            
            # stock les faiblesse/résistances du pokemon
            for i in range (len(tabtype1)-2):
                self.faiblesse.append(tabtype1[i+1])
        
        # compte le nombre de pokemon
        curseur.execute("SELECT COUNT(idpokemon) from pokemon")
        idmax = curseur.fetchall()[0][0]
        
        # si l'id du pokemon est 151 le prochaine est 1
        if self.id >=idmax:
            self.next = 1
        # le suivent est l'id du pokemon +1
        else:
            self.next = self.id + 1
        
        # si l'id du pokemon est 1 le précédent est 151
        if self.id <=1:
            self.old = idmax
        
        # le précédent est l'id du pokemon -1
        else :
            self.old = self.id - 1
        
        self.switch = False
        
        
    def afficherDescInfo(self,currentalent):
        """ Affiche la description du talent du pokemon """
        
        pos = (600,310)
        width = (500,210)
        
        # affiche un carrée noire
        fondBlack = Surface(width)
        fondBlack.fill((49, 49, 49))
        fenetre.blit(fondBlack, pos)
        
        # crée un boutton pour fermer la description
        self.close = Button(pos[0]+475,pos[1]+5,20,20,"image\\X.png")
        self.close.afficher()
        
        # affiche le nom du talen
        talent = fontname.render(currentalent[0] + ":", True, (255, 255, 255))
        fenetre.blit(talent, (pos[0]+25, pos[1]+10))
        
        temp = ""
        i = 0
        n=0
        
        # affiche la description du talent
        for l in currentalent[1]:
            if l == " " and i>35:
                description = font.render(temp, True, (255, 255, 255))
                fenetre.blit(description, (pos[0]+40,(n%8)*25+pos[1]+45))
                i = 0
                n+=1
                temp = ""
            else:
                temp += l
            i+=1
        description = font.render(temp, True, (255, 255, 255))
        fenetre.blit(description, (pos[0]+40,(n%8)*25+pos[1]+45))
        
        
    def afficherFicheInfo(self):
        """ Affiche les informations du pokemon """
        
        pos = [600,310]
        info=True
        
        # affiche un rectangle bleu
        fondBlue = Surface((500,210))
        fondBlue.fill((48, 167, 215))
        fenetre.blit(fondBlue, pos)
        
        pos[0] += 20
        pos[1] += 10
        
        # affiche la taille du pokemon
        nametaille = fontname.render("Taille:" , True, (0, 0, 0))
        fenetre.blit(nametaille, pos)
        pos[0] += 20
        pos[1] += 40
        taille = font.render(str(self.size) + " m", True, (0, 0, 0))
        fenetre.blit(taille, pos)
        
        pos[0] += -20
        pos[1] += 40
        
        # affiche la masse du pokemon
        namemasse = fontname.render("Masse :" , True, (0, 0, 0))
        fenetre.blit(namemasse, pos)
        pos[0] += 20
        pos[1] += 30
        masse = font.render(str(self.masse) + " Kg", True, (0, 0, 0))
        fenetre.blit(masse, pos)
        
        pos[0] += -20
        pos[1] += 40
        
        # affiche le sexe du pokemon
        namegenre = fontname.render("Sexe :" , True, (0, 0, 0))
        fenetre.blit(namegenre, pos)
        pos[0] += 20
        pos[1] += 30
        if self.genre == "inconnue": 
            genre = font.render(self.genre, True, (0, 0, 0))
            fenetre.blit(genre, pos)
        else:
            for i in range (2):
                if self.genre[i] != None:
                    fenetre.blit(self.genre[i],(pos[0]+22*i,pos[1]))
        
        pos = [850, 320]
        
        # affiche le premier talent du pokemon
        nametalent = fontname.render("Talent :" , True, (0, 0, 0))
        fenetre.blit(nametalent, pos)
        pos[0] += 20
        pos[1] += 40
        talent1 = font.render(self.talent1[0], True, (0, 0, 0))
        fenetre.blit(talent1, pos)
        
        # affiche le boutton pour afficher la description du talent
        self.infotalent1 = Button(pos[0]+190,pos[1],20,20,"image\\info.png")
        self.infotalent1.afficher()
        
        pos[1] += 80
        
        # affiche le deuxieme talent du pokemon
        if self.talent2 != None:
            talent2 = font.render(self.talent2[0], True, (0, 0, 0))
            fenetre.blit(talent2, pos)
            
            # affiche le boutton pour afficher la description du talent
            self.infotalent2 = Button(pos[0]+190,pos[1],20,20,"image\\info.png")
            self.infotalent2.afficher()
            
            
    def afficher (self):
        """ Affiche la page Pokedex du pokemon """
        fenetre.fill(RED)
        
        pos = [250,200]
        width = 215*1.5
        height = 215*1.5
        
        # affiche un carré blanc
        fondBlanc = Surface((width,height))
        fondBlanc.fill((235, 246, 253))
        fenetre.blit(fondBlanc, pos)
        
        # affiche l'image le carré blanc
        fenetre.blit(self.img, pos)
        
        pos = [500,150]
        
        # verifi si le pokemon est un nidoran pour afficher son sexe
        if self.name[0:len(self.name)-1] == "Nidoran":
            
            # affiche le nom et l'id du nidoran
            name = fontname.render("N°" + str(self.id) + " " + self.name[0:len(self.name)-1], True, (0, 0, 0))
            
            # vérifi si c'est un male
            if self.name[len(self.name)-1] == "♂":
                genreNidoran = image.load("image\\male.png")
            
            # vérifi si c'est une femelle
            else:
                genreNidoran = image.load("image\\femelle.png")
            
            # affiche le sexe du nidoran
            fenetre.blit(genreNidoran,(pos[0]+name.get_width(),pos[1]+5))
            
        else:
            # affiche le nom et l'id du pokemon
            name = fontname.render("N°" + str(self.id) + " " + self.name, True, (0, 0, 0))
            
        fenetre.blit(name, pos)
        
        # affiche les information du pokemon
        self.afficherFicheInfo()
        
        pos[0]+=100
        pos[1]+=50
        temp = ""
        i = 0
        n=0
        
        # affiche la description du pokemon
        for l in self.describe:
            if l == " " and i>40:
                description = font.render(temp, True, (0, 0, 0))
                fenetre.blit(description, (pos[0],(n%4)*25+pos[1]))
                i = 0
                n+=1
                temp = ""
            else:
                temp += l
            i+=1
        description = font.render(temp, True, (0, 0, 0))
        fenetre.blit(description, (pos[0],(n%4)*25+pos[1]))
        
        pos[0] += 400
        pos[1] = 20
        
        # affiche le boutton pour afficher le prochain pokemon
        self.buttonnext = Button(pos[0],pos[1],200,100,"image\\next.png")
        self.buttonnext.afficher()
        
        pos[0] = 50
        
        # # affiche le boutton pour afficher le pokemon précédent
        self.buttonold = Button(pos[0],pos[1],200,100,"image\\old.png")
        self.buttonold.afficher()  
        
        # récupère le nom des types
        curseur.execute("SELECT nomtype FROM type")
        result = curseur.fetchall()
        
        self.alltype = []
        self.tabbtntype = []
        x = 0
        y = 0
        pos = [600,530]
        
        # affiche le mot type
        typename = fontname.render("Type :", True, (0, 0, 0))
        fenetre.blit(typename, pos)
        
        pos[1] += 90
        
        # affiche l'intitulé des faiblesses et des résistances
        faiblessename = fontname.render("Faiblesses / Résistances :", True, (0, 0, 0))
        fenetre.blit(faiblessename, pos)
        
        pos[1] += -55
        
        # affiche le premier type du pokemon
        self.btntype1 = Button(pos[0],pos[1],45,45,"image\\"+self.type1+".png")
        self.btntype1.afficher()
        
        
        pos[0] += 100
        
        # affiche le deuxieme type du pokemon
        if self.type2 != None:
            self.btntype2 = Button(pos[0],pos[1],45,45,"image\\"+self.type2+".png")
            self.btntype2.afficher()
            
            
        pos = [598,677]
        
        # affiche les faiblesses et résistance de tout les types
        for elem in result:
            self.alltype.append(elem[0])
            
            fondBlanc = Surface((90,50))
            fondBlanc.fill((235, 246, 253))
            fenetre.blit(fondBlanc, (pos[0] + (x%6)*100,y*80+pos[1]))
            
            # affiche le type
            self.tabbtntype.append(Button(pos[0]+2 + (x%6)*100,y*80+pos[1]+3,45,45,"image\\"+self.alltype[x]+".png"))
            self.tabbtntype[x].afficher()
            
            # affiche le coefficient multiplicateur du type
            if self.faiblesse[x] == 1.0 or self.faiblesse[x] == 2.0 or self.faiblesse[x] == 4.0 or self.faiblesse[x] == 0:
                strtype = str(int(self.faiblesse[x]))
            
            else:
                strtype = "1/"+str(int(1/self.faiblesse[x]))
            
            faiblessetype = font.render("x" + strtype, True, (0, 0, 0))
            fenetre.blit(faiblessetype, (pos[0]+47 + (x%6)*100,y*80+pos[1]+23))
            
            x+=1
            if x%6 == 0:
                y += 1
        
        # affiche le boutton pour retourner au menu
        self.menu = Button(pos[0]-73,20,200,100,"image\\Menu.png")
        self.menu.afficher()
        
        # crée un boutton pour passer de l'evolution au stats du pokemon 
        self.btnswitch = Button (530,555,30,30,"image\\swip.png")
        
        # affiche les évolution du pokemon
        self.afficherevo()
        
    def afficherevo(self):
        """ Affiche la famille du pokemon """
        pos=[25,550]
        
        # affiche un carré noir
        fondBlack = Surface((550,350))
        fondBlack.fill((97, 97, 97))
        fenetre.blit(fondBlack, pos)
        
        # récupère les évolution du pokemon
        curseur.execute("SELECT * FROM evolution where idpokemon1 = " + str(self.id)+" or idpokemon2 = " + str(self.id) + " or idpokemon3 = "+str(self.id))
        result = curseur.fetchall()
        
        pos[0] += 35
        pos[1] += 10
        
        evoname = fontname.render("Évolutions :", True, (255, 255, 255))
        fenetre.blit(evoname, pos)
        
        self.imgevo = []
        self.idevo = []
        
        # si le pokemon n'evolu pas
        if result[0][2] == None:
            
            pos[0] += 20
            pos[1] += 40
        
            pasevo = font.render("Ce Pokémon n'évolue pas.", True, (255, 255, 255))
            fenetre.blit(pasevo, pos)
            
            pos[0] += 100
            pos[1] += 70
            
            # affiche un carré noir
            fondBlack = Surface((int(215*0.75),int(215*0.75)))
            fondBlack.fill((110, 110, 110))
            fenetre.blit(fondBlack, pos)
            
            # récupère l'image du pokemon
            curseur.execute("SELECT image FROM pokemon where idpokemon = " + str(self.id))
            imgpoke = curseur.fetchall()[0][0]
            
            # affiche l'image du pokemon
            self.imgevo.append(Button(pos[0],pos[1],215,215,imgpoke,0.75))
            self.idevo.append(self.id)
            
        else:
            # récupère les lignes évolutive du pokemon en partant de la première préevolution
            curseur.execute("SELECT * FROM evolution where idpokemon1="+ str(result[0][1]) +" or idpokemon2="+ str(result[0][1]) +" or idpokemon3="+ str(result[0][1]))
            result = curseur.fetchall()
            
            # récupère l'image du premiere prépokemon 
            curseur.execute("SELECT image FROM pokemon where idpokemon = " + str(result[0][1]))
            imgpoke = curseur.fetchall()[0][0]
            
            
            # affficge un carré noir en fond
            fondBlack = Surface((int(215*0.70),int(215*0.70)))
            fondBlack.fill((110, 110, 110))
            fenetre.blit(fondBlack, (40,670))
            
            # stock le premier pokemon
            poke1 = Evolution(result[0][1],imgpoke)
            self.imgevo.append(Button(40,670,215,215,poke1.img,0.70))
            self.idevo.append(result[0][1])
            
            # affiche un caractère pour le prochain pokemon
            nexte = fontname.render(">", True, (255, 255, 255))
            fenetre.blit(nexte, (197, 730))
            
            # stock les diférentes evolution possible du premier pokemon
            tabfils = []
            for evo in (result):
                existe = True
                for elem in tabfils:
                    if elem == evo[2]:
                        existe = False
                if existe:
                    tabfils.append(evo[2])
            
            
            x = 220
            y = 600
            i=0
            # cherche pour chaque evolution possible si il existe d'autres evolutions
            for elem in tabfils:
                
                # récupère l'image du pokemon
                curseur.execute("SELECT image FROM pokemon where idpokemon = " + str(elem) )
                imgpoke = curseur.fetchall()[0][0]
                poke1.fils.append(Evolution(elem,imgpoke))
                
                # si la pre evolution a une seule evolution possible
                if len(tabfils) == 1:
                    # affiche le pokemon evc un fond gris
                    fondBlack = Surface((int(215*0.70),int(215*0.70)))
                    fondBlack.fill((110, 110, 110))
                    fenetre.blit(fondBlack, (220,670))
                    self.imgevo.append(Button(220,670,215,215,poke1.fils[i].img,0.70))
                    self.idevo.append(elem)
                    
                # si il y a plus de 1 evolution possible
                elif len(tabfils) >= 2:
                    
                    # affiche le pokemon affiche le pokemon evc un fond gris
                    fondBlack = Surface((int(215*0.40),int(215*0.40)))
                    fondBlack.fill((110, 110, 110))
                    fenetre.blit(fondBlack, (x,y))
                    self.imgevo.append(Button(x,y,215,215,poke1.fils[i].img,0.40))
                    self.idevo.append(elem)
                    
                i += 1
                
                # modifie les coordonnés pour le prochain pokemon
                y += 100
                if y > 800:
                    y = 600
                    x += 110
            
            # pour toute les evolutions
            for poke in poke1.fils:
                tabfils = []
                # stock les evolutions possibles du pokemon
                for evo in result:
                    if evo[2] == poke.id and evo[3] != None:
                        existe = True
                        for elem in tabfils:
                            if elem == evo[3]:
                                existe = False   
                        if existe:
                            tabfils.append(evo[3])
                
                # si le au moins une evolution
                if len(tabfils) != 0:
                    i = 0
                    
                    # affiche un caractère pour le prochain pokemon
                    nexte = fontname.render(">", True, (255, 255, 255))
                    fenetre.blit(nexte, (377, 730))
                    
                    # pour toute les evolutions du pokemon
                    for elem in tabfils:
                        
                        # récupère l'image du pokemon
                        curseur.execute("SELECT image FROM pokemon where idpokemon = " + str(elem) )
                        imgpoke = curseur.fetchall()[0][0]
                        poke.fils.append(Evolution(elem,imgpoke))
                        
                        # si l'evolution a une seule evolution possible
                        if len(tabfils) == 1:
                            
                            # affiche le pokemon avec un fond gris
                            fondBlack = Surface((int(215*0.70),int(215*0.70)))
                            fondBlack.fill((110, 110, 110))
                            fenetre.blit(fondBlack, (400,670))
                            self.imgevo.append(Button(400,670,215,215,poke.fils[i].img,0.70))
                            self.idevo.append(elem)
                        
                        # si il y a plus de 1 evolution possible
                        elif len(tabfils) >= 2:
                            
                            # affiche le pokemon avec un fond gris
                            fondBlack = Surface((int(215*0.40),int(215*0.40)))
                            fondBlack.fill((110, 110, 110))
                            fenetre.blit(fondBlack, (x,y))
                            self.imgevo.append(Button(x,y,215,215,poke.fils[i].img,0.40))
                            self.idevo.append(elem)
                            
                        i += 1
                        x += 110
                        y += 100
        
        # affiche toutes les évolution
        for img in self.imgevo:
            img.afficher()
        
        # affiche le boutton pour afficher les stats
        self.btnswitch.afficher()
        
    def afficherStat(self):
        """ Affiche les stats du pokemon """
        
        # récupère les stat du pokemon
        curseur.execute("SELECT * from stat where idpokemon = "+str(self.id))
        result = curseur.fetchall()[0]
        
        self.btnstat = []
        
        tab = ["PV","Atk","Def","SpAtk","SpDef","Vitesse"]
        
        # crée un carré noir
        fondBlack = Surface((550,350))
        fondBlack.fill((97, 97, 97))
        
        x = 10
        stat = fontname.render("Stat :" , True, (255, 255, 255))
        fondBlack.blit(stat,(35,10))
        
        # affiche les stats du pokemon
        for i in range (1,7):
            
            # crée une barre blanche
            maxstat = Surface((80,255))
            maxstat.fill((235, 246, 253))
            
            # crée une barre en fonction du valeur de la stat
            statpoke = Surface((85,result[i]))
            statpoke.fill((48, 167, 215))
            
            # crée le nom de la stat
            statName = font.render(tab[i-1] + ":" , True, (255, 255, 255))
            
            # affiche la stat
            maxstat.blit(statpoke,(0,255-result[i]))
            fondBlack.blit(statName, (x+5,70 + 260))
            fondBlack.blit(maxstat,(x,70))
            
            # crée un boutton pour chaque stat
            self.btnstat.append((Button(x+25,620,80,255),tab[i-1]))
            
            x += 90
        
        # affiche tous
        fenetre.blit(fondBlack, (25,550))
        
        # affiche un boutton
        self.btnswitch.afficher()
        
        
        