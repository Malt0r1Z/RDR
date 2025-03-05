from Element import Element
import heapq
import theGame

class Creature(Element):
    """A creature that occupies the dungeon.
        Is an Element. Has hit points and strength."""

    def __init__(self, name, hp, abbrv="", strength=1,poison=False):
        Element.__init__(self, name, abbrv)
        self.hp = hp
        self.strength = strength
        self._poison = poison
        self.armure=None

    def description(self):
        """Description of the creature"""
        return Element.description(self) + "(" + str(self.hp) + ")"


    def meet(self, other):
        from Hero import Hero
        """The creature is encountered by an other creature.
            The other one hits the creature. Return True if the creature is dead."""
        if self.armure==1:
            if other.strength>=5:
                self.hp -=5
            else:
                self.hp -= other.strength
        elif self.armure==2:
            if other.strength>=4:
                self.hp -=4
            else:
                self.hp -= other.strength
        elif self.armure==3:
            if other.strength>=3:
                self.hp -=3
            else:
                self.hp -= other.strength
        elif self.armure==4:
            if other.strength>=2:
                self.hp -=2
            else:
                self.hp -= other.strength
        else:
            self.hp -= other.strength
        if other.name=="Voleur":
            other.abbrv="V"
            if self.gold>0:
                self.gold-=1
        if self._poison==True:
                other._poison=True
                theGame.theGame().addMessage("Le " + other.name + " vient d'être empoisonné par le " +self.description())
        theGame.theGame().addMessage("Le " + other.name + " tape le " + self.description())
        if self.hp<=0:
#gère les xp du héro, niveau et l'augmentation du niveau etc...
            if isinstance(other, Hero):
                a=other.level
                other.xp+=self.strength
                other.level+=other.xp//10
                other.xp=other.xp%10
                if a<other.level:
                    other.strength+=1
                    other.hpmax+=1
                    other.hp=other.hpmax
        if self.hp > 0:
            return False
        return True
