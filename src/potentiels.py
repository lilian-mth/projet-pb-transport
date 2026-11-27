"""
Calcul des potentiels par sommet, des matrices de coûts potentiels et marginaux,
et détection de la meilleure arête améliorante.
Responsable : Lilian
"""
from collections import deque


def calculer_potentiels(
    n: int,
    m: int,
    couts: list[list[int]],
    base: set[tuple[int, int]],
) -> tuple[list[int], list[int]]:
    """
    Calcule les potentiels u (taille n) et v (taille m) sur l'arbre couvrant 'base'.
    Convention : u[i] - v[j] = couts[i][j] pour tout (i, j) in base, avec u[0] = 0.
    """
    u: list[int | None] = [None] * n
    v: list[int | None] = [None] * m
    u[0] = 0

    # TODO: Utiliser une file (deque) pour propager u[i] et v[j] le long des arêtes de base
    #       - Si u[i] est connu et v[j] est None : v[j] = u[i] - couts[i][j]
    #       - Si v[j] est connu et u[i] est None : u[i] = couts[i][j] + v[j]

    return [val if val is not None else 0 for val in u], [val if val is not None else 0 for val in v]


def calculer_tables_couts(
    couts: list[list[int]],
    u: list[int],
    v: list[int],
) -> tuple[list[list[int]], list[list[int]]]:
    """
    Calcule la matrice des coûts potentiels (c_pot[i][j] = u[i] - v[j])
    et la matrice des coûts marginaux (c_marg[i][j] = couts[i][j] - c_pot[i][j]).
    """
    n = len(u)
    m = len(v)
    c_pot = [[u[i] - v[j] for j in range(m)] for i in range(n)]
    c_marg = [[couts[i][j] - c_pot[i][j] for j in range(m)] for i in range(n)]
    return c_pot, c_marg


def trouver_arete_ameliorante(
    c_marg: list[list[int]],
    base: set[tuple[int, int]],
) -> tuple[int, int] | None:
    """
    Cherche la case hors base ayant le coût marginal strictement négatif le plus petit.
    Retourne (i, j) ou None si la proposition est optimale (tous les coûts marginaux >= 0).
    """
    meilleure_arete: tuple[int, int] | None = None
    min_marg = 0

    # TODO: Parcourir c_marg ; si (i, j) not in base et c_marg[i][j] < min_marg, mettre à jour

    return meilleure_arete