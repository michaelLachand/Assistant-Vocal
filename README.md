# 🎤 Assistant Vocal de Recherche de Chansons YouTube

Ce projet est une application Python qui permet de **rechercher vocalement des chansons sur YouTube**. Elle utilise une interface graphique moderne, une synthèse vocale, ainsi qu'une reconnaissance vocale pour rendre l’expérience utilisateur fluide et interactive.

## 🚀 Fonctionnalités

- Interface graphique moderne avec **CustomTkinter**
- Reconnaissance vocale de l’utilisateur avec **speech_recognition**
- Synthèse vocale des réponses avec **pyttsx3**
- Recherche automatique sur YouTube avec **youtube-search**

---

## 🧰 Technologies & Modules utilisés

### 1. `customtkinter`
> Un module basé sur Tkinter pour créer des interfaces graphiques modernes avec un thème sombre ou clair.

🔧 Installation :
```bash
pip install customtkinter
```

### 2. `speech_recognition`
> Permet de transformer la voix en texte en utilisant un micro. Ce module gère différents moteurs de reconnaissance vocale (comme Google Speech API).

🔧 Installation :
```bash
pip install SpeechRecognition
```

### 3. `pyttsx3`
> Permet la synthèse vocale (Text-To-Speech) hors-ligne, pour que l’application puisse "parler" à l’utilisateur.

🔧 Installation :
```bash
pip install pyttsx3
```

### 4. `youtube-search`
> Permet de rechercher des vidéos sur YouTube via un mot-clé, sans avoir besoin de l’API officielle YouTube.

🔧 Installation :
```bash
pip install youtube-search
```

### 5. `pyaudio`
> Requis par `speech_recognition` pour capter l’audio depuis le micro.

🔧 Installation (sous Windows – méthode recommandée) :
1. Télécharge un fichier `.whl` depuis [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
2. Installe-le via pip :
   ```bash
   pip install PyAudio‑0.2.11‑cp311‑cp311‑win_amd64.whl
   ```

---

## ▶️ Lancer l'application

1. Clone le projet :
   ```bash
   git clone https://github.com/ton-utilisateur/assistant-vocal-youtube.git
   cd assistant-vocal-youtube
   ```

2. Crée un environnement virtuel :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # Windows
   source .venv/bin/activate # Linux/macOS
   ```

3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Lance l’application :
   ```bash
   python app.py
   ```

---

## 📦 Exemple d’usage

1. L’utilisateur clique sur un bouton pour parler.
2. Il dit par exemple : _"Recherche la chanson Imagine de John Lennon"_
3. L’assistant répète la requête avec `pyttsx3`
4. L'application affiche les résultats YouTube correspondants

---

## 📄 Fichier `requirements.txt` (exemple)

```txt
customtkinter
SpeechRecognition
pyttsx3
youtube-search
pyaudio
```

---

## ✅ À faire / Améliorations possibles

- Ouvrir automatiquement le lien YouTube dans le navigateur
- Ajouter un lecteur audio intégré
- Gérer plusieurs langues
- Améliorer la précision de la reconnaissance vocale

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des bugs à signaler, n’hésitez pas à ouvrir une issue.

---

## 🧑‍💻 Auteur

Créé par **[Ton Prénom Nom]** – Passionné par l’IA, le Python et les assistants vocaux intelligents.

---

## 📜 Licence

Ce projet est sous licence MIT.
