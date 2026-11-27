"""
Point d'entrée interactif et script de génération automatique des 48 traces d'exécution.
Responsable : Joseph
"""
import contextlib
import os
from src.io_display import lire_probleme, afficher_matrice
from src.init_algos import nord_ouest, balas_hammer, calculer_cout_total
from src.marche_pied import resoudre_marche_pied


def executer_un_probleme(num_prob: int, algo_init: str, afficher_trace: bool = True) -> None:
    """Exécute la résolution complète d'un problème donné avec 'no' ou 'bh'."""
    chemin = os.path.join("data", "problemes", f"prob{num_prob}.txt")
    n, m, couts, provisions, commandes = lire_probleme(chemin)

    afficher_matrice(f"Matrice des coûts — Problème {num_prob}", couts, provisions, commandes)

    if algo_init.lower() == "no":
        print("\n--- Initialisation : Algorithme Nord-Ouest ---")
        prop_init, base_init = nord_ouest(couts, provisions, commandes, afficher_trace=afficher_trace)
    elif algo_init.lower() == "bh":
        print("\n--- Initialisation : Algorithme Balas-Hammer ---")
        prop_init, base_init = balas_hammer(couts, provisions, commandes, afficher_trace=afficher_trace)
    else:
        raise ValueError("Algorithme inconnu. Choisir 'no' ou 'bh'.")

    afficher_matrice("Proposition initiale", prop_init, provisions, commandes, base_init)
    print(f"Coût de la proposition initiale : {calculer_cout_total(couts, prop_init)}")

    prop_opt, cout_opt = resoudre_marche_pied(
        couts, provisions, commandes, prop_init, base_init, afficher_trace=afficher_trace
    )

    afficher_matrice("PROPOSITION DE TRANSPORT OPTIMALE", prop_opt, provisions, commandes)
    print(f"COÛT TOTAL OPTIMAL : {cout_opt}\n")


def generer_toutes_les_traces(groupe: str, equipe: str) -> None:
    """Génère les 48 fichiers de traces au format G-E-traceX-no.txt et G-E-traceX-bh.txt."""
    os.makedirs("traces", exist_ok=True)
    for num in range(1, 25):
        for algo in ("no", "bh"):
            nom_fichier = f"{groupe}-{equipe}-trace{num}-{algo}.txt"
            chemin_sortie = os.path.join("traces", nom_fichier)
            with open(chemin_sortie, "w", encoding="utf-8") as f:
                with contextlib.redirect_stdout(f):
                    executer_un_probleme(num, algo, afficher_trace=True)
            print(f"Généré : {chemin_sortie}")


def menu_interactif() -> None:
    """Boucle principale conforme au pseudo-code de la section 2.2 du sujet."""
    while True:
        choix = input("\nNuméro du problème à tester (1-24), 'all' pour les 48 traces, ou 'q' pour quitter : ").strip().lower()
        if choix == "q":
            break
        if choix == "all":
            g = input("Numéro de groupe NEW (ex: 2) : ").strip()
            e = input("Numéro d'équipe (ex: 4) : ").strip()
            generer_toutes_les_traces(g, e)
            continue

        # TODO: Valider l'entier num_prob dans [1, 24], demander 'no' ou 'bh', et appeler executer_un_probleme


if __name__ == "__main__":
    menu_interactif()