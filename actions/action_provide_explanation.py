# actions/action_provide_explanation.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionProvideExplanation(Action):

    def name(self) -> Text:
        return "action_provide_explanation"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # -------------------------
        # 1. Lire les slots
        # -------------------------
        tool = tracker.get_slot("tool")
        concept = tracker.get_slot("concept")
        level = tracker.get_slot("level") or "beginner"

        tool = tool.lower() if tool else None
        concept = concept.lower() if concept else None

        # -------------------------
        # 2. Récupérer l’explication
        # -------------------------
        explanation = None

        if tool and tool in TOOLS_DATABASE:
            explanation = TOOLS_DATABASE[tool].get("explanation")

        elif concept and concept in CONCEPTS_DATABASE:
            explanation = CONCEPTS_DATABASE[concept].get("explanation")

        if not explanation:
            dispatcher.utter_message(
                text="Je n’ai pas encore d’explication pour ce sujet. Peux-tu préciser ?"
            )
            return []

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        explanation = adapt_content(level, explanation)

        # -------------------------
        # 4. Appliquer template
        # -------------------------
        template =get_template("explanation", level)
        message = template.format(
            topic=tool or concept,
            content=explanation
        )

        # -------------------------
        # 5. Envoyer réponse
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
