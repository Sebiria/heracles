from tkinter import *
from PIL import Image, ImageTk
import re
import main


def show(frame_body):

    image_body = ImageTk.PhotoImage(Image.open("img/body.png").resize((700,530)))
    label_body = Label(frame_body,image=image_body,bd=0)
    label_body.image = image_body
    label_body.place(x=0,y=0)

    # Titre de la page paramètres
    Label(
        frame_body,
        text="PARAMÈTRES",
        font=("Arial",32,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=190,y=20)

    # Titre Noms des écoles (20px sous PARAMÈTRES, mieux centré)
    Label(
        frame_body,
        text="Noms des écoles",
        font=("Arial",16,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=250,y=92)

    # Frame pour les paramètres (style comme ajout.py)
    frame_params = Frame(frame_body, bg="#B9934B")
    frame_params.place(x=40,y=125,width=620,height=320)

    # Message de confirmation (en bas du body)
    message_confirmation = Label(
        frame_body,
        text="",
        fg="#7CFC00",
        bg="#B9934B",
        font=("Arial",10,"bold")
    )
    message_confirmation.place(x=240, y=500)

    # Frame pour les champs d'écoles
    frame_ecoles = Frame(frame_params, bg="#B9934B")
    frame_ecoles.pack(pady=(5,0))

    # Variables pour les noms d'écoles
    ecole1_var = StringVar()
    ecole2_var = StringVar()
    ecole3_var = StringVar()

    # -----------------------------
    # Validation nom d'école
    # -----------------------------

    def ecole_valide(nom):
        nom = nom.strip()
        if len(nom) < 3:
            return False
        if not re.match(r"^[A-Za-zÀ-ÿ ]+$", nom):
            return False
        return True

    # -----------------------------
    # Bouton valider - fonction
    # -----------------------------

    def valider_ecoles():
        noms_valides = []
        if ecole_valide(ecole1_var.get()):
            noms_valides.append(ecole1_var.get())
        if ecole_valide(ecole2_var.get()):
            noms_valides.append(ecole2_var.get())
        if ecole_valide(ecole3_var.get()):
            noms_valides.append(ecole3_var.get())
        
        main.nom_site = "\n".join(noms_valides)
        # Vider les champs
        ecole1_var.set("")
        ecole2_var.set("")
        ecole3_var.set("")
        
        # Message de confirmation
        message_confirmation.config(text="✅ Noms des écoles mis à jour ✅", fg="#5306B8")
        frame_ecoles.after(5000, lambda: message_confirmation.config(text=""))

    # -----------------------------
    # Vérification des écoles
    # -----------------------------

    def verifier_ecoles(*args):
        au_moins_un_valide = (
            ecole_valide(ecole1_var.get()) or
            ecole_valide(ecole2_var.get()) or
            ecole_valide(ecole3_var.get())
        )

        if au_moins_un_valide:
            bouton_valider.config(bg="#7CFC00", state="normal")
        else:
            bouton_valider.config(bg="#FF6B6B", state="disabled")

    # Labels au-dessus
    Label(frame_ecoles, text="École 1", font=("Arial",12,"bold"),
          fg="white", bg="#B9934B").grid(row=0, column=0, padx=10)
    Label(frame_ecoles, text="École 2", font=("Arial",12,"bold"),
          fg="white", bg="#B9934B").grid(row=0, column=1, padx=10)
    Label(frame_ecoles, text="École 3", font=("Arial",12,"bold"),
          fg="white", bg="#B9934B").grid(row=0, column=2, padx=10)

    # Champs côte à côte
    ecole1_entry = Entry(frame_ecoles, textvariable=ecole1_var, width=20)
    ecole1_entry.grid(row=1, column=0, padx=10, pady=(5,0))
    ecole1_entry.bind("<KeyRelease>", verifier_ecoles)

    ecole2_entry = Entry(frame_ecoles, textvariable=ecole2_var, width=20)
    ecole2_entry.grid(row=1, column=1, padx=10, pady=(5,0))
    ecole2_entry.bind("<KeyRelease>", verifier_ecoles)

    ecole3_entry = Entry(frame_ecoles, textvariable=ecole3_var, width=20)
    ecole3_entry.grid(row=1, column=2, padx=10, pady=(5,0))
    ecole3_entry.bind("<KeyRelease>", verifier_ecoles)

    # Bouton valider à côté du champ 3
    bouton_valider = Button(frame_ecoles, text="Valider", font=("Arial",12,"bold"),
                           bg="#FF6B6B", fg="white", state="disabled",
                           command=valider_ecoles)
    bouton_valider.grid(row=1, column=3, padx=(10,0), pady=(5,0))

    # Titre Réinitialisation des profils
    Label(
        frame_body,
        text="Réinitialisation des profils",
        font=("Arial",16,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=230,y=270)

    # Frame pour la réinitialisation
    frame_reinit = Frame(frame_params, bg="#B9934B")
    frame_reinit.place(x=0, y=180, width=620, height=100)

    # Variable pour le champ de réinitialisation
    reinit_var = StringVar()

    # Colonne vide pour centrage
    frame_reinit.grid_columnconfigure(0, weight=1)
    frame_reinit.grid_columnconfigure(3, weight=1)

    # Label d'instruction
    Label(
        frame_reinit,
        text="Écrivez REINITIALISER en majuscule",
        font=("Arial",10),
        fg="white",
        bg="#B9934B"
    ).grid(row=0, column=1, padx=5, pady=(10,0))

    # Champ de réinitialisation
    reinit_entry = Entry(frame_reinit, textvariable=reinit_var, width=20, font=("Arial",12))
    reinit_entry.grid(row=1, column=1, padx=5, pady=(5,0))

    # Bouton valider pour réinitialisation
    bouton_reinit = Button(frame_reinit, text="Valider", font=("Arial",12,"bold"),
                          bg="#FF6B6B", fg="white", state="disabled",
                          command=lambda: None)
    bouton_reinit.grid(row=1, column=2, padx=5, pady=(5,0))

    # Validation réinitialisation
    def valider_reinit():
        main.profils.clear()
        reinit_var.set("")
        
        # Message de confirmation
        message_confirmation.config(text="✅ Réinitialisation effectuée ✅", fg="#5306B8")
        frame_reinit.after(5000, lambda: message_confirmation.config(text=""))
        
        verifier_reinit()

    def verifier_reinit(*args):
        if reinit_var.get() == "REINITIALISER":
            bouton_reinit.config(bg="#7CFC00", state="normal", command=valider_reinit)
        else:
            bouton_reinit.config(bg="#FF6B6B", state="disabled", command=lambda: None)

    reinit_entry.bind("<KeyRelease>", verifier_reinit)
