# actions/action_set_level.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionSetLevel(Action):

    def name(self) -> Text:
        return "action_set_level"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # ---------------------------------------------
        # 1. Récupération du niveau depuis entités/texte
        # ---------------------------------------------
        level_entity = next(
            tracker.get_latest_entity_values("level"), None
        )

        message_text = tracker.latest_message.get("text", "").lower()

        # ---------------------------------------------
        # 2. Normalisation intelligente
        # ---------------------------------------------
        if level_entity:
            raw_level = level_entity.lower()
        else:
            raw_level = message_text

        if any(k in raw_level for k in ["debutant", "débutant", "début", "commencer"]):
            level = "beginner"

        elif any(k in raw_level for k in ["intermediaire", "intermédiaire", "moyen"]):
            level = "intermediate"

        elif any(k in raw_level for k in ["expert", "avance", "avancé", "senior"]):
            level = "expert"

        else:
            dispatcher.utter_message(
                text=(
                    "Je n'ai pas bien identifié ton niveau\n"
                    "Tu peux choisir entre : débutant, intermédiaire ou expert."
                )
            )
            return []

        # ---------------------------------------------
        # 3. Confirmation utilisateur
        # ---------------------------------------------
        dispatcher.utter_message(
            text=f"Parfait, je m'adapterai désormais à un niveau **{level}**."
        )

        # ---------------------------------------------
        # 4. Mise à jour du slot
        # ---------------------------------------------
        return [SlotSet("level", level)]
