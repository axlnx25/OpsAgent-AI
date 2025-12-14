# actions/utils/database/concepts.py

CONCEPTS_DATABASE = {
    "ci/cd": {
        "definition": (
            "CI/CD est un ensemble de pratiques permettant d'automatiser l'intégration "
            "du code (CI) et le déploiement continu des applications (CD)."
        ),
        "explanation": (
            "CI (Continuous Integration) consiste à intégrer fréquemment les modifications "
            "du code dans un dépôt central, avec des tests automatisés pour garantir la qualité.\n"
            "CD (Continuous Delivery/Deployment) automatise la livraison ou le déploiement du "
            "logiciel en production.\n"
            "L'objectif est d'accélérer le cycle logiciel tout en réduisant les erreurs humaines."
        ),
        "analogy": (
            "CI/CD est comme une chaîne de montage automatisée dans une usine : "
            "chaque pièce (commit) est automatiquement testée, assemblée, puis livrée sans attendre."
        ),
        "examples": [
            "Pipeline GitLab CI qui compile et teste le code à chaque commit.",
            "Pipeline GitHub Actions qui déploie automatiquement sur AWS.",
        ],
        "principles": [
            "Automatisation",
            "Intégration fréquente",
            "Feedback rapide",
            "Déploiements sécurisés et reproductibles",
        ],
        "benefits": [
            "Réduction des bugs avant production",
            "Livraisons plus rapides",
            "Processus reproductibles",
            "Moins d’erreurs humaines",
        ],
        "challenges": [
            "Configurer correctement les pipelines",
            "Écrire des tests automatisés robustes",
            "Gérer les secrets et credentials",
        ],
    },

    "infrastructure as code": {
        "definition": (
            "L’Infrastructure as Code (IaC) consiste à gérer l’infrastructure "
            "serveurs, réseaux, bases de données — au moyen de fichiers code."
        ),
        "explanation": (
            "Au lieu de créer un serveur manuellement dans une console cloud, "
            "IaC permet de définir l'infrastructure dans des fichiers versionnés.\n"
            "Les outils comme Terraform ou Ansible automatisent ensuite la création, "
            "la mise à jour et la suppression de ces ressources."
        ),
        "analogy": (
            "C’est comme une recette de cuisine : tu écris exactement ce que tu veux, "
            "et l'outil se charge de préparer le plat de la même manière à chaque fois."
        ),
        "examples": [
            "Fichier Terraform pour créer un cluster Kubernetes sur AWS.",
            "Playbook Ansible pour configurer des serveurs web.",
        ],
        "principles": [
            "Idempotence",
            "Automatisation",
            "Reproductibilité",
            "Versioning",
        ],
        "benefits": [
            "Déploiements cohérents",
            "Rollback facile",
            "Audit de toute modification d’infrastructure",
        ],
        "challenges": [
            "Gestion des états (Terraform state)",
            "Écriture de modules réutilisables",
            "Gestion sécurisée des variables sensibles",
        ],
    },

    "observability": {
        "definition": (
            "L’observabilité est la capacité à comprendre l’état interne d’un système "
            "à partir de ses signaux externes (logs, métriques, traces)."
        ),
        "explanation": (
            "Elle s’appuie sur trois piliers :\n"
            "- Logs (événements détaillés)\n"
            "- Metrics (indicateurs chiffrés)\n"
            "- Traces (cheminement d’une requête)\n"
            "L'observabilité permet de diagnostiquer rapidement les problèmes."
        ),
        "analogy": (
            "C’est comme un tableau de bord de voiture : vitesse, température, alertes… "
            "tout ce dont tu as besoin pour comprendre ce qui se passe."
        ),
        "examples": [
            "Prometheus + Grafana pour les métriques",
            "ELK Stack pour les logs",
            "Jaeger pour les traces distribuées",
        ],
        "principles": [
            "Instrumentation",
            "Centralisation",
            "Visualisation",
            "Alerte proactive",
        ],
        "benefits": [
            "Détection rapide d'incidents",
            "Analyse post-mortem facilitée",
            "Amélioration continue",
        ],
        "challenges": [
            "Coût du stockage des logs",
            "Bruit dans les alertes",
            "Gérer des systèmes distribués complexes",
        ],
    },

    "containers": {
        "definition": (
            "Les conteneurs permettent d’exécuter des applications dans un environnement "
            "isolé, léger et portable."
        ),
        "explanation": (
            "Un conteneur embarque l’application et toutes ses dépendances. "
            "Contrairement à une VM, il ne nécessite pas d’OS complet.\n"
            "Docker est la plateforme la plus utilisée."
        ),
        "analogy": (
            "C’est comme une boîte hermétique : ce qu’il y a dedans ne dépend pas "
            "de l’endroit où tu poses la boîte."
        ),
        "examples": [
            "Exécuter une API Python dans un conteneur Docker.",
            "Déployer une application avec Docker Compose.",
        ],
        "principles": [
            "Isolation",
            "Portabilité",
            "Reproductibilité",
        ],
        "benefits": [
            "Rapidement déployable",
            "Consomme peu de ressources",
            "Uniformité des environnements",
        ],
        "challenges": [
            "Sécurisation des images",
            "Gestion des volumes",
            "Réseaux Docker avancés",
        ],
    },

    "microservices": {
        "definition": (
            "Les microservices sont une architecture où l’application est divisée "
            "en services indépendants et autonomes."
        ),
        "explanation": (
            "Chaque microservice gère une responsabilité précise.\n"
            "Ils communiquent via API ou messages.\n"
            "Ils peuvent être déployés indépendamment, facilitant l'évolutivité."
        ),
        "analogy": (
            "C’est comme une équipe où chaque membre a un rôle précis, "
            "plutôt qu’une seule personne qui fait tout."
        ),
        "examples": [
            "Un service Auth, un service Billing, un service Notifications.",
            "Architecture Netflix microservices.",
        ],
        "principles": [
            "Indépendance",
            "Déploiement autonome",
            "Communication via API",
        ],
        "benefits": [
            "Évolutivité",
            "Résilience",
            "Développement parallèle",
        ],
        "challenges": [
            "Complexité accrue des communications",
            "Observabilité plus difficile",
            "Gestion des versions d’API",
        ],
    },

    "gitops": {
        "definition": (
            "GitOps est une approche où Git devient la source unique de vérité "
            "pour déployer l’infrastructure et les applications."
        ),
        "explanation": (
            "Un changement dans Git déclenche automatiquement le déploiement.\n"
            "Les outils comme ArgoCD ou Flux surveillent le repo et appliquent "
            "l’état désiré sur le cluster."
        ),
        "analogy": (
            "C’est comme une télécommande : tu appuies sur un bouton (commit) "
            "et tout se configure automatiquement."
        ),
        "examples": [
            "ArgoCD qui déploie une application Kubernetes depuis un repo Git.",
            "Flux qui synchronise un cluster avec un dépôt Git.",
        ],
        "principles": [
            "Déclaratif",
            "Automatisé",
            "Versionné",
        ],
        "benefits": [
            "Sécurité (audit Git)",
            "Déploiements reproductibles",
            "Rollback très simple",
        ],
        "challenges": [
            "Gestion des secrets",
            "Structure du repo Git",
            "Apprentissage des outils GitOps",
        ],
    },
}
