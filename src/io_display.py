"""
Module de lecture des fichiers problèmes et d'affichage formaté des matrices.
Responsable : Lilian
"""

def lire_probleme(chemin_fichier: str) -> tuple[int, int, list[list[int]], list[int], list[int]]:
    """
    Lit un fichier .txt au format du projet SM502.
    Retourne : (n, m, couts, provisions, commandes)
    """
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        lignes = [ligne.strip() for ligne in f if ligne.strip()]

    # TODO: Extraire n et m depuis lignes[0]
    n, m = 0, 0

    couts: list[list[int]] = []
    provisions: list[int] = []

    # TODO: Lire les n lignes suivantes pour remplir couts (m valeurs) et provisions (dernière valeur)

    # TODO: Lire la dernière ligne pour remplir commandes (m valeurs)
    commandes: list[int] = []

    # TODO: Vérifier que len(couts) == n, len(commandes) == m et sum(provisions) == sum(commandes)
    return n, m, couts, provisions, commandes


def afficher_matrice(
    titre: str,
    matrice: list[list[int | float | str]],
    provisions: list[int] | None = None,
    commandes: list[int] | None = None,
    base: set[tuple[int, int]] | None = None,
) -> None:
    """
    Affiche proprement une matrice n x m sans aucun décalage de colonnes.
    Utilisable pour :
      - la matrice des coûts (avec provisions et commandes)
      - la proposition de transport (avec provisions, commandes, et marquage éventuel des cases de base)
      - la table des coûts potentiels (sans provisions ni commandes)
      - la table des coûts marginaux (sans provisions ni commandes)
    """
    print(f"\n=== {titre} ===")
    if not matrice:
        print("(Matrice vide)")
        return

    # TODO: Construire les en-têtes ["", "C1", ..., "Cm"] (+ "Provisions" si provisions is not None)
    # TODO: Formater chaque cellule (ex: si base est fourni et (i, j) in base et valeur == 0, afficher "0*")
    # TODO: Calculer la largeur maximale de chaque colonne pour garantir un alignement parfait (.rjust)
    # TODO: Afficher les lignes de séparation (+---+) et chaque ligne alignée
    pass