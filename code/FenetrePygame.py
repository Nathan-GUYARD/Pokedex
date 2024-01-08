"""-----------------------------------------------------------------------------------------------------------------------

Auteur : Nathan GUYARD
Date : 18/12/2022

Role : Crée toute les variable global, notamment crée la fenètre et la liaison avec la base de donnée

-----------------------------------------------------------------------------------------------------------------------"""

from pygame import*
import mysql.connector
import os


# lance a la base de donnée
os.popen(r"ZMWSPortable\serveurZMWSPortable.exe")

# crée les couleurs
BLACK = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (220, 20, 20)

# afiche la fenetre
init()
font.init()
display.set_caption("Pokedex")
sizefenetre = [1250,920]
fenetre = display.set_mode((sizefenetre[0], sizefenetre[1]))

# crée les font
fontname = font.Font(font.get_default_font(), 30)
font = font.Font(font.get_default_font(), 20)

# se connecte a la base de donnée

Pokedex = mysql.connector.connect(
    host="localhost",
    user="root",
    password="eric",
    database="Pokedex"
)

data_base_is_load = False

while not data_base_is_load:
    try:
        curseur = Pokedex.cursor()
        data_base_is_load = True
    except:
        data_base_is_load = False





