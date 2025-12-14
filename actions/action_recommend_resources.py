# actions/action_recommend_resources.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionRecommendResources(Action):

    def name(self) -> Text:
        return "action_recommend_resources"

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

        level_map = {
            "debutant": "beginner",
            "intermediaire": "intermediate",
            "expert": "expert",
        }
        level_key = level_map.get(level.lower(), "beginner")

        # --------------------------------------------------
        # 2. Priorité outil > concept
        # --------------------------------------------------
        if tool:
            tool = tool.lower()

            if tool not in TOOLS_DATABASE:
                dispatcher.utter_message(
                    text=f"Je n'ai pas de ressources documentées pour l’outil {tool}."
                )
                return []

            resources = TOOLS_DATABASE[tool].get("resources")

            if not resources:
                dispatcher.utter_message(
                    text=f"Aucune ressource disponible pour {tool}."
                )
                return []

            content = "\n".join(f"- {r}" for r in resources)

            adapted_content = adapt_content(level_key, content)
            template = get_template("resources", level_key)

            dispatcher.utter_message(
                text=template.format(
                    topic=tool,
                    content=adapted_content
                )
            )
            return []

        # --------------------------------------------------
        # 3. Rien fourni → clarification
        # --------------------------------------------------
        dispatcher.utter_message(
            text="Souhaites-tu des ressources pour un outil ou pour un concept DevOps précis ?"
        )
        return []
