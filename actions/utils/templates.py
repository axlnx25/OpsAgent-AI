# actions/utils/templates.py

"""
Templates de réponse pour différents niveaux d'explication :
- débutant : vulgarisation, phrases simples, analogies
- intermédiaire : notions techniques, exemples pratiques
- expert : détails avancés, concepts internes, meilleures pratiques
"""

TEMPLATES = {
    "definition": {
        "beginner": (
            "Voici une explication simple de {topic} :\n"
            "{content}\n\n"
            "Si tu veux, je peux donner un exemple concret."
        ),
        "intermediate": (
            "Définition de {topic} :\n"
            "{content}\n\n"
            "Souhaites-tu aussi une explication technique ou un schéma ?"
        ),
        "expert": (
            "Définition technique de {topic} :\n"
            "{content}\n\n"
            "Je peux fournir une analyse approfondie ou un comparatif si besoin."
        ),
    },

    "explanation": {
        "beginner": (
            "Voici une explication simple de {topic} :\n"
            "{content}\n\n"
            "Je peux aussi te donner une analogie ou un exemple."
        ),
        "intermediate": (
            "Explication de {topic} :\n"
            "{content}\n\n"
            "Veux-tu un exemple d'utilisation ou une démonstration ?"
        ),
        "expert": (
            "Explication avancée de {topic} :\n"
            "{content}\n\n"
            "Je peux entrer dans les détails internes (archi, runtime, optimisation)."
        ),
    },

    "example": {
        "beginner": (
            "Voici un exemple simple concernant {topic} :\n"
            "{content}"
        ),
        "intermediate": (
            "Exemple pratique pour {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Exemple avancé et optimisé pour {topic} :\n"
            "{content}"
        ),
    },

    "analogy": {
        "beginner": (
            "Voici une analogie facile pour comprendre {topic} :\n"
            "{content}"
        ),
        "intermediate": (
            "Voici une analogie utile pour comprendre {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Analogie conceptuelle pour {topic} :\n"
            "{content}"
        ),
    },

    "usage": {
        "beginner": (
            "Voici comment utiliser {topic} de manière simple :\n"
            "{content}"
        ),
        "intermediate": (
            "Utilisation courante de {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Utilisation avancée de {topic} :\n"
            "{content}"
        ),
    },


    "step_by_step": {
        "beginner": (
            "Voici les étapes pour comprendre/utiliser {topic} :\n"
            "{content}"
        ),
        "intermediate": (
            "Étapes structurées pour {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Procédure avancée ou pipeline complet pour {topic} :\n"
            "{content}"
        ),
    },

    "installation": {
        "beginner": (
            "Voici comment installer {tool} facilement :\n"
            "{content}"
        ),
        "intermediate": (
            "Procédure d'installation détaillée pour {tool} :\n"
            "{content}"
        ),
        "expert": (
            "Installation optimisée + bonnes pratiques pour {tool} :\n"
            "{content}"
        ),
    },

    "configuration": {
        "beginner": (
            "Voici comment configurer {tool} simplement :\n"
            "{content}"
        ),
        "intermediate": (
            "Configuration détaillée de {tool} :\n"
            "{content}"
        ),
        "expert": (
            "Configuration avancée et optimisations pour {tool} :\n"
            "{content}"
        ),
    },

    "architecture": {
        "beginner": (
            "Voici une vue simple de l'architecture de {topic} :\n"
            "{content}"
        ),
        "intermediate": (
            "Architecture technique de {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Architecture détaillée et principes internes de {topic} :\n"
            "{content}"
        ),
    },

    "resources": {
        "beginner": (
            "Voici des ressources simples pour apprendre {topic} :\n"
            "{content}"
        ),
        "intermediate": (
            "Ressources recommandées pour approfondir {topic} :\n"
            "{content}"
        ),
        "expert": (
            "Ressources avancées et spécialisées pour {topic} :\n"
            "{content}"
        ),
    },
}

def get_template(category: str, level: str) -> str:
    """
    Récupère un template selon la catégorie et le niveau.

    category : "definition", "explanation", "example", etc.
    level    : "beginner", "intermediate", "expert"
    """
    try:
        return TEMPLATES[category][level]
    except KeyError:
        # Fallback
        return "{content}"
