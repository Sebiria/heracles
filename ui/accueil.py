from tkinter import *
from PIL import Image, ImageTk
import time
from main import annee_scolaire, maj_necessaire, nom_site


def show(frame_body):

    image_body = ImageTk.PhotoImage(Image.open("img/body.png").resize((700,530)))
    label_body = Label(frame_body,image=image_body,bd=0)
    label_body.image = image_body
    label_body.place(x=0,y=0)

    # Année scolaire
    Label(
        frame_body,
        text="Année scolaire",
        font=("Arial",12,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=40,y=30)

    Label(
        frame_body,
        text=annee_scolaire,
        font=("Arial",12,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=55,y=55)

    # Heure dynamique
    label_heure = Label(
        frame_body,
        font=("Arial",20,"bold"),
        fg="white",
        bg="#B9934B"
    )
    label_heure.place(x=565,y=30)

    def update_clock():
        heure_actuelle = time.strftime("%HH%M")
        label_heure.config(text=heure_actuelle)
        label_heure.after(1000, update_clock)

    update_clock()

    # Nom du site (gros titre)
    Label(
        frame_body,
        text=nom_site,
        font=("Arial",32,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=170,y=40)

    # Titre mise à jour
    Label(
        frame_body,
        text="MISE À JOUR NÉCESSAIRE",
        font=("Arial",14,"bold"),
        fg="white",
        bg="#B9934B"
    ).place(x=230,y=210)

    # Cadre blanc
    cadre = ImageTk.PhotoImage(Image.open("img/cadre_blanc.png").resize((660,280)))
    label_cadre = Label(frame_body,image=cadre,bd=0)
    label_cadre.image = cadre
    label_cadre.place(x=20,y=240)

    # Grille
    frame_grille = Frame(frame_body,bg="#FFFFFF")
    frame_grille.place(x=80,y=285,width=540,height=200)

    lignes = 5
    colonnes = 3

    index = 0

    for i in range(lignes):
        for j in range(colonnes):

            texte = ""

            if index < len(maj_necessaire):
                texte = maj_necessaire[index]

            cellule = Label(
                frame_grille,
                text=texte,
                font=("Arial",11,"bold"),
                bg="#FFFFFF",
                width=16
            )

            cellule.grid(row=i,column=j,padx=10,pady=6)

            index += 1