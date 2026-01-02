# actions/action_provide_step_by_step.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionProvideStepByStep(Action):
    def name(self) -> Text:
        return "action_provide_step_by_step"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # -------------------------
        # 1. Lire les slots
        # -------------------------
        tool = tracker.get_slot("tool")
        concept = tracker.get_slot("concept")
        level = tracker.get_slot("level") or "debutant"

        # Normalize level to match templates: débutant/intermediaire/expert
        level_map = {"debutant": "beginner", "intermediaire": "intermediate", "expert": "expert"}
        level_key = level_map.get(level.lower(), "beginner")

        # Normalize names
        tool = tool.lower() if tool else None
        concept = concept.lower() if concept else None

        # -------------------------
        # 2. Récupérer le pas-à-pas
        # -------------------------
        steps = None

        if tool and tool in TOOLS_DATABASE:
            steps = TOOLS_DATABASE[tool].get("step_by_step")
        elif concept and concept in CONCEPTS_DATABASE:
            steps = CONCEPTS_DATABASE[concept].get("step_by_step")

        if not steps:
            dispatcher.utter_message(
                text="Je n’ai pas encore de guide étape par étape pour ce sujet."
            )
            return []

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        # Chaque étape peut être simplifiée ou enrichie
        adapted_steps = [adapt_content(level_key, step) for step in steps]

        # -------------------------
        # 4. Formater la réponse
        # -------------------------
        template = get_template("step_by_step", level_key)
        formatted_steps = "\n".join([f"{i+1}. {step}" for i, step in enumerate(adapted_steps)])
        message = template.format(topic=task or tool or concept, content=formatted_steps)

        # -------------------------
        # 5. Envoyer la réponse
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
