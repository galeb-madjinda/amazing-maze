import heapq

def solve_maze(maze):
    n = len(maze)
    
    # Définir les déplacements possibles (haut, droite, bas, gauche)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Fonction pour calculer le coût d'un déplacement
    def cost(current, next):
        return 1  # Coût uniforme pour chaque déplacement
    
    # Fonction pour estimer la distance entre deux points (heuristique)
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    # Initialiser les points de départ et d'arrivée
    start = (0, 0)
    goal = (n - 1, n - 1)
    
    # Initialiser la liste des nœuds à explorer (file de priorité)
    open_list = [(0, start)]
    heapq.heapify(open_list)
    
    # Initialiser les coûts de déplacement
    g_costs = {start: 0}
    
    # Initialiser les nœuds parents
    parents = {}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Construire le chemin depuis la fin jusqu'au début
            path = []
            while current in parents:
                path.insert(0, current)
                current = parents[current]
            path.insert(0, start)
            return path
        
        for dx, dy in directions:
            next_node = (current[0] + dx, current[1] + dy)
            if 0 <= next_node[0] < n and 0 <= next_node[1] < n and maze[next_node[0]][next_node[1]] == '.':
                tentative_g_cost = g_costs[current] + cost(current, next_node)
                if next_node not in g_costs or tentative_g_cost < g_costs[next_node]:
                    g_costs[next_node] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(next_node, goal)
                    heapq.heappush(open_list, (f_cost, next_node))
                    parents[next_node] = current
    
    return None  # Aucun chemin trouvé

if __name__ == "__main__":
    try:
        filename = input("Entrez le nom du fichier contenant le labyrinthe : ")
        with open(filename, 'r') as file:
            maze = [list(line.strip()) for line in file.readlines()]
        
        solution = solve_maze(maze)
        if solution:
            for x, y in solution:
                maze[x][y] = 'O'  # Marquer le chemin avec 'O'
            
            # Imprimer le labyrinthe résolu
            for row in maze:
                print(''.join(row))
        else:
            print("Aucun chemin trouvé dans le labyrinthe.")
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'existe pas.")
