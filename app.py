from tkinter import *
from PIL import Image, ImageTk

# import des pages
from ui import accueil, ajout, bonus_malus, profil, stats, parametre

#region Paramétrage fenêtre
fenetre = Tk()
fenetre.title("HÉRACLÈS")
# fenetre.iconbitmap("img/icone_heracles.ico")  # Fichier icône manquant - à ajouter
fenetre.configure(bg="#FFFFFF")

largeur = 700
hauteur = 700

largeur_ecran = fenetre.winfo_screenwidth()
hauteur_ecran = fenetre.winfo_screenheight()

x = (largeur_ecran // 2) - (largeur // 2)
y = (hauteur_ecran // 2) - (hauteur // 2)

fenetre.geometry(f"{largeur}x{hauteur}+{x}+{y}")
fenetre.resizable(False, False)
#endregion


#region Header
logo_gauche = ImageTk.PhotoImage(Image.open("img/logo_vide.png").resize((190,70)))
Label(fenetre,image=logo_gauche,bd=0).place(x=5,y=15)

titre = ImageTk.PhotoImage(Image.open("img/titre.png").resize((300,100)))
Label(fenetre,image=titre,bd=0).place(x=200,y=0)

logo_droite = ImageTk.PhotoImage(Image.open("img/logo_vide.png").resize((190,70)))
Label(fenetre,image=logo_droite,bd=0).place(x=505,y=15)
#endregion


#region Navbar

onglet_actif = "accueil"

frame_nav = Frame(fenetre,bg="#FFFFFF")
frame_nav.place(x=0,y=110,width=700,height=50)

ajout_vide = ImageTk.PhotoImage(Image.open("img/ajout_vide.png").resize((134,50)))
ajout_plein = ImageTk.PhotoImage(Image.open("img/ajout_plein.png").resize((134,50)))

profil_vide = ImageTk.PhotoImage(Image.open("img/profil_vide.png").resize((134,50)))
profil_plein = ImageTk.PhotoImage(Image.open("img/profil_plein.png").resize((134,50)))

accueil_vide = ImageTk.PhotoImage(Image.open("img/accueil_vide.png").resize((134,50)))
accueil_plein = ImageTk.PhotoImage(Image.open("img/accueil_plein.png").resize((134,50)))

bonus_vide = ImageTk.PhotoImage(Image.open("img/bonus_malus_vide.png").resize((134,50)))
bonus_plein = ImageTk.PhotoImage(Image.open("img/bonus_malus_plein.png").resize((134,50)))

stats_vide = ImageTk.PhotoImage(Image.open("img/stats_vide.png").resize((134,50)))
stats_plein = ImageTk.PhotoImage(Image.open("img/stats_plein.png").resize((134,50)))

parametre_img = ImageTk.PhotoImage(Image.open("img/parametre.png").resize((60,60)))

#endregion


#region Body

frame_body = Frame(fenetre,bg="#FFFFFF")
frame_body.place(x=0,y=170,width=700,height=530)

# fond permanent
image_body = ImageTk.PhotoImage(Image.open("img/body.png").resize((700,530)))

label_body = Label(frame_body, image=image_body, bd=0)
label_body.image = image_body
label_body.place(x=0, y=0)

#endregion


#region Fonctions

def nettoyer_body():
    for widget in frame_body.winfo_children():
        if widget != label_body:
            widget.destroy()


def changer_onglet(nouvel_onglet):

    global onglet_actif
    onglet_actif = nouvel_onglet

    label_ajout.config(image=ajout_plein if onglet_actif=="ajout" else ajout_vide)
    label_profil.config(image=profil_plein if onglet_actif=="profil" else profil_vide)
    label_accueil.config(image=accueil_plein if onglet_actif=="accueil" else accueil_vide)
    label_bonus.config(image=bonus_plein if onglet_actif=="bonus" else bonus_vide)
    label_stats.config(image=stats_plein if onglet_actif=="stats" else stats_vide)
    
    # Afficher/masquer le bouton paramètre selon l'onglet actif
    if onglet_actif == "accueil":
        frame_parametre.place(x=5,y=350)
    else:
        frame_parametre.place_forget()

    nettoyer_body()

    if onglet_actif == "accueil":
        accueil.show(frame_body)

    elif onglet_actif == "ajout":
        ajout.show(frame_body)

    elif onglet_actif == "profil":
        profil.show(frame_body)

    elif onglet_actif == "bonus":
        bonus_malus.show(frame_body)

    elif onglet_actif == "stats":
        stats.show(frame_body)

    elif onglet_actif == "parametre":
        parametre.show(frame_body)

#endregion


#region Boutons Navbar

label_ajout = Label(frame_nav,image=ajout_vide,bd=0)
label_ajout.place(x=5,y=0)

label_profil = Label(frame_nav,image=profil_vide,bd=0)
label_profil.place(x=144,y=0)

label_accueil = Label(frame_nav,image=accueil_plein,bd=0)
label_accueil.place(x=283,y=0)

label_bonus = Label(frame_nav,image=bonus_vide,bd=0)
label_bonus.place(x=422,y=0)

label_stats = Label(frame_nav,image=stats_vide,bd=0)
label_stats.place(x=561,y=0)

label_ajout.bind("<Button-1>",lambda e: changer_onglet("ajout"))
label_profil.bind("<Button-1>",lambda e: changer_onglet("profil"))
label_accueil.bind("<Button-1>",lambda e: changer_onglet("accueil"))
label_bonus.bind("<Button-1>",lambda e: changer_onglet("bonus"))
label_stats.bind("<Button-1>",lambda e: changer_onglet("stats"))

# Bouton paramètre (juste au-dessus de "MISE À JOUR NÉCESSAIRE")
frame_parametre = Frame(fenetre, bg="#B9934B", relief="flat", bd=0)
frame_parametre.place(x=5,y=350)

label_parametre = Label(frame_parametre, image=parametre_img, bd=0, bg="#B9934B", highlightthickness=0)
label_parametre.pack(padx=5, pady=5)
label_parametre.bind("<Button-1>",lambda e: changer_onglet("parametre"))

# Rendre le frame cliquable aussi
frame_parametre.bind("<Button-1>",lambda e: changer_onglet("parametre"))

#endregion


# affichage initial
accueil.show(frame_body)

fenetre.mainloop()