# actions/action_provide_definition.py OK

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionProvideDefinition(Action):

    def name(self) -> Text:
        return "action_provide_definition"

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
        level = tracker.get_slot("level") or "debutant"

        # Nettoyage minimal
        tool = tool.lower() if tool else None
        concept = concept.lower() if concept else None

        # -------------------------
        # 2. Choisir la source (TOOL ou CONCEPT)
        # -------------------------
        definition = None

        if tool and tool in TOOLS_DATABASE:
            definition = TOOLS_DATABASE[tool].get("definition")

        elif concept and concept in CONCEPTS_DATABASE:
            definition = CONCEPTS_DATABASE[concept].get("definition")

        # Si rien trouvé
        if not definition:
            dispatcher.utter_message(
                text="Je n’ai pas encore la définition de ce sujet. Peux-tu préciser ?"
            )
            return []

        # -------------------------
        # 3. Adapter au niveau de l'utilisateur
        # -------------------------
        definition = adapt_content(level, definition)

        # -------------------------
        # 4. Appliquer le template
        # -------------------------
        template = get_template("definition", level)
        message = template.format(
            topic=tool or concept,
            content=definition
        )

        dispatcher.utter_message(text=message)
        return []
