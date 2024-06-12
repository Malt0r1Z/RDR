from Element import Element


# Nouvelle classe qui hérite de Creature
class Piege(Element):
    def __init__(self):
        super().__init__("Pièges",'.')

    def meet(self, hero):
        from Map import Map
        from theGame import theGame
        hero.hp-=2
        theGame()._floor.rm(theGame()._floor.pos(self))
        theGame().addMessage("Vous venez de tomber sur un piège ")