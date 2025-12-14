# actions/action_explain_usage.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionExplainUsage(Action):
    def name(self) -> Text:
        return "action_explain_usage"

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

        # Normalize level
        level_map = {"debutant": "beginner", "intermediaire": "intermediate", "expert": "expert"}
        level_key = level_map.get(level.lower(), "beginner")

        # Normalize names
        tool = tool.lower() if tool else None

        # -------------------------
        # 2. Récupérer l’usage
        # -------------------------
        usage = None

        if tool and tool in TOOLS_DATABASE:
            usage = TOOLS_DATABASE[tool].get("usage")

        if not usage:
            dispatcher.utter_message(
                text="Je n’ai pas encore d’informations d’usage pour ce sujet."
            )
            return []

        # Liste → texte formaté
        if isinstance(usage, list):
            usage_text = "\n".join(f"- {item}" for item in usage)
        else:
            usage_text = str(usage)

        # -------------------------
        # 3. Adapter au niveau
        # -------------------------
        adapted_usage = adapt_content(level_key, usage_text)

        # -------------------------
        # 4. Formater avec un template
        # -------------------------
        template = get_template("usage", level_key)
        message = template.format(topic=tool , content=adapted_usage)

        # -------------------------
        # 5. Envoyer la réponse
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
