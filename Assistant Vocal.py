import customtkinter as ctk

#Initialiser l'application

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Assistant Vocal")
app.geometry("500x400")

# Label d'instructions

label = ctk.CTkLabel(app, text="Cliquez sur le bouton pour écouter une commande", font=("Helvetica", 16))
label.pack(pady=30)

# Bouton pour activer la reconnaissance vocale

ecoute_bouton = ctk.CTkButton(app, text="Ecouter", font=("Helvetica", 14), height=50, width=200)
ecoute_bouton.pack(pady=20)

# Bouton pour quitter l'application

quitter_bouton = ctk.CTkButton(app, text="Quitter", font=("Helvetica", 14), height=50, width=200, fg_color="red")
quitter_bouton.pack(pady=20)

app.mainloop()