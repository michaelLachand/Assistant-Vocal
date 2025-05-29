import customtkinter as ctk
import speech_recognition as sr
import pyttsx3
from youtube_search import YoutubeSearch
import webbrowser

# Initialiser la reconnaissance vocale et la synthèse vocale

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Fonction pour parler (synthèse vocale)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fonction pour écouter et reconnaître la voix

def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Parlez maintenant")

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language='fr_FR')
            print(f"Vous avez dit: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Je n'ai pas compris")
            return ""
        except sr.RequestError:
            speak("Erreur de connexion")
            return ""

# Fonction pour éxecuter des commandes vocales

def execute_command():
    command = recognize_speech()

    if "joue" in command:
        song_name = command.replace("joue", "").strip()
        speak(f"Recherche de {song_name} sur Youtube.")

        # Recherche Youtube
        results = YoutubeSearch(song_name, max_results=1).to_dict()
        if results:
            video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"
            speak(f"Lecture de {results[0]['title']} sur YouTube.")
            webbrowser.open(video_url)

        else:
            speak("Aucune vidéo trouvée.")

    elif "ouvre Youtube" in command:
        speak("Ouverture de YouTube.")
        webbrowser.open("https://www.youtube.com/")

    elif "ferme" in command:
        speak("Fermeture de l'application")
        app.quit()

    else:
        speak("Commande non reconnue")

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

ecoute_bouton = ctk.CTkButton(app, text="Ecouter", command=execute_command, font=("Helvetica", 14), height=50, width=200)
ecoute_bouton.pack(pady=20)

# Bouton pour quitter l'application

quitter_bouton = ctk.CTkButton(app, text="Quitter", command=app.quit(), font=("Helvetica", 14), height=50, width=200, fg_color="red")
quitter_bouton.pack(pady=20)

app.mainloop()