from Element import Element
from theGame import theGame

# Classe marchand qui hérite de Element, est relié aussi à la classe Magasin, qui place le marchand sur la carte
class Marchand(Element):
# Cet élément est nommé "Marchand" et possède comme abbréviation "M"
    def __init__(self, name="Marchand", abr="M"):
        super().__init__(name, abr)
# Représente les éléments, tirés au sort dans sa boutique        
        self.elem=[theGame().randEquipment() for x in range(3)]

# Méthode permettant de sélectionner au clavier, l'élément que l'on souhaite
    def select(self, elem):
        from utils import getch
        print("Que voulez vous acheter ? : " + str([str(elem.index(e)) + ": " + e.name for e in elem]))
        c = getch()
        if c=='^[':
            return None
        elif c.isdigit() and int(c) in range(len(elem)):
            return elem[int(c)]

# Méthode qui fixe le prix des éléments dans la boutique suivant leur degré de rareté        
    def prix(self,elem):
        from theGame import theGame
        for l in theGame().equipments.items():
            for objet in l[1]:
# On s'assure que l'élément est bien un élément
                if type(elem)==type(objet):
                    return (l[0]+1)*2


# Méthode qui gère la rencontre entre le joueur et le marchand
    def meet(self,creature):
        from Hero import Hero
        from theGame import theGame
# Condition pour s'assurer que le marchand possède encore des éléments à vendre
        if len(self.elem)!=0:
# On s'assure que le héro, uniquement, puisse intéragir avec le marchand
            if isinstance(creature,Hero):
# Affiche les objets proposés par le marchand et leur prix
                print("Les prix sont : "+"  ".join([x.name+": "+str(self.prix(x)) for x in self.elem]))
                elem = theGame().select(self.elem)
                if elem==None:
                    pass
# Cas si le marchand vend de l'or
                elif elem.name=="gold" and creature.gold-self.prix(elem)>=0:
                    creature.gold -= self.prix(elem)
                    creature.gold+=1
                    self.elem.pop(self.elem.index(elem))
# Cas pour les autres marchandises
                elif elem.name!="gold" and creature.gold-self.prix(elem)>=0:
                    creature.gold -= self.prix(elem)
                    creature._inventory.append(elem)
                    self.elem.pop(self.elem.index(elem))
                else:
                    theGame().addMessage("Pas assez de ressources, à bientôt ")
        else:
            theGame().addMessage("Le magasin est vide...")
