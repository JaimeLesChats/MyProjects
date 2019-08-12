from Classes.Players import Player
from Classes.Players import Boss
import time
from random import *

#Fonction des combats

def fight():
    global stage
    #Si le joueur a plus de vitesse que le boss, il commence le combat
    if player.get_speed() > boss.get_speed():
        #tant que tout le monde a de la vie
       while player.get_health() >0 and boss.get_health() > 0:
            #attaque sur le boss
            is_crit = randint(1, 100)
            crit_dmg = randint(player.get_attack() + 1, player.get_attack() * 2)
            player.attack_boss(boss, is_crit, crit_dmg)
            #affiche l'attaque
            if is_crit < player.get_crit():
                print('{} subit {} dégats ! il lui reste {} points de vie'.format(boss.get_name(), crit_dmg, boss.get_health()))
            else:
                print('{} subit {} dégats ! il lui reste {} points de vie'.format(boss.get_name(), player.get_attack(), boss.get_health()))

            #si apres le coup le boss n'est pas mort, il attaque
            if boss.get_health() > 0:
                #attaque sur le joueur
                boss.attack_player(player)
                #affiche l'attaque
                print('Vous avez subi {} dégats ! il vous reste {} points de vie'.format(boss.get_attack(), player.get_health()))

            #si au moins une personne a plus de PV, on arrete le combat
            else:
                break

            time.sleep(0.5)

    else:
        #le boss commence le combat, tant que personne est mort
        while player.get_health() > 0 or boss.get_health() > 0:
            #attaque du boss sur le joueur
            boss.attack_player(player)
            # on affiche l'attaque
            print('Vous avez subi {} dégats ! il vous reste {} points de vie'.format(boss.get_attack(), player.get_health()))

            # Si le joueur n'est toujours pas mort, alors il attaque
            if player.get_health() > 0 :
                is_crit = randint(1, 100)
                crit_dmg = randint(player.get_attack() + 1, player.get_attack() * 2)
                # attaque du joueur sur le boss
                player.attack_boss(boss, is_crit, crit_dmg)
                # on affiche l'attaque
                if is_crit < player.crit:
                    print('{} subit {} dégats ! il lui reste {} points de vie'.format(boss.get_name(), crit_dmg, boss.get_health()))
                else:
                    print('{} subit {} dégats ! il lui reste {} points de vie'.format(boss.get_name(), player.get_attack(), boss.get_health()))

            # si finalement le joueur etait mort, on arrete le combat
            else:
                break

            time.sleep(0.5)

    # si c'est le boss qui meurt
    if boss.get_health() <= 0:
        # le joueur gagne le combat
        player.won_battle()

        #on augmente la difficultée
        player.stage_pass()

        #on augmente l'xp du joueur
        player.level_up(player.get_stage() * 3 + player.get_stage())




    #si c'est le joueur qui meurt
    elif player.get_health() <= 0:
        # le joueur a perdu
        player.lost_battle()
        if player.get_lives() == 0:
            player.start()


#MainLoop

#on met le stage a 1 et on initialise le joueur et la boucle de jeu
stage = 1
player = Player(
                "Matt", #name
                20, #health_max
                20, #health
                3,  #attack
                4, #speed
                1, #xp
                1, #level
                3, #lives
                5, #crit
                5000) #money

run = True
#debut de la boucle
while run == True:
    #on affiche le menu
    menu = ["Voulez vous :", "- Jouer ( j )", "- Afficher vos stats ( s )", "- Acceder au Magasin ( m )","- Quitter ( q )"]
    for s in menu:
        print(s)
    menu1 = input("")


    # si on veut regarder les stats
    if menu1 == "s":
        #on affiche les stats
        stats = [player.get_money(), player.get_max_health(), player.get_attack(), player.get_crit(), player.get_level(), player.get_speed(), player.get_lives(), player.get_stage()]
        stats_names = ["Money : ", "PVs : ", "Attack : ", "Crit : ", "Level : ", "Vitesse : ", "Vies : ", "Stage : "]
        stats_count = 0
        for s in stats:
            print(stats_names[stats_count], s)
            stats_count +=1
            time.sleep(0.5)

        time.sleep(2)


    # si le joueur veut quitter
    if menu1 == "q":
        #on arrete la boucle
        run = False

    # si le joueur veut acceder au magasin
    if menu1 == "m":
        magasin = ["1) Coup Crit + : 20 $", "2) Next Stage : 100 $"]
        for m in magasin:
            print(m)
        magasin1 = input("").split(" ")

        if magasin1[0] == "1":
            if player.buy(20, int(magasin1[1])) == True:
                player.market(1, int(magasin1[1]))

        if magasin1[0] == "2":
            if player.buy(100, int(magasin1[1])) == True:
                for a in range(0, int(magasin1[1])):
                    player.stage_pass()

    # si le joueur veut jouer
    if menu1 == "j":
        #on initialise le boss
        if player.get_stage() == 1:
            boss = Boss("DIDIER", 50, 1, 2)
        elif player.get_stage() == 2:
            boss = Boss("FRANCIS", 130, 2, 2)
        elif player.get_stage() == 3:
            boss = Boss("JEAN MICHEL", 270, 3, 3)
        elif player.get_stage() == 4:
            boss = Boss("BRUNO", 390, 3, 3)
        elif player.get_stage() == 5:
            boss = Boss("ROBERT", 510, 7, 3)
        elif player.get_stage() == 6:
            boss = Boss("MARVICK",620, 4, 4)
        elif player.get_stage()== 7:
            boss = Boss("LEON", 1360, 2, 3)
        elif player.get_stage() == 8:
            boss = Boss("BERNARD", 780, 12, 5)
        else:
            continue


        # on montre au joueur le boss qu il va affronter
        print("Vous etes au stage {}, vous allez vous battre contre {}, un Boss avec {} point(s) de vie et {} point(s) d'attaque".format(player.get_stage(), boss.get_name(), boss.get_health(), boss.get_attack() ))
        time.sleep(5)
        # on commence le combat
        fight()


    #ChEaT cOdEs
    if menu1 == "cheat123":
        player.level_up(100)
				
