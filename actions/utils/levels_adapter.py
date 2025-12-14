# actions/utils/adapters.py

"""
Adaptation du contenu selon le niveau utilisateur :
- débutant : vulgarisation, simplification, phrases courtes
- intermédiaire : explications techniques modérées
- expert : approfondissement, détails internes, vocabulaire avancé
"""

import re


def _simplify_text(text: str) -> str:
    """
    Simplifie le texte pour un niveau débutant :
    - phrases plus courtes
    - vocabulaire plus simple
    - suppression des termes trop techniques
    """
    simple = text

    # Termes complexes → termes simples
    replacements = {
        r"\bcontainerisation\b": "utilisation de conteneurs",
        r"\borchestration\b": "organisation automatique",
        r"\binfrastructure\b": "système",
        r"\benvironnement d’exécution\b": "environnement",
        r"\bvirtualisation\b": "machines virtuelles",
        r"\bpipeline\b": "chaîne d'étapes",
        r"\bCI/CD\b": "automatisation du développement",
        r"\bAPI\b": "interface pour communiquer",
    }

    for pattern, replacement in replacements.items():
        simple = re.sub(pattern, replacement, simple, flags=re.IGNORECASE)

    # Phrase courte : on fractionne les phrases trop longues
    sentences = re.split(r"(?<=[.!?])\s+", simple)
    short_sentences = []
    for s in sentences:
        if len(s) > 140:
            # découper en deux si trop long
            mid = len(s) // 2
            short_sentences.append(s[:mid] + ".")
            short_sentences.append(s[mid:].strip())
        else:
            short_sentences.append(s)

    return " ".join(short_sentences)


def _technical_text(text: str) -> str:
    """
    Ajoute un niveau intermédiaire :
    - Explications techniques utiles
    - Structure plus rigoureuse
    - Légère montée en précision
    """
    technical = text

    inserts = [
        "Sur le plan technique, ",
        "D’un point de vue pratique, ",
        "Dans un environnement DevOps standard, ",
    ]

    # On ajoute un préfixe technique à la première phrase
    sentences = re.split(r"(?<=[.!?])\s+", technical)
    if sentences:
        sentences[0] = inserts[0] + sentences[0]

    return " ".join(sentences)


def _expert_text(text: str) -> str:
    """
    Ajoute de la profondeur :
    - concepts internes
    - détails d’optimisation
    - fonctionnement bas niveau
    """
    expert = text

    additions = (
        "\n\nDétails avancés :\n"
        "- Fonctionnement interne optimisé.\n"
        "- Concept aligné avec les meilleures pratiques DevOps.\n"
        "- Intégration possible dans des architectures distribuées.\n"
    )

    return expert + additions


# ----------------------------
# Fonction principale
# ----------------------------

def adapt_content(level: str, content: str) -> str:
    """
    Adapte un contenu brut à un niveau :
    - level : "beginner", "intermediate", "expert"
    - content : texte original
    """
    if level == "beginner":
        return _simplify_text(content)

    elif level == "intermediate":
        return _technical_text(content)

    elif level == "expert":
        return _expert_text(content)

    else:
        # fallback
        return content
