from Creature import Creature

class Hero(Creature):
    """The hero of the game.
        Is a creature. Has an inventory of elements. """
    def __init__(self, name="Hero", hp=75, abbrv="@", strength=2,xp=0,level=0,hpmax=75,poison=False,faim=30,gold=10):
        Creature.__init__(self, name, hp, abbrv, strength)
        from Weapon import Weapon

        self._inventory = []
        self._poison=poison
        self.xp=xp
        self.level=level
        self.hpmax=hpmax
        self._faim=faim
        self.base_weapon = Weapon("bâton","h",0)
        self.weapon = self.base_weapon
        self.gold=gold
        self.armure=None

    def description(self):
        """Description of the hero"""
        return Creature.description(self)

    
    def descriptionJeu(self):
        # Description du héros dans le jeu
        return '\n'+'HP : '+ Creature.description(self) \
            + " sur : " + str(self.hpmax) + '\n' \
            +'Inventaire : '+ str(self._inventory) + '\n' \
            +'XP : '+ str(self.xp) + '\n' \
            + "Niveau : " + str(self.level) + '\n' \
            + "Taux d'alcoolémie : "+str(self._faim) + '\n' \
            + "Or : " + str(self.gold) + '\n' \
        + ("Vous êtes empoisonné !" if self._poison else "")+ '\n' \
        + ("Vous allez mourir de faim !" if self._faim==0 else "")

    def fullDescription(self):
        """Complete description of the hero"""
        res = ''
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory])
        return res

    def checkEquipment(self, o):
        from Equipment import Equipment
        """Check if o is an Equipment."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """The hero takes adds the equipment to its inventory"""
        self.checkEquipment(elem)
        if elem.name!="gold":
            self._inventory.append(elem)
        else:
            self.gold+=1

    def use(self,item):
        """
        use or equip an Equipement
        :param item: Equipement instance
        """
        from Weapon import Weapon
        from Equipment import Equipment
        from Piege import Piege
        # print("in hero use, with item",item)
        if item == None:
            return None
        self.checkEquipment(item)
        if item not in self._inventory:
            raise ValueError("Not in inventory",item,self._inventory)
        else:
            if isinstance(item,Weapon):
                item.equip(self)
            elif isinstance(item,Equipment):
                item.use(self)
                self._inventory.remove(item)
        if isinstance(item,Piege):
                item.meet(self)
        
    def heal(self):
        self.hp += 3
        self._poison=False
        return True
    

#(1) Nourriture : Le héros à un niveau de satiété (par ex. 20) qui descend chaque X
#actions (par ex. 3). Si le héros tombe à 0 en satiété, il perd un hp chaque X action,
#jusqu’à ce qu’il utilise une nourriture, il revient alors au niveau initial de satiété.
    
    
    def nourriture(self):
        self._faim+=5
        return True


# Méthode qui dédruit les équipements lorsque l'inventaire est rempli (>10)
    def detruire_inventory(self):
        from utils import getch
        from Equipment import Equipment
        if len(self._inventory)>10:
            retire=True
            print("Vous êtes trop lourds, débarassez-vous d'un objet > " + 
str([str(self._inventory.index(e))+": " + e.name for e in self._inventory]))
            while retire:
                c = getch()
                if c.isdigit() and int(c) in range(len(self._inventory)) and int(c)!=Equipment("gold","o"):
                    self._inventory.remove(self._inventory[int(c)])
                    retire=False

    #(1)Quand il change de niveau il gagne en force et en hp maximum et regagne tous ses points de
#vie (hp).