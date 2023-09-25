import random

def generate_maze(n):
    # Créer une grille n x n remplie de murs
    maze = [['#' for _ in range(n)] for _ in range(n)]
    
    # Fonction récursive pour générer le labyrinthe
    def recursive_backtracking(x, y):
        # Liste des directions possibles (haut, droite, bas, gauche)
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Vérifier si la nouvelle cellule est valide
            if 0 <= nx < n and 0 <= ny < n and maze[ny][nx] == '#':
                # Casser le mur entre la cellule actuelle et la nouvelle cellule
                maze[y + dy // 2][x + dx // 2] = '.'
                maze[ny][nx] = '.'
                recursive_backtracking(nx, ny)
    
    # Appeler la fonction récursive à partir du coin supérieur gauche
    recursive_backtracking(0, 0)
    
    # Définir l'entrée et la sortie
    maze[0][0] = '.'
    maze[n - 1][n - 1] = '.'
    
    return maze

def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    try:
        n = int(input("Entrez la taille du labyrinthe (un nombre entier naturel) : "))
        filename = input("Entrez le nom du fichier de sortie : ")
        
        maze = generate_maze(n)
        save_maze_to_file(maze, filename)
        
        print(f"Le labyrinthe a été enregistré dans le fichier '{filename}'.")
    except ValueError:
        print("Veuillez entrer un nombre entier naturel valide.")


def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    try:
        n = int(input("Entrez la taille du labyrinthe (un nombre entier naturel) : "))
        filename = input("Entrez le nom du fichier de sortie : ")
        
        maze = generate_maze(n)
        save_maze_to_file(maze, filename)
        
        print(f"Le labyrinthe a été enregistré dans le fichier '{filename}'.")
    except ValueError:
        print("Veuillez entrer un nombre entier naturel valide.")
