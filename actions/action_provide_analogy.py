# actions/action_provide_analogy.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionProvideAnalogy(Action):
    def name(self) -> Text:
        return "action_provide_analogy"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # -------------------------
        # 1. Lire les slots
        # -------------------------

        concept = tracker.get_slot("concept")
        level = tracker.get_slot("level") or "debutant"

        # Normalize level to match templates
        level_map = {"debutant": "beginner", "intermediaire": "intermediate", "expert": "expert"}
        level_key = level_map.get(level.lower(), "beginner")

        # Normalize names

        concept = concept.lower() if concept else None

        # -------------------------
        # 2. Récupérer l’analogie
        # -------------------------
        analogy = None

        if concept and concept in CONCEPTS_DATABASE:
            analogy = CONCEPTS_DATABASE[concept].get("analogy")

        if not analogy:
            dispatcher.utter_message(
                text="Je n’ai pas encore d’analogie pour ce sujet."
            )
            return []

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        adapted_analogy = adapt_content(level_key, analogy)

        # -------------------------
        # 4. Formater la réponse
        # -------------------------
        template = get_template("analogy", level_key)
        message = template.format(topic=concept, content=adapted_analogy)

        # -------------------------
        # 5. Envoyer la réponse
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
