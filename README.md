# OpsAgent

OpsAgent est un assistant virtuel intelligent spécialisé dans le domaine du DevOps. Basé sur Rasa, il est conçu pour aider les utilisateurs à comprendre des concepts, installer des outils et configurer des environnements, en s'adaptant à leur niveau d'expertise (Débutant, Intermédiaire, Avancé).

## Fonctionnalités

*   **Pédagogie Adaptative** :  L'assistant ajuste ses explications selon votre niveau déclaré.
*   **Documentation Interactive** :
    *   **Définitions** : Explication claire de concepts (Docker, Kubernetes, CI/CD, etc.).
    *   **Analogies** : Utilisation d'images simples pour vulgariser des sujets complexes.
    *   **Exemples Concrets** : Cas d'usage pratiques.
*   **Assistance Technique** :
    *   **Installation** : Guides pas à pas pour installer des outils sur différents OS (Linux, Windows, macOS).
    *   **Configuration** : Aide au paramétrage d'outils.
    *   **Bonnes Pratiques** : Recommandations de standards de l'industrie.
*   **Interface Web Moderne** : Une interface de chat épurée et responsive supportant le mode sombre.

## Technologies

*   **Core AI** : [Rasa](https://rasa.com/) (Open Source Conversational AI).
*   **NLU Config** : Spacy (fr_core_news_md) pour le traitement du langage français.
*   **Frontend** : HTML5, CSS3 (Glassmorphism), Vanilla JavaScript, Socket.IO.
*   **Backend** : Python (Rasa Action Server).

## Installation

### Prérequis

*   Python 3.8, 3.9 ou 3.10
*   Node.js (optionnel, pour des modifications avancées du frontend)

### Installation du projet

1.  **Cloner le dépôt** :
    ```bash
    git clone https://github.com/axlnx25/OpsAgent-AI.git
    cd OpsAgent
    ```

2.  **Créer un environnement virtuel Python** :
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Installer les dépendances** :
    ```bash
    pip install rasa spacy
    python -m spacy download fr_core_news_md
    ```

4.  **Entraîner le modèle** (si nécessaire) :
    ```bash
    rasa train
    ```

## Utilisation

Pour utiliser OpsAgent avec l'interface web, vous devez lancer deux services : le serveur d'actions (pour la logique métier) et le serveur Rasa (pour l'IA et l'API).

### 1. Lancer le serveur d'actions
Dans un terminal (avec l'environnement virtuel activé) :
```bash
rasa run actions
```

### 2. Lancer le serveur Rasa (API activée)
Dans un **autre terminal** (toujours avec l'environnement virtuel activé) :
```bash
rasa run --enable-api --cors "*"
```
*L'option `--cors "*"` est nécessaire pour permettre au frontend de communiquer avec le backend.*

### 3. Ouvrir l'interface Web
Ouvrez simplement le fichier `web_interface/index.html` dans votre navigateur web préféré.

```bash
# Exemple sous Linux
xdg-open web_interface/index.html
```

## Structure du Projet

*   `actions/` : Code Python des actions personnalisées (réponses dynamiques).
*   `data/` : Données d'entraînement NLU et histoires (stories) pour le dialogue.
*   `models/` : Modèles Rasa entraînés (`.tar.gz`).
*   `web_interface/` : Code source du frontend (HTML/CSS/JS).
*   `config.yml` : Configuration du pipeline NLU et des politiques.
*   `credentials.yml` : Configuration des canaux de communication (Socket.IO activé).
*   `domain.yml` : Définition de l'univers du bot (intents, entities, slots, réponses).
*   `endpoints.yml` : Configuration des endpoints (Action Server, Tracker Store).

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour améliorer les capacités d'OpsAgent.
