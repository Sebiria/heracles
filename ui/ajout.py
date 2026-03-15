from tkinter import *
from tkinter import ttk
import calendar
import re
from main import annee_scolaire, profils, jours_travail
from datetime import datetime


def show(frame_body):

    frame_form = Frame(frame_body, bg="#B9934B")
    frame_form.place(relx=0.5, rely=0.5, anchor="center")

    for i in range(4):
        frame_form.grid_columnconfigure(i, weight=1)

    nom_var = StringVar()

    annee_var = StringVar()
    mois_var = StringVar()
    jour_var = StringVar()

    lundi_var = StringVar()
    mardi_var = StringVar()
    jeudi_var = StringVar()
    vendredi_var = StringVar()

    # -----------------------------
    # Retirer focus (supprime le bleu)
    # -----------------------------

    def enlever_focus(event=None):
        frame_body.focus_set()

    # -----------------------------
    # Messages d'erreur
    # -----------------------------

    erreur_nom = Label(frame_form, text="", fg="#750000", bg="#B9934B", font=("Arial",8))
    erreur_date = Label(frame_form, text="", fg="#750000", bg="#B9934B", font=("Arial",8))
    erreur_semaine = Label(frame_form, text="", fg="#750000", bg="#B9934B", font=("Arial",8))
    erreur_doublon = Label(frame_form, text="", fg="#750000", bg="#B9934B", font=("Arial",8))

    # -----------------------------
    # Message confirmation
    # -----------------------------

    message_confirmation = Label(
        frame_form,
        text="",
        fg="#7CFC00",
        bg="#B9934B",
        font=("Arial",10,"bold")
    )

    # -----------------------------
    # Validation Nom Prénom
    # -----------------------------

    def nom_valide():

        nom = " ".join(nom_var.get().split())

        if len(nom) < 3:
            return False

        if not re.match(r"^[A-Za-zÀ-ÿ ]+$", nom):
            return False

        return True

    # -----------------------------
    # Vérification formulaire
    # -----------------------------

    def verifier_formulaire(*args):

        valide = True
        erreur_doublon.config(text="")

        nom = " ".join(nom_var.get().split()).upper()

        if not nom_valide():
            erreur_nom.config(text="Nom Prénom invalide")
            valide = False
        else:
            erreur_nom.config(text="")

        if nom in profils:
            erreur_doublon.config(text="Ce profil existe déjà")
            valide = False

        if not (annee_var.get() and mois_var.get() and jour_var.get()):
            erreur_date.config(text="Date incomplète")
            valide = False
        else:
            erreur_date.config(text="")

        if not (lundi_var.get() and mardi_var.get() and jeudi_var.get() and vendredi_var.get()):
            erreur_semaine.config(text="Semaine incomplète")
            valide = False
        else:
            erreur_semaine.config(text="")

        if valide:
            bouton_valider.config(bg="#7CFC00", state="normal")
        else:
            bouton_valider.config(bg="#FF6B6B", state="disabled")

    # -----------------------------
    # Nom prénom
    # -----------------------------

    Label(frame_form, text="Prénom Nom", font=("Arial",16,"bold"),
          fg="white", bg="#B9934B").grid(row=0, column=0, columnspan=4)

    nom_entry = Entry(frame_form, textvariable=nom_var, width=25)
    nom_entry.grid(row=1, column=0, columnspan=4, pady=(0,5))

    erreur_nom.grid(row=2, column=0, columnspan=4)

    nom_var.trace_add("write", verifier_formulaire)

    # -----------------------------
    # Date
    # -----------------------------

    Label(frame_form, text="Premier jour de travail",
          font=("Arial",16,"bold"),
          fg="white", bg="#B9934B").grid(row=3, column=0, columnspan=4, pady=(10,0))

    annee_actuelle = int(annee_scolaire.split("-")[0])

    annees = [
        str(annee_actuelle - 1),
        str(annee_actuelle),
        str(annee_actuelle + 1)
    ]

    annee_menu = ttk.Combobox(frame_form, textvariable=annee_var,
                              values=annees, width=8, state="readonly")
    annee_menu.grid(row=4, column=1)

    mois_liste = [
        "Janvier","Février","Mars","Avril","Mai","Juin",
        "Juillet","Août","Septembre","Octobre","Novembre","Décembre"
    ]

    mois_menu = ttk.Combobox(frame_form, textvariable=mois_var,
                             values=mois_liste, width=10, state="readonly")
    mois_menu.grid(row=4, column=2)

    jour_menu = ttk.Combobox(frame_form, textvariable=jour_var,
                             width=5, state="readonly")
    jour_menu.grid(row=4, column=3)

    erreur_date.grid(row=5, column=0, columnspan=4)

    def update_jours(event=None):

        if annee_var.get() and mois_var.get():

            mois_index = mois_liste.index(mois_var.get()) + 1
            annee = int(annee_var.get())

            nb_jours = calendar.monthrange(annee, mois_index)[1]

            jours = list(range(1, nb_jours + 1))
            jour_menu["values"] = jours

            jour_var.set("")

    annee_menu.bind("<<ComboboxSelected>>", update_jours)
    mois_menu.bind("<<ComboboxSelected>>", update_jours)

    annee_menu.bind("<<ComboboxSelected>>", verifier_formulaire, add="+")
    mois_menu.bind("<<ComboboxSelected>>", verifier_formulaire, add="+")
    jour_menu.bind("<<ComboboxSelected>>", verifier_formulaire)

    annee_menu.bind("<<ComboboxSelected>>", enlever_focus, add="+")
    mois_menu.bind("<<ComboboxSelected>>", enlever_focus, add="+")
    jour_menu.bind("<<ComboboxSelected>>", enlever_focus, add="+")

    # -----------------------------
    # Semaine type
    # -----------------------------

    Label(frame_form, text="Semaine type",
          font=("Arial",16,"bold"),
          fg="white", bg="#B9934B").grid(row=6, column=0, columnspan=4, pady=(10,0))

    types_journee = ["Manuelle","Sportive","Simple","Libre"]

    jours = [
        ("Lundi", lundi_var),
        ("Mardi", mardi_var),
        ("Jeudi", jeudi_var),
        ("Vendredi", vendredi_var)
    ]

    for i, (jour_nom, variable) in enumerate(jours):

        Label(frame_form, text=jour_nom, font=("Arial",11,"bold"),
              fg="white", bg="#B9934B").grid(row=7, column=i)

        menu = ttk.Combobox(frame_form, textvariable=variable,
                            values=types_journee, width=10, state="readonly")

        menu.grid(row=8, column=i)

        menu.bind("<<ComboboxSelected>>", verifier_formulaire)
        menu.bind("<<ComboboxSelected>>", enlever_focus, add="+")

    erreur_semaine.grid(row=9, column=0, columnspan=4)

    erreur_doublon.grid(row=10, column=0, columnspan=4)

    # -----------------------------
    # Validation finale
    # -----------------------------

    def valider():

        nom = " ".join(nom_var.get().split()).upper()

        print("Nom :", nom)
        print("Date :", jour_var.get(), mois_var.get(), annee_var.get())

        print("Lundi :", lundi_var.get().lower())
        print("Mardi :", mardi_var.get().lower())
        print("Jeudi :", jeudi_var.get().lower())
        print("Vendredi :", vendredi_var.get().lower())

        # Intégration du nouveau participant
        numero_mois = {"janvier": "01", "février": "02", "mars": "03",
                           "avril": "04", "mai": "05", "juin": "06",
                           "juillet": "07", "août": "08", "septembre": "09",
                           "octobre": "10", "novembre": "11", "décembre": "12"}
        date_brute = jour_var.get() + numero_mois[mois_var.get().lower()] + annee_var.get()
        if len(date_brute) < 8:
            date_brute = "0" + date_brute
        date = datetime.strptime(date_brute, "%d%m%Y")
        profils[nom] = {"premier_jour": date,
                        "p1": {"lundi": "", "mardi": "", "jeudi": "", "vendredi": ""},
                        "p2": {"lundi": "", "mardi": "", "jeudi": "", "vendredi": ""},
                        "p3": {"lundi": "", "mardi": "", "jeudi": "", "vendredi": ""},
                        "p4": {"lundi": "", "mardi": "", "jeudi": "", "vendredi": ""},
                        "p5": {"lundi": "", "mardi": "", "jeudi": "", "vendredi": ""},
                        "projet": {},
                        "penalite": {}}
        for periode, (debut, fin) in jours_travail.items():
            if debut <= date <= fin:
                profils[nom][periode] = {"lundi": lundi_var.get().lower(),
                                          "mardi": mardi_var.get().lower(),
                                          "jeudi": jeudi_var.get().lower(),
                                          "vendredi": vendredi_var.get().lower()}

        message_confirmation.config(text=f"✅ {nom} a bien été ajouté ✅", fg="#5306B8")

        nom_var.set("")
        annee_var.set("")
        mois_var.set("")
        jour_var.set("")

        lundi_var.set("")
        mardi_var.set("")
        jeudi_var.set("")
        vendredi_var.set("")

        bouton_valider.config(bg="#FF6B6B", state="disabled")

        nom_entry.focus_set()

        frame_form.after(5000, lambda: message_confirmation.config(text=""))

    bouton_valider = Button(
        frame_form,
        text="Valider",
        command=valider,
        bg="#FF6B6B",
        state="disabled"
    )

    bouton_valider.grid(row=11, column=0, columnspan=4, pady=20)

    message_confirmation.grid(row=12, column=0, columnspan=4)