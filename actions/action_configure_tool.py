# actions/action_configure_tool.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionConfigureTool(Action):

    def name(self) -> Text:
        return "action_configure_tool"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # --------------------------------------------------
        # 1. Lecture des slots
        # --------------------------------------------------
        tool = tracker.get_slot("tool")
        level = tracker.get_slot("level") or "debutant"

        if not tool:
            dispatcher.utter_message(
                text="Quel outil souhaitez-vous configurer ?"
            )
            return []

        tool = tool.lower()

        level_map = {
            "debutant": "beginner",
            "intermediaire": "intermediate",
            "expert": "expert",
        }
        level_key = level_map.get(level.lower(), "beginner")

        # --------------------------------------------------
        # 2. Vérification outil
        # --------------------------------------------------
        if tool not in TOOLS_DATABASE:
            dispatcher.utter_message(
                text=f"Je ne dispose pas d'informations de configuration pour {tool}."
            )
            return []

        # --------------------------------------------------
        # 3. Récupération configuration depuis DATABASE
        # --------------------------------------------------
        configuration = TOOLS_DATABASE[tool].get("configuration")

        if not configuration:
            dispatcher.utter_message(
                text=f"Aucune configuration disponible pour {tool}."
            )
            return []

        # --------------------------------------------------
        # 4. Normalisation du contenu
        # --------------------------------------------------
        if isinstance(configuration, list):
            content = "\n".join(configuration)
        else:
            content = str(configuration)

        # --------------------------------------------------
        # 5. Adaptation au niveau
        # --------------------------------------------------
        adapted_content = adapt_content(level_key, content)

        # --------------------------------------------------
        # 6. Chargement du template
        # --------------------------------------------------
        template = get_template("configuration", level_key)

        # --------------------------------------------------
        # 7. Formatage final
        # --------------------------------------------------
        message = template.format(
            tool=tool,
            content=adapted_content
        )

        # --------------------------------------------------
        # 8. Réponse
        # --------------------------------------------------
        dispatcher.utter_message(text=message)
        return []
