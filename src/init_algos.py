"""
Algorithmes de proposition initiale (Nord-Ouest, Balas-Hammer) et calcul du coût total.
Responsable : Louis
"""

def calculer_cout_total(couts: list[list[int]], proposition: list[list[int]]) -> int:
    """Calcule sum(a_ij * b_ij)."""
    # TODO: Implémenter le calcul du coût total
    return 0


def nord_ouest(
    couts: list[list[int]],
    provisions: list[int],
    commandes: list[int],
    afficher_trace: bool = True,
) -> tuple[list[list[int]], set[tuple[int, int]]]:
    """
    Algorithme du coin Nord-Ouest (À livrer en priorité J+1).
    Retourne : (proposition, base) où base est l'ensemble des couples (i, j) retenus.
    """
    n = len(provisions)
    m = len(commandes)
    proposition = [[0] * m for _ in range(n)]
    base: set[tuple[int, int]] = set()

    p_rest = provisions.copy()
    c_rest = commandes.copy()
    i, j = 0, 0

    # TODO: Tant que i < n et j < m :
    #   - quantité = min(p_rest[i], c_rest[j])
    #   - affecter proposition[i][j] = quantité et ajouter (i, j) à base
    #   - décrémenter p_rest[i] et c_rest[j]
    #   - avancer i ou j (en cas d'égalité p_rest[i] == c_rest[j] avant la fin, avancer d'un seul pas)

    return proposition, base


def _calculer_penalites(
    couts: list[list[int]],
    lignes_actives: set[int],
    colonnes_actives: set[int],
) -> tuple[dict[int, int | float], dict[int, int | float]]:
    """Calcule la pénalité (écart des 2 plus petits coûts) pour chaque ligne et colonne active."""
    pen_lignes: dict[int, int | float] = {}
    pen_colonnes: dict[int, int | float] = {}

    # TODO: Calculer pen_lignes[i] pour i in lignes_actives
    # TODO: Calculer pen_colonnes[j] pour j in colonnes_actives

    return pen_lignes, pen_colonnes


def balas_hammer(
    couts: list[list[int]],
    provisions: list[int],
    commandes: list[int],
    afficher_trace: bool = True,
) -> tuple[list[list[int]], set[tuple[int, int]]]:
    """
    Algorithme de Balas-Hammer (méthode des pénalités).
    Si afficher_trace=True, affiche à chaque étape :
      - les pénalités des lignes et colonnes
      - la/les ligne(s) ou colonne(s) de pénalité maximale
      - l'arête (i, j) choisie et la quantité affectée
    """
    n = len(provisions)
    m = len(commandes)
    proposition = [[0] * m for _ in range(n)]
    base: set[tuple[int, int]] = set()

    p_rest = provisions.copy()
    c_rest = commandes.copy()
    lignes_actives = set(range(n))
    colonnes_actives = set(range(m))

    # TODO: Boucler tant que lignes_actives et colonnes_actives sont non vides

    return proposition, base