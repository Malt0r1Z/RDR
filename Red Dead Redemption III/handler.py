import theGame

def heal(creature):
    """Heal the creature"""
    creature.hp += 3
    creature._poison=False
    return True

def teleport(creature, unique):
    from theGame import theGame
    from Map import Map
    """Teleport the creature"""
    map=theGame()._floor
    carte=map._rooms[-1]
    boucle=True
    while boucle:
        new_coord = carte.randCoord()
# r.randEmptyCoord(map) 
        if map.get(new_coord)==Map.ground:
            theGame()._floor.rm(theGame()._floor.pos(creature))
            theGame()._floor.put(new_coord, creature)
            theGame().addMessage("Vous vous êtes téléportés")
            boucle=False
    return unique

def throw(power, loss):
    """Throw an object"""
    pass

def heal_boost(creature):
# Heal le héro avec une super potion
    creature.hp+=20
    return True


def armure_paille(creature):
    creature.armure=1
    return True

def armure_cb(creature):
    creature.armure=2
    return True

def armure_plomb(creature):
    creature.armure=3
    return True

def armure_diamant(creature):
    creature.armure=4
    return True