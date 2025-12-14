# actions/action_provide_example.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionProvideExample(Action):
    def name(self) -> Text:
        return "action_provide_example"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # -------------------------
        # 1. Récupérer les slots
        # -------------------------
        concept = tracker.get_slot("concept")
        level = tracker.get_slot("level") or "debutant"

        # Normalisation du niveau pour correspondre aux templates
        level_map = {"debutant": "beginner", "intermediaire": "intermediate", "expert": "expert"}
        level_key = level_map.get(level.lower(), "beginner")

        concept = concept.lower() if concept else None

        # -------------------------
        # 2. Récupérer l’exemple
        # -------------------------
        examples = None

        if concept and concept in CONCEPTS_DATABASE:
            examples = CONCEPTS_DATABASE[concept].get("examples")

        if not examples:
            dispatcher.utter_message(text="Je n’ai pas encore d’exemple disponible pour ce sujet.")
            return []

        # On prend le premier exemple pour simplifier (on peut randomiser si besoin)
        #example_content = examples[0]

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        adapted_example = [adapt_content(level_key, example_content) for example_content in examples]

        # -------------------------
        # 4. Formater la réponse
        # -------------------------
        template = get_template("example", level_key)
        formated_example = "\n".join([f"{i + 1}. {example}" for i,example in enumerate(adapted_example)])
        message = template.format(topic=concept, content=formated_example)

        # -------------------------
        # 5. Envoyer la réponse
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
