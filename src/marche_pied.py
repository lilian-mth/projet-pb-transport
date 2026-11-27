"""
Algorithme du marche-pied avec potentiel : maximisation sur cycle,
gestion des dégénérescences / delta = 0 et boucle de résolution.
Responsable : Yoann (utilise potentiels.py de Lilian et graph_ops.py de Loïc)
"""
from src.io_display import afficher_matrice
from src.init_algos import calculer_cout_total
from src.graph_ops import detecter_cycle_bfs, rendre_connexe
from src.potentiels import calculer_potentiels, calculer_tables_couts, trouver_arete_ameliorante


def maximiser_sur_cycle(
    proposition: list[list[int]],
    base: set[tuple[int, int]],
    cycle: list[tuple[int, int]],
    arete_entree: tuple[int, int] | None = None,
    afficher_trace: bool = True,
) -> int:
    """
    Maximise le transport le long du cycle fourni.
    - Oriente le cycle en alternant + et - (en commençant par + sur arete_entree si fournie)
    - Affiche les conditions pour chacune des cases (si afficher_trace=True)
    - Calcule delta = min des quantités sur les cases marquées -
    - Met à jour proposition et retire de base les arêtes dont la quantité tombe à 0
    - Affiche l'arête (ou les arêtes) supprimée(s)
    Retourne la valeur de delta.
    """
    # TODO: Réordonner cycle pour que cycle[0] == arete_entree si arete_entree est présente
    # TODO: Séparer cases_plus (indices pairs) et cases_moins (indices impairs)
    # TODO: Afficher les conditions (ex: "b[i][j] - delta >= 0") et calculer delta
    # TODO: Mettre à jour proposition[i][j] (+/- delta)
    # TODO: Retirer de base la (ou les) case(s) de cases_moins devenue(s) nulle(s) et afficher
    return 0


def resoudre_marche_pied(
    couts: list[list[int]],
    provisions: list[int],
    commandes: list[int],
    proposition_init: list[list[int]],
    base_init: set[tuple[int, int]],
    afficher_trace: bool = True,
) -> tuple[list[list[int]], int]:
    """
    Boucle complète de la méthode du marche-pied avec potentiel (incluant les améliorations §2.3).
    Retourne : (proposition_optimale, cout_optimal)
    """
    n = len(provisions)
    m = len(commandes)
    proposition = [ligne.copy() for ligne in proposition_init]
    base = set(base_init)
    iteration = 0
    dernieres_aretes_connexite: list[tuple[int, int]] = []
    arete_ameliorante_forcee: tuple[int, int] | None = None

    while True:
        iteration += 1
        if afficher_trace:
            print(f"\n==================== ITÉRATION {iteration} ====================")
            afficher_matrice("Proposition de transport", proposition, provisions, commandes, base)
            print(f"Coût total actuel : {calculer_cout_total(couts, proposition)}")

        # 1. Élimination répétée de tous les cycles éventuels (§2.3 point 1)
        while True:
            cycle = detecter_cycle_bfs(n, m, base, afficher_trace=afficher_trace)
            if cycle is None:
                break
            delta = maximiser_sur_cycle(
                proposition, base, cycle, arete_entree=arete_ameliorante_forcee, afficher_trace=afficher_trace
            )
            # Gestion du cas particulier delta == 0 (§2.3 point 2)
            if delta == 0 and arete_ameliorante_forcee is not None and dernieres_aretes_connexite:
                for edge in dernieres_aretes_connexite:
                    base.discard(edge)
                base.add(arete_ameliorante_forcee)
                dernieres_aretes_connexite = []
                break
            arete_ameliorante_forcee = None

        # 2. Test de connexité et complétion par coûts croissants si non connexe
        dernieres_aretes_connexite = rendre_connexe(n, m, couts, base, afficher_trace=afficher_trace)

        # 3. Calcul et affichage des potentiels (module de Lilian)
        u, v = calculer_potentiels(n, m, couts, base)
        if afficher_trace:
            print(f"Potentiels fournisseurs (u) : {u}")
            print(f"Potentiels clients (v)      : {v}")

        # 4. Tables des coûts potentiels et marginaux (module de Lilian)
        c_pot, c_marg = calculer_tables_couts(couts, u, v)
        if afficher_trace:
            afficher_matrice("Table des coûts potentiels", c_pot)
            afficher_matrice("Table des coûts marginaux", c_marg)

        # 5. Test d'optimalité et ajout de la meilleure arête améliorante
        arete_ameliorante = trouver_arete_ameliorante(c_marg, base)
        if arete_ameliorante is None:
            if afficher_trace:
                print("\n>>> Aucun coût marginal négatif : la proposition est OPTIMALE.")
            break

        if afficher_trace:
            print(f"\n>>> Arête améliorante détectée : (P{arete_ameliorante[0]+1}, C{arete_ameliorante[1]+1}) "
                  f"avec coût marginal {c_marg[arete_ameliorante[0]][arete_ameliorante[1]]}")

        base.add(arete_ameliorante)
        arete_ameliorante_forcee = arete_ameliorante

    cout_optimal = calculer_cout_total(couts, proposition)
    return proposition, cout_optimal