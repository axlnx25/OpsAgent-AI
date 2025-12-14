# actions/action_install_tool.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .utils.database.tools import TOOLS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content


class ActionInstallTool(Action):

    def name(self) -> Text:
        return "action_install_tool"

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
        level = tracker.get_slot("level") or "debutant"

        if tool:
            tool = tool.lower()

        # Mapper les niveaux
        level_map = {
            "debutant": "beginner",
            "intermediaire": "intermediate",
            "expert": "expert",
        }
        level_key = level_map.get(level.lower(), "beginner")

        # -------------------------
        # 2. Vérifier que l'outil existe
        # -------------------------
        if not tool or tool not in TOOLS_DATABASE:
            dispatcher.utter_message(
                text="Je ne connais pas encore cet outil dans ma base."
            )
            return []

        installation_data = TOOLS_DATABASE[tool].get("installation")

        if not installation_data:
            dispatcher.utter_message(
                text=f"Je n’ai pas encore d’instructions d’installation pour **{tool}**."
            )
            return []

        # -------------------------
        # 3. Rassembler les instructions pour tous les OS
        # -------------------------
        final_text = ""

        for os_name, steps in installation_data.items():

            # Convertir liste → texte
            if isinstance(steps, list):
                steps_text = "\n".join(f"- {step}" for step in steps)
            else:
                steps_text = str(steps)

            final_text += f"\n### Installation sur {os_name.capitalize()} :\n{steps_text}\n"

        # -------------------------
        # 4. Adapter en fonction du niveau (débutant/intermédiaire/expert)
        # -------------------------
        adapted_text = adapt_content(level_key, final_text)

        # -------------------------
        # 5. Appliquer le template
        # -------------------------
        template = get_template("installation", level_key)
        message = template.format(topic=tool, content=adapted_text)

        # -------------------------
        # 6. Répondre
        # -------------------------
        dispatcher.utter_message(text=message)
        return []
