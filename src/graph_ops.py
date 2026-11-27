"""
Opérations sur le graphe biparti associé à une proposition de transport (BFS cycle & connexité).
Convention des sommets :
  - Fournisseurs P_0 .. P_{n-1} -> sommets 0 .. n-1
  - Clients C_0 .. C_{m-1}      -> sommets n .. n+m-1
Responsable : Loïc
"""
from collections import deque


def construire_adjacence(n: int, m: int, base: set[tuple[int, int]]) -> dict[int, list[int]]:
    """Construit la liste d'adjacence du graphe biparti non orienté à partir des arêtes de base."""
    adj: dict[int, list[int]] = {u: [] for u in range(n + m)}
    for i, j in base:
        u, v = i, n + j
        adj[u].append(v)
        adj[v].append(u)
    return adj


def detecter_cycle_bfs(
    n: int,
    m: int,
    base: set[tuple[int, int]],
    afficher_trace: bool = True,
) -> list[tuple[int, int]] | None:
    """
    Détecte l'existence d'un cycle par parcours en largeur (BFS).
    Si un voisin v est déjà visité et v != parent[u], reconstruit et affiche le cycle.
    Retourne : la liste ordonnée des arêtes [(i1, j1), (i2, j2), ...] du cycle, ou None si acyclique.
    """
    adj = construire_adjacence(n, m, base)
    visites: set[int] = set()
    parent: dict[int, int | None] = {}

    # TODO: Lancer un BFS depuis chaque sommet non visité :
    #   - Si un voisin v est déjà dans visites et v != parent[u] :
    #       * Remonter les parents de u et v jusqu'à leur ancêtre commun
    #       * Convertir les paires de sommets consécutifs en coordonnées (i, j)
    #       * Afficher le cycle si afficher_trace=True
    #       * Retourner la liste ordonnée des cases (i, j) du cycle

    return None


def trouver_composantes_connexes_bfs(
    n: int,
    m: int,
    base: set[tuple[int, int]],
) -> list[set[int]]:
    """Retourne la liste des composantes connexes du graphe biparti via BFS."""
    adj = construire_adjacence(n, m, base)
    visites: set[int] = set()
    composantes: list[set[int]] = []

    # TODO: Pour chaque sommet s de 0 à n + m - 1, collecter sa composante via BFS

    return composantes


def rendre_connexe(
    n: int,
    m: int,
    couts: list[list[int]],
    base: set[tuple[int, int]],
    afficher_trace: bool = True,
) -> list[tuple[int, int]]:
    """
    Teste la connexité par BFS. Si non connexe :
      - Affiche les sous-graphes connexes (si afficher_trace=True)
      - Trie les arêtes hors base par coûts croissants
      - Ajoute les arêtes reliant deux composantes distinctes jusqu'à obtenir 1 seule composante
    Retourne la liste des arêtes ajoutées (nécessaire pour le retour arrière si delta == 0).
    """
    composantes = trouver_composantes_connexes_bfs(n, m, base)
    arretes_ajoutees: list[tuple[int, int]] = []

    if len(composantes) <= 1:
        return arretes_ajoutees

    # TODO: Afficher les sous-graphes connexes
    # TODO: Trier toutes les arêtes (i, j) hors base par couts[i][j] croissant
    # TODO: Ajouter les arêtes reliant deux composantes distinctes et fusionner les composantes

    return arretes_ajoutees