# actions/action_explain_architecture.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from .utils.database.concept import CONCEPTS_DATABASE
from .utils.templates import get_template
from .utils.levels_adapter import adapt_content
from .utils.database.architecture import ARCHITECTURE_DATABASE



class ActionExplainArchitecture(Action):
    def name(self) -> Text:
        return "action_explain_architecture"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # ------------------------------------------
        # 1. Récupération des slots
        # ------------------------------------------
        tool = tracker.get_slot("tool")
        concept = tracker.get_slot("concept")
        level = tracker.get_slot("level") or "debutant"

        if tool:
            tool = tool.lower()
        if concept:
            concept = concept.lower()

        # Map langage → templates English key
        level_map = {
            "debutant": "beginner",
            "intermediaire": "intermediate",
            "expert": "expert",
        }
        level_key = level_map.get(level.lower(), "beginner")

        # ------------------------------------------
        # 2. Recherche architecture outil
        # ------------------------------------------
        architecture = None
        topic = None

        # Si un outil est reconnu
        if tool:
            # On teste les clés archi : docker_architecture, gitops_architecture…
            arch_key = f"{tool}_architecture"
            if arch_key in ARCHITECTURE_DATABASE:
                architecture = ARCHITECTURE_DATABASE[arch_key]
                topic = tool

        # ------------------------------------------
        # 3. Recherche architecture concept
        # ------------------------------------------
        if not architecture and concept:
            if concept in ARCHITECTURE_DATABASE:  # ex: microservices_architecture
                architecture = ARCHITECTURE_DATABASE[concept]
                topic = concept

            elif concept in CONCEPTS_DATABASE and "architecture" in CONCEPTS_DATABASE[concept]:
                architecture = CONCEPTS_DATABASE[concept]["architecture"]
                topic = concept

        # ------------------------------------------
        # 4. Fallback final si rien trouvé
        # ------------------------------------------
        if not architecture:
            dispatcher.utter_message(
                text=f"Désolé, je n’ai pas encore d’architecture définie pour **{tool or concept}**."
            )
            return []

        # ------------------------------------------
        # 5. Préparation des sections architecture
        # ------------------------------------------
        description = architecture.get("description", "")
        components = "\n- ".join([""] + architecture.get("components", []))
        explanation = architecture.get("explanation", "")
        benefits = "\n- ".join([""] + architecture.get("benefits", []))
        challenges = "\n- ".join([""] + architecture.get("challenges", []))
        diagram = architecture.get("diagram", "")

        full_content = (
            f" **Description** :\n{description}\n\n"
            f" **Diagramme** :\n{diagram}\n\n"
            f" **Composants principaux** :{components}\n\n"
            f" **Explication** :\n{explanation}\n\n"
            f" **Avantages** :{benefits}\n\n"
            f"️ **Défis** :{challenges}\n"
        )

        # Adaptation au niveau utilisateur
        full_content = adapt_content(level_key, full_content)

        # Template
        template = get_template("architecture", level_key)
        message = template.format(topic=topic, content=full_content)

        dispatcher.utter_message(text=message)
        return []
