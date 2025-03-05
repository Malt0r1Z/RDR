from Equipment import Equipment

class Weapon(Equipment):
    def __init__(self,name,abr=False,strength=0):
        Equipment.__init__(self,name,abr,False)
        self.strength = strength

    def equip(self, creature):
        """equip a weapon the creature"""
        from theGame import theGame
        if creature.weapon != self:
            theGame().addMessage("le héro équipe un " 
+ self.name+" et gagne "+str(self.strength-creature.weapon.strength)+" de forces")
            creature.strength -= creature.weapon.strength
            creature.strength += self.strength
            creature._inventory.pop(creature._inventory.index(self))
            creature._inventory.append(creature.weapon)
            creature.weapon = self
