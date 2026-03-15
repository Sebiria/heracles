import locale
from datetime import datetime

#region Temporalité
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
date_heure = datetime.now()  # Date et heure
date_du_jour = datetime.now().date()
jour = datetime.now().strftime("%A")  # Jour de la semaine
heure = datetime.now().strftime("%HH%M") # Heure
#endregion

profils = {}


annee_scolaire = "2026-2027"
maj_necessaire = ["Monir", "Nabil", "Hassan"]
nom_site = "Jean Mermoz\nAdrienne Bolland"
jours_travail = {"p1": [datetime(2026, 9, 1), datetime(2026, 10, 16)],
                 "p2": [datetime(2026, 11, 2), datetime(2026, 12, 18)],
                 "p3": [datetime(2027, 1, 4), datetime(2027, 2, 19)],
                 "p4": [datetime(2027, 3, 8), datetime(2027, 4, 16)],
                 "p5": [datetime(2027, 5, 3), datetime(2027, 7, 2)]}




