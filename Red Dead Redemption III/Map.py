from Coord import Coord
from Hero import Hero
from Room import Room
from Element import Element
from Creature import Creature
import utils
from Marchand import Marchand

import random

class Map(object):
    """A map of a game floor.
        Contains game elements."""

    ground = '.'  # A walkable ground cell
    dir = {'z': Coord(0, -1), 's': Coord(0, 1), 'd': Coord(1, 0), 'q': Coord(-1, 0)}  # four direction user keys
    empty = ' '  # A non walkable cell
    hide = ' '

    def __init__(self, size=20, hero=None):
        self._mat = []
        self._elem = {}
        self._rooms = []
        self._roomsToReach = []
        self.size=size

        for i in range(size):
            self._mat.append([Map.empty] * size)
        if hero is None:
            hero = Hero()
        self._hero = hero
        self.generateRooms(7)
        self.reachAllRooms()
        self.put(self._rooms[0].center(), hero)
        for r in self._rooms[1:]:
            r.decorate(self)
        self.mapdonnee=[["0" for j in range(self.size)] for i in range(self.size)]

    def addRoom(self, room):
        """Adds a room in the map."""
        self._roomsToReach.append(room)
        for y in range(room.c1.y, room.c2.y + 1):
            for x in range(room.c1.x, room.c2.x + 1):
                self._mat[y][x] = Map.ground

    def findRoom(self, coord):
        """If the coord belongs to a room, returns the room elsewhere returns None"""
        for r in self._roomsToReach:
            if coord in r:
                return r
        return None

    def intersectNone(self, room):
        """Tests if the room shall intersect any room already in the map."""
        for r in self._roomsToReach:
            if room.intersect(r):
                return False
        return True

    def dig(self, coord):
        """Puts a ground cell at the given coord.
            If the coord corresponds to a room, considers the room reached."""
        self._mat[coord.y][coord.x] = Map.ground
        r = self.findRoom(coord)
        if r:
            self._roomsToReach.remove(r)
            self._rooms.append(r)

    def corridor(self, cursor, end):
        """Digs a corridors from the coordinates cursor to the end, first vertically, then horizontally."""
        d = end - cursor
        self.dig(cursor)
        while cursor.y != end.y:
            cursor = cursor + Coord(0,utils.sign(d.y))
            self.dig(cursor)
        while cursor.x != end.x:
            cursor = cursor + Coord(utils.sign(d.x), 0)
            self.dig(cursor)

    def reach(self):
        """Makes more rooms reachable.
            Start from one random reached room, and dig a corridor to an unreached room."""
        roomA = random.choice(self._rooms)
        roomB = random.choice(self._roomsToReach)

        self.corridor(roomA.center(), roomB.center())

    def reachAllRooms(self):
        """Makes all rooms reachable.
            Start from the first room, repeats @reach until all rooms are reached."""
        self._rooms.append(self._roomsToReach.pop(0))
        while len(self._roomsToReach) > 0:
            self.reach()

    def randRoom(self):
        """A random room to be put on the map."""
        c1 = Coord(random.randint(0, len(self) - 3), random.randint(0, len(self) - 3))
        c2 = Coord(min(c1.x + random.randint(3, 8), len(self) - 1), min(c1.y + random.randint(3, 8), len(self) - 1))
        return Room(c1, c2)

    def generateRooms(self, n):
        """Generates n random rooms and adds them if non-intersecting."""
        for i in range(n):
            r = self.randRoom()
            if self.intersectNone(r):
                self.addRoom(r)

    def __len__(self):
        return len(self._mat)

    def __contains__(self, item):
        if isinstance(item, Coord):
            return 0 <= item.x < len(self) and 0 <= item.y < len(self)
        return item in self._elem

    def __repr__(self):
        s = ""
        for i in self._mat:
            for j in i:
                s += str(j)
            s += '\n'
        return s

    def checkCoord(self, c):
        """Check if the coordinates c is valid in the map."""
        if not isinstance(c, Coord):
            raise TypeError('Not a Coord')
        if not c in self:
            raise IndexError('Out of map coord')

    def checkElement(self, o):
        """Check if o is an Element."""
        if not isinstance(o, Element):
            raise TypeError('Not a Element')

    def put(self, c, o):
        """Puts an element o on the cell c"""
        self.checkCoord(c)
        self.checkElement(o)
        if self._mat[c.y][c.x] != Map.ground:
            raise ValueError('Incorrect cell')
        if o in self._elem:
            raise KeyError('Already placed')
        self._mat[c.y][c.x] = o
        self._elem[o] = c

    def get(self, c):
        """Returns the object present on the cell c"""
        self.checkCoord(c)
        return self._mat[c.y][c.x]

    def pos(self, o):
        """Returns the coordinates of an element in the map """
        self.checkElement(o)
        return self._elem[o]

    def rm(self, c):
        """Removes the element at the coordinates c"""
        self.checkCoord(c)
        del self._elem[self._mat[c.y][c.x]]
        self._mat[c.y][c.x] = Map.ground

    def move(self, e, way):
        """Moves the element e in the direction way."""
        orig = self.pos(e)
        dest = orig + way
        if dest in self:
            if self.get(dest) == Map.ground:
                self._mat[orig.y][orig.x] = Map.ground
                self._mat[dest.y][dest.x] = e
                self._elem[e] = dest
            elif self.get(dest) != Map.empty and self.get(dest).meet(e) and self.get(dest) != self._hero:
                self.rm(dest)

    def moveAllMonsters(self):
        """Moves all monsters in the map.
            If a monster is at distance lower than 6 from the hero, the monster advances."""
        h = self.pos(self._hero)
        for e in self._elem:
            c = self.pos(e)
            if isinstance(e, Creature) and e != self._hero and c.distance(h) < 6:
                d = c.direction(h)
                if self.get(c + d) in [Map.ground, self._hero]:
                    self.move(e, d)

    # Méthode de classe qui "crée un disque de lumière" autour du joueur pour voir juste autour de lui
    def cachemapv1(self):
