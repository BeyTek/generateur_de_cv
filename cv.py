import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF

class CVGenerator:
    def __init__(self, root):
        self.root = root
        root.geometry("600x700")
        self.root.title("Générateur de CV")

        self.prenom_var = tk.StringVar()
        self.nom_var = tk.StringVar()
        self.adresse_var = tk.StringVar()
        self.ville_var = tk.StringVar()
        self.telephone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.permis_b_var = tk.BooleanVar()
        self.experiences = []
        self.formations = []

        frame_nom_prenom = tk.Frame(root)
        frame_nom_prenom.pack()

        tk.Label(frame_nom_prenom, text="Nom:").grid(row=0, column=0)
        self.nom_entry = tk.Entry(frame_nom_prenom, textvariable=self.nom_var)
        self.nom_entry.grid(row=0, column=1)

        tk.Label(frame_nom_prenom, text="Prénom:").grid(row=1, column=0)
        self.prenom_entry = tk.Entry(frame_nom_prenom, textvariable=self.prenom_var)
        self.prenom_entry.grid(row=1, column=1)

        frame_adresse_ville = tk.Frame(root)
        frame_adresse_ville.pack()

        tk.Label(frame_adresse_ville, text="Adresse:").grid(row=0, column=0)
        self.adresse_entry = tk.Entry(frame_adresse_ville, textvariable=self.adresse_var)
        self.adresse_entry.grid(row=0, column=1)

        tk.Label(frame_adresse_ville, text="Ville:").grid(row=1, column=0)
        self.ville_entry = tk.Entry(frame_adresse_ville, textvariable=self.ville_var)
        self.ville_entry.grid(row=1, column=1)

        frame_telephone_email = tk.Frame(root)
        frame_telephone_email.pack()

        tk.Label(frame_telephone_email, text="Téléphone:").grid(row=0, column=0)
        self.telephone_entry = tk.Entry(frame_telephone_email, textvariable=self.telephone_var)
        self.telephone_entry.grid(row=0, column=1)

        tk.Label(frame_telephone_email, text="Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(frame_telephone_email, textvariable=self.email_var)
        self.email_entry.grid(row=1, column=1)
        tk.Checkbutton(root, text="Permis B", variable=self.permis_b_var).pack()

        tk.Label(root, text="Expériences Professionnelles:").pack()
        tk.Button(root, text="Ajouter une expérience", command=self.ajouter_experience).pack()

        tk.Label(root, text="Formation:").pack()
        tk.Button(root, text="Ajouter une formation", command=self.ajouter_formation).pack()

        tk.Button(root, text="Générer CV", command=self.generer_cv).pack()

    def ajouter_experience(self):
        experience_window = tk.Toplevel(self.root)
        experience_window.title("Nouvelle Expérience Professionnelle")

        tk.Label(experience_window, text="Expérience:").pack()
        experience_text = tk.Text(experience_window, height=5, width=60)
        experience_text.pack()

        tk.Label(experience_window, text="Date de début:").pack()
        date_debut_entry = tk.Entry(experience_window)
        date_debut_entry.pack()

        tk.Label(experience_window, text="Date de fin:").pack()
        date_fin_entry = tk.Entry(experience_window)
        date_fin_entry.pack()

        def ajouter_experience_a_liste():
            self.experiences.append({
                "Expérience": experience_text.get("1.0", "end-1c"),
                "Date de début": date_debut_entry.get(),
                "Date de fin": date_fin_entry.get()
            })
            experience_window.destroy()

        tk.Button(experience_window, text="Ajouter", command=ajouter_experience_a_liste).pack()

    def ajouter_formation(self):
        formation_window = tk.Toplevel(self.root)
        formation_window.title("Nouvelle Formation")

        tk.Label(formation_window, text="Formation:").pack()
        formation_text = tk.Text(formation_window, height=5, width=60)
        formation_text.pack()

        tk.Label(formation_window, text="Date de début:").pack()
        date_debut_formation_entry = tk.Entry(formation_window)
        date_debut_formation_entry.pack()

        tk.Label(formation_window, text="Date de fin:").pack()
        date_fin_formation_entry = tk.Entry(formation_window)
        date_fin_formation_entry.pack()

        def ajouter_formation_a_liste():
            self.formations.append({
                "Formation": formation_text.get("1.0", "end-1c"),
                "Date de début": date_debut_formation_entry.get(),
                "Date de fin": date_fin_formation_entry.get()
            })
            formation_window.destroy()

        tk.Button(formation_window, text="Ajouter", command=ajouter_formation_a_liste).pack()

    def generer_cv(self):
        prenom = self.prenom_var.get()
        nom = self.nom_var.get()
        adresse = self.adresse_var.get()
        ville = self.ville_var.get()
        telephone = self.telephone_var.get()
        email = self.email_var.get()
        permis_b = self.permis_b_var.get()
        pdf = FPDF()
        pdf.add_page()

        barre_laterale_largeur = 80
        hauteur_page = pdf.h

        pdf.set_fill_color(200, 200, 200)
        pdf.rect(0, 0, barre_laterale_largeur, hauteur_page, 'F')

        pdf.set_font("Arial", size=12)

        pdf.text(10, 10, f"{prenom} {nom}")
        pdf.text(10, 20, f"Adresse: {adresse}")
        pdf.text(10, 30, f"Ville: {ville}")
        pdf.text(10, 40, f"Téléphone: {telephone}")
        pdf.text(10, 50, f"Email: {email}")
        if permis_b:
            pdf.text(10, 60, "Permis de conduire: B")
        pdf.set_font("Arial", size=14)
        pdf.set_x(barre_laterale_largeur + 10)
        pdf.cell(0, 10, "Expériences Professionnelles:", ln=True)
        pdf.set_font("Arial", size=12)
        for experience in self.experiences:
            pdf.set_x(barre_laterale_largeur + 15)
            pdf.multi_cell(0, 10, experience["Expérience"])
            pdf.set_x(barre_laterale_largeur + 15)
            pdf.cell(0, 10, f"Début: {experience['Date de début']} - Fin: {experience['Date de fin']}", ln=True)
            pdf.ln()
            pdf.set_font("Arial", size=12)
        if self.formations:
            pdf.ln()
            pdf.set_fill_color(0, 0, 0)
            pdf.rect(barre_laterale_largeur + 2, pdf.get_y(), pdf.w - barre_laterale_largeur - 8, 3, 'F')
            pdf.ln()
            pdf.set_font("Arial", size=14)
            pdf.set_x(barre_laterale_largeur + 10)
            pdf.cell(0, 10, "Formations:", ln=True)
            pdf.set_font("Arial", size=12)
        
            for formation in self.formations:
                pdf.set_x(barre_laterale_largeur + 15)
                pdf.multi_cell(0, 10, formation["Formation"])
                pdf.set_x(barre_laterale_largeur + 15)
                pdf.cell(0, 10, f"Début: {formation['Date de début']} - Fin: {formation['Date de fin']}", ln=True)
                pdf.ln()
                pdf.set_font("Arial", size=12)

   
        
        nom_du_fichier = f'{nom}_{prenom}_cv.pdf'

        pdf.output(nom_du_fichier)

        messagebox.showinfo("CV Généré", f"Le CV a été généré avec succès dans le fichier {nom_du_fichier}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CVGenerator(root)
    root.mainloop()


