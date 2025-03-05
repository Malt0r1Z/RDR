import math
import heapq

class PathFinder:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.start = start
        self.end = end
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
 
    def heuristic(self, p1, p2):
        # Fonction heuristique (distance euclidienne)
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def find_path(self):
        # Initialiser les ensembles ouverts et fermés
        open_set = []
        closed_set = set()

        # Initialiser le noeud de départ
        start_node = (self.start, 0)
        # Utilisez une file d'attente prioritaire pour stocker les nœuds à visiter, avec le nœud avec le coût le plus bas en premier
        heapq.heappush(open_set, start_node)

        # Gardez une trace du chemin de chaque nœud
        path = {}
        # Gardez une trace du coût pour atteindre chaque nœud
        g_score = {self.start: 0}

        while open_set:
            # Obtenez le nœud avec le coût le plus bas
            current_node, current_cost = heapq.heappop(open_set)

            # Vérifiez si nous avons atteint l'objectif
            if current_node == self.end:
                return self.reconstruct_path(path, current_node)

            # Ajouter le nœud actuel à l'ensemble fermé
            closed_set.add(current_node)

            # Explorer les voisins du nœud actuel
            for neighbor in self.get_neighbors(current_node):
                neighbor_cost = current_cost + 1  # Assume a constant cost of 1 for each step
                if neighbor not in closed_set and neighbor_cost < g_score.get(neighbor, float('inf')):
                    # Mettre à jour le coût pour atteindre le voisin
                    g_score[neighbor] = neighbor_cost
                    # Calculer le coût total pour le voisin (g_score + heuristique)
                    total_cost = neighbor_cost + self.heuristic(neighbor, self.end)
                    # Ajouter le voisin à l'ensemble ouvert
                    heapq.heappush(open_set, (neighbor, total_cost))
                    # Mettre à jour le chemin vers le voisin
                    path[neighbor] = current_node

        # Aucun chemin trouvé
        return None

    def get_neighbors(self, node):
        # Récupère les voisins valides d'un nœud (y compris les diagonales)
        x, y = node
        neighbors = []
        for dx, dy in self.neighbors:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.matrix[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def reconstruct_path(self, path, node):
        # Reconstruire le chemin du nœud de fin au nœud de départ
        path_list = []
        while node in path:
            path_list.append(node)
            node = path[node]
        path_list.append(self.start)
        path_list.reverse()
        return tuple(path_list)