# Créer une copie de la matrice
        mapdujoueur=[row.copy() for row in self._mat]

# Parcourir la copie de la matrice et associer le caractère "#"
        for i in range(self.size):
            for j in range(self.size):
                if mapdujoueur[i][j]!=Map.empty and self.pos(self._hero).distance(Coord(j,i))>4:
                    mapdujoueur[i][j] = Map.hide
        s = ""
        for i in mapdujoueur:
            for j in i:
                s += str(j)
            s += '\n'
        return s
    


# Méthode qui permet de cacher la carte et lorsque le joueur passe par un chemin, celui-ci reste découvert jusqu'à la fin du niveau    
    def cachemapv2(self):
# Créer une copie de la matrice
        mapdujoueur=[row.copy() for row in self._mat]
# Parcourir la copie de la matrice et associer le caractère "#"
        for i in range(self.size):
            for j in range(self.size):
                if mapdujoueur[i][j]!=Map.empty and self.pos(self._hero).distance(Coord(j,i))>4 and self.mapdonnee[i][j]=="0":
                    mapdujoueur[i][j] = Map.hide
                else:
                    self.mapdonnee[i][j]="1"
        s = ""
        for i in mapdujoueur:
            for j in i:
                s += str(j)
            s += '\n'
        return s
    


# Méthode qui permet de déplacer intelligemment les monstres sur la carte    
    def deplIntelMonstre(self):
        from algo_djikv1 import PathFinder
# Position du héro
        p_hero = self.pos(self._hero)
        end = (p_hero.y,p_hero.x)
        for e in self._elem:
            if isinstance(e, Creature) and e != self._hero:
                mapgraph=[[0 for j in range(self.size)] for i in range(self.size)]
                for i in range(self.size):
                    for j in range(self.size):
                        if self._mat[i][j]!=Map.ground and self._mat[i][j]!=e:
                            mapgraph[i][j] = 1
                mapgraph[p_hero.y][p_hero.x]=0
                pos_monstre = self.pos(e)
# Position du monstre
                start=(pos_monstre.y,pos_monstre.x)
                path_finder = PathFinder(mapgraph, start, end)
                path = path_finder.find_path()
                if path==None:
                    pass
                else:
                    move_x=path[1][1]-path[0][1]
                    move_y=path[1][0]-path[0][0]
                    self.move(e,Coord(move_x,move_y))
