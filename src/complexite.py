"""
Étude expérimentale de la complexité dans le pire des cas (Section 3 du sujet).
Responsable : Joseph
"""
import random
import time
from src.init_algos import nord_ouest, balas_hammer
from src.marche_pied import resoudre_marche_pied


def generer_probleme_aleatoire(n: int) -> tuple[list[list[int]], list[int], list[int]]:
    """
    Génère un problème carré équilibré de taille n x n selon le protocole §3.3.1 :
      - a[i][j] aléatoire dans [1, 100]
      - temp[i][j] aléatoire dans [1, 100]
      - P[i] = sum_j temp[i][j], C[j] = sum_i temp[i][j]
    """
    couts = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    temp = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

    provisions = [sum(temp[i][j] for j in range(n)) for i in range(n)]
    commandes = [sum(temp[i][j] for i in range(n)) for j in range(n)]

    return couts, provisions, commandes


def mesurer_temps_execution(n: int) -> tuple[float, float, float, float]:
    """
    Mesure le temps CPU (via time.process_time()) pour une instance de taille n :
      - theta_no : temps de nord_ouest
      - theta_bh : temps de balas_hammer
      - t_no     : temps du marche-pied depuis Nord-Ouest
      - t_bh     : temps du marche-pied depuis Balas-Hammer
    """
    couts, provisions, commandes = generer_probleme_aleatoire(n)

    # 1. Nord-Ouest
    t0 = time.process_time()
    prop_no, base_no = nord_ouest(couts, provisions, commandes, afficher_trace=False)
    theta_no = time.process_time() - t0

    # 2. Balas-Hammer
    t0 = time.process_time()
    prop_bh, base_bh = balas_hammer(couts, provisions, commandes, afficher_trace=False)
    theta_bh = time.process_time() - t0

    # 3. Marche-pied depuis NO
    t0 = time.process_time()
    resoudre_marche_pied(couts, provisions, commandes, prop_no, base_no, afficher_trace=False)
    t_no = time.process_time() - t0

    # 4. Marche-pied depuis BH
    t0 = time.process_time()
    resoudre_marche_pied(couts, provisions, commandes, prop_bh, base_bh, afficher_trace=False)
    t_bh = time.process_time() - t0

    return theta_no, theta_bh, t_no, t_bh


def lancer_campagne_mesures(nb_essais: int = 100) -> None:
    """
    Exécute les mesures sur n in [10, 40, 100, 400, 1000, 4000, 10000]
    et sauvegarde les résultats bruts en CSV pour tracer les nuages de points et enveloppes max.
    """
    tailles = [10, 40, 100, 400, 1000, 4000, 10000]

    # TODO: Boucler sur tailles et nb_essais, enregistrer dans un fichier CSV (ex: graphs/mesures.csv)
    # TODO: Tracer avec matplotlib :
    #   - Les 6 nuages de points : theta_NO, theta_BH, t_NO, t_BH, (theta_NO+t_NO), (theta_BH+t_BH)
    #   - Les 6 courbes d'enveloppe supérieure (max sur les 100 essais)
    #   - Le ratio max((t_NO + theta_NO) / (t_BH + theta_BH)) en fonction de n
    pass


if __name__ == "__main__":
    lancer_campagne_mesures(nb_essais=100)