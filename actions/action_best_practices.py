# actions/action_best_practices.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionBestPractices(Action):
    def name(self) -> Text:
        return "action_best_practices"

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
        level = tracker.get_slot("level") or "debutant"

        # Normalisation
        tool = tool.lower() if tool else None

        level_map = {
            "debutant": "beginner",
            "intermediaire": "intermediate",
            "expert": "expert"
        }
        level_key = level_map.get(level.lower(), "beginner")

        # -------------------------
        # 2. Récupérer les bonnes pratiques depuis DATABASE
        # -------------------------
        if not tool or tool not in TOOLS_DATABASE:
            dispatcher.utter_message(text="Je n’ai pas de bonnes pratiques pour cet outil.")
            return []

        practices = TOOLS_DATABASE[tool].get("best_practices")

        if not practices:
            dispatcher.utter_message(text="Aucune bonne pratique trouvée pour cet outil.")
            return []

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        adapted_practices = adapt_content(level_key, "\n".join(practices))

        # -------------------------
        # 4. Charger le template
        # -------------------------
        template = get_template("best_practices", level_key)

        # -------------------------
        # 5. Formater la réponse
        # -------------------------
        message = template.format(topic=tool, content=adapted_practices)

        # -------------------------
        # 6. Répondre
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
