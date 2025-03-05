from Element import Element
import theGame

class Equipment(Element):
    """A piece of equipment"""

    def __init__(self, name, abbrv="", usage=None):
        Element.__init__(self, name, abbrv)
        self.usage = usage

    def meet(self, hero):
        """Makes the hero meet an element. The hero takes the element."""
        hero.take(self)
        theGame.theGame().addMessage("Vous ramassez un(e) " + self.name)
        return True

    def use(self, creature):
        from theGame import theGame
        """Uses the piece of equipment. Has effect on the hero according usage.
            Return True if the object is consumed."""
        if self.usage is None:
            theGame().addMessage("Le " + self.name + " n'est pas utilisable")
            return False
        else:
            theGame().addMessage("Le " + creature.name + " utilise le " + self.name)
            return self.usage(self, creature)
