from Element import Element
import theGame

class Stairs(Element):
    """ Strairs that goes down one floor. """

    def __init__(self):
        super().__init__("Stairs", 'E')

    def meet(self, hero):
# Nouvelle salle
        theGame.theGame().buildFloor()
        theGame.theGame().addMessage("Le " + hero.name + " vient de trouver une nouvelle salle")
