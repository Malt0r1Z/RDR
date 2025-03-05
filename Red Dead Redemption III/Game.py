from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
import Stairs
from utils import getch
from Weapon import Weapon
from Piege import Piege
from handler import*
import theGame

import random, copy

class Game(object):
    """ Class representing game state """

    """ available equipments """
    equipments = {0: [Equipment("Clope", "c", usage=lambda self, hero: hero.heal()), \
                      Equipment("gold", "o"), \
                      Equipment("Bière","b",usage=lambda self, hero: hero.nourriture()),\
                      Equipment("Armure de paille", "a", usage=lambda self, hero: armure_paille(hero))],\
                  1: [Equipment("Petit tonerre","t",usage=lambda self, hero : teleport(hero,True)),\
                      Equipment("Armure cow-boy","A", usage=lambda self, hero: armure_cb(hero)),\
                      Weapon("Pistolet","p",4)],\
                  2: [Weapon("Fusil à pompe","f",6),\
                      Equipment("Armure de plomb","P", usage=lambda self, hero: armure_plomb(hero))]
                  }
    """ available monsters """
    monsters = {0: [Creature("Natif", 4,"n",poison=True), 
                    Creature("Cowboy", 2, "W")],
                1: [Creature("Sherif", 6,"S", strength=2), 
                    Creature("Loup", 10,"l")],\
                5: [Creature("Dutch", 20, strength=3,poison=False)],\
                3: [Creature("Voleur",6,".")]}

    """ available actions """
    _actions = {'z': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)), \
                'q': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)), \
                's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)), \
                'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)), \
                'i': lambda h: theGame.theGame().addMessage(h.fullDescription()), \
                'k': lambda h: h.__setattr__('hp', 0), \
                'u': lambda h: h.use(theGame.theGame().select(h._inventory)), \
                ' ': lambda h: None, \
                'h': lambda hero: theGame.theGame().addMessage("Actions disponibles : " + str(list(Game._actions.keys()))), \
                'b': lambda hero: theGame.theGame().addMessage("I am " + hero.name), \
                'r': lambda hero: theGame.theGame().repos(), \
                'a': lambda h: theGame.theGame()._floor.move(h, Coord(-1, -1)), \
                'e': lambda h: theGame.theGame()._floor.move(h, Coord(1, -1)), \
                'w': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 1)), \
                'c': lambda h: theGame.theGame()._floor.move(h, Coord(1, 1))}
    
    last_dance={"potion": Equipment("Special potion", "!", usage=lambda self, hero: heal_boost(hero)), 
                "armure": Equipment("Armure de diamant","A", usage=lambda self, hero: armure_diamant(hero)), 
                "arme": Weapon("TNT", "T", 8),
                "monstre": Creature("Pinkertons", 30, "K", strength=5)}

    def __init__(self, level=1, hero=None):
        self._level = level
        self._messages = []
        if hero == None:
            hero = Hero()
        self._hero = hero
        self._floor = None
        self._end=False
        self._deplacement=0
        self.reposer=False

    def buildFloor(self):
        from Map import Map
        self._deplacement=0
        self.reposer=False
        """Crée une map pour chaque étage"""
        if self._level<10:
            self._floor = Map(hero=self._hero)
            self._floor.put(self._floor._rooms[-1].center(), Stairs.Stairs())
            newpos=self._floor._rooms[-2].randCoord()
            while self._floor.get(newpos)!=Map.ground:
                newpos=self._floor._rooms[-2].randCoord()
            self._floor.put(newpos,Piege())
            self.marchand()
            self._level += 1 
        else:   
            self._floor = Map(hero=self._hero)
            self._floor.put(self._floor._rooms[-1].center(), self.last_dance["monstre"])
            map=self._floor
            self.addMessage("Vous êtes dans la salle du boss, finissez là")
            for i in range(1,4):
                if i==1:
                    boost=self.last_dance["potion"]
                elif i==2:
                    boost=self.last_dance["armure"]
                else:
                    boost=self.last_dance["arme"]
                carte=map._rooms[1]
                boucle=True
                while boucle:
                    new_coord = carte.randCoord()
                    if map.get(new_coord)==Map.ground:
                        map.put(new_coord, boost)
                        boucle=False

        


# Méthode de classe marchand qui place sur la carte le Marchand sur la carte
    def marchand(self):
        from Marchand import Marchand
        from Map import Map
        dealer=False
        if self._level%4==0:
            for i in self._floor._rooms:
                if self._floor.get(i.center()) == Map.ground and dealer==False:
                    self._floor.put(i.center(),Marchand())
                    dealer=True

    def addMessage(self, msg):
        """Adds a message in the message list."""
        self._messages.append(msg)

    def readMessages(self):
        """Returns the message list and clears it."""
        s = ''
        for m in self._messages:
            s += m + '. '
        self._messages.clear()
        return s

    def randElement(self, collect):
        """Returns a clone of random element from a collection using exponential random law."""
        x = random.expovariate(1 / self._level)
        for k in collect.keys():
            if k <= x:
                l = collect[k]
        return copy.copy(random.choice(l))

    def randEquipment(self):
        """Returns a random equipment."""
        return self.randElement(Game.equipments)

    def randMonster(self):
        """Returns a random monster."""
        return self.randElement(Game.monsters)

    def select(self, l):
        print("Choisit un item> " + str([str(l.index(e)) + ": " + e.name for e in l]))
        c = getch()
        if c.isdigit() and int(c) in range(len(l)):
            return l[int(c)]
    
    
    def repos(self):
        if self.reposer==False:
            for i in range(5):
                self._floor.deplIntelMonstre()
                print()
                print(self._floor)
                print(self._floor.cachemapv2())
                print(self._hero.description())
                print(self.readMessages())
            self._hero.hp+=5
            self.reposer=True


    def fatigue(self):
        self._deplacement+=1
        if self._deplacement%5==0:
            if self._hero._faim==0:
                self._hero.hp-=1
            else: 
                self._hero._faim-=1
            if self._hero._poison==True:
                self._hero.hp-=1
                return True


    def play(self):
        """Main game loop"""
        self.buildFloor()
        print("--- Welcome Hero! ---") 
        while self._hero.hp > 0 and not self._end:
            print()
            print(self._floor)
            print(self._floor.cachemapv2())  #Nuage de visibilité + (=cachemapv1) / Nuage de visibilité normal (=cachemapv1)
            print("Vous vous trouvez à l'étage " + str(self._level))
            print(self._hero.descriptionJeu())
            print(self.readMessages())
            c = getch()
            self._hero.detruire_inventory()
            if c in self._actions:
                self._actions[c](self._hero)                
            self._floor.deplIntelMonstre()
            if self._level==10 and len(self._floor._elem)==1:
                self._end=True
            self.fatigue()
        if not self._end:
            print("--- GAME OVER ---")
        else:
            print("--- Bon séjour dans le Far West ---")