#boucle finie, le programme s arrete on affiche un message gentil :)
print("Merci d'avoir joué !")







#__________________________________________________________________________________



from math import *
import time
from random import *

#classe du joueur
class Player:

    def __init__(self, name, health, max_health, attack, speed, xp, level, lives, crit, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.xp = xp
        self.level = level
        self.speed = speed
        self.lives = lives
        self.max_health = max_health
        self.crit = crit
        self.money = money
        self.stage = 1

    #Fonctions des propriétés du joueur

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack
    def get_xp(self):
        return self.xp

    def get_level(self):
        return self.level

    def get_speed(self):
        return self.speed

    def get_lives(self):
        return self.lives

    def get_max_health(self):
        return self.max_health

    def get_crit(self):
        return self.crit

    def get_money(self):
        return self.money

    def get_stage(self):
        return self.stage


    #Autres fonctions ____________________


    def start(self):
        self.max_health = 20
        self.health = 20
        self.attack = 3
        self.speed = 4
        self.xp = 1
        self.level = 1
        self.lives = 3
        self.crit = 5
        self.money = 10
        self.stage = 1

    # fonction pour recevoir des degats, a ne pas appeler, fonctionne avec attack_player() du Boss
    def damage(self, damage):
        self.health -= damage


    #fonction a appeler pour attaquer le boss
    def attack_boss(self, boss, is_crit, crit_dmg):
        if is_crit <= self.crit:
            damage = crit_dmg
            print("Vous avez fait un coup critique !")
        else:
            damage = self.attack
        boss.damage(damage)

    #fonction qui augmente l'xp de joueur + fait passer de level si jamais en augmentant les stats
    def level_up(self, xp_gained): #Fonctionne
        # xp a atteindre pour le niveau suivant
        xp_pass = round(self.level * 1.5 + self.level, 1)

        #si le joueur a plus d'xp que xp a atteindre, il monte d'un niveau
        if  self.xp + xp_gained >= xp_pass:
            #boucle si jamais il monte de plusieurs niveaux
            while self.xp + xp_gained >= xp_pass:
                # augmente le niveau
                self.level += 1
                #augmente les stats
                self.max_health += 4 + self.level
                self.attack += 1 + self.level
                # pour ne pas avoir + de 100% de crit
                self.crit += 3
                if self.crit >100:
                    self.crit = 100

                # on lui donne l'xp supplementaire
                self.xp = self.xp + xp_gained - xp_pass
                xp_gained = 0
                # on change l'xp a atteindre
                xp_pass = round(self.level * 1.5 + self.level, 1)
                #on affiche au joueur qu'il vient de monter d'un niveau
                print("Level Up ! You are now level {} with {} xp !".format(self.level, self.xp))
                time.sleep(1)

        # si le joueur ne monte pas de niveau en gagnant de l'xp
        else:
            # on lui ajoute simplement l'xp qu il vient de gagner
            self.xp += xp_gained

    #permet de voir si un objet est achetable ou non
    def buy(self, price, quantity):
        if self.money  > price * quantity:
            self.money -= price * quantity
            return True
        else:
            print("Vous n'avez pas assez d'argent !")
            time.sleep(1)
            return False

    #ajoute au joueur l'item acheté au market
    def market(self, item, quantity):
        if item == 1:
            self.crit += 10 * quantity

        print("Vous avez bien acheté votre Item !")
        time.sleep(1)

    def stage_pass(self):
        self.stage += 1


    # fonction a appeler quand le joueur perd le combat
    def lost_battle(self): # pas fini
        # le joueur perd une vie
        self.lives -= 1

        #si il lui reste des vies
        if self.lives != 0:
            print("Vous avez perdu le combat, il vous reste encore {} vies !".format(self.lives))
            #on remet ses points de vie
            self.health = self.max_health

        #si il n'a plus de vies
        else:
            print("Vous avez perdu le combat, il ne vous reste plus de vies... Vous allez recommencer la partie !")
        time.sleep(2)


    #fonction a appeler quand le joueur gagne le combat
    def won_battle(self):
        self.health = self.max_health
        # message de victoire
        print("Vous avez gagné le combat ! Vous remportez {} xp !".format(self.stage * 3 + self.stage))
        self.money += self.level * 2 + self.stage
        print("Vous venez de gagner {} $ !".format(self.level * 2 + self.stage))



# Classe du boss
class Boss:
    def __init__(self, name, health, attack, speed):
        self.health = health
        self.attack = attack
        self.name = name
        self.speed = speed

    #Fonctions des propriétés du boss

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_speed(self):
        return self.speed

    #Autres fonctions

    #fonction de degats sur le boss qui marche avec attack_boss, ne s'appelle pas
    def damage(self, damage):
        self.health -= damage

    #fonction pour infliger des degats au joueur, qui s'appelle
    def attack_player(self,player):
        damage = self.attack
        player.damage(damage)
	
	
