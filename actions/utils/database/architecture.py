ARCHITECTURE_DATABASE = {

    # -----------------------------------------------------
    # 1. Architecture Docker Basique
    # -----------------------------------------------------
    "docker_architecture": {
        "description": (
            "Architecture simple basée sur Docker, adaptée aux petites applications "
            "ou environnements de développement."
        ),

        "diagram": """
          +---------------------+
          |   Docker Client     |
          +---------+-----------+
                    |
                    v
          +---------------------+
          |   Docker Engine     |
          |  (Daemon + API)     |
          +---------+-----------+
                    |
       +------------+----------------------+
       |           |                      |
       v           v                      v
   +--------+  +--------+            +--------+
   |Container| |Container|           |Container|
   |  App1   | |  App2   |           |  DB     |
   +--------+  +--------+            +--------+
        """,

        "components": [
            "Docker Client (CLI)",
            "Docker Engine / Daemon",
            "Images",
            "Containers",
            "Registry (Docker Hub, private registry)",
        ],

        "explanation": (
            "Le client Docker envoie des commandes au Docker Engine, qui gère "
            "les conteneurs. Chaque conteneur exécute une application isolée. "
            "Les images servent de modèle pour créer les conteneurs."
        ),

        "benefits": [
            "Isolation des applications",
            "Portabilité élevée",
            "Déploiement rapide",
        ],

        "challenges": [
            "Gestion du stockage",
            "Sécurisation des images",
            "Réseautage avancé",
        ],
    },

    # -----------------------------------------------------
    # 2. Architecture Kubernetes (K8s)
    # -----------------------------------------------------
    "kubernetes_architecture": {
        "description": (
            "Architecture distribuée orchestrée par Kubernetes, adaptée aux applications "
            "scalables et distribuées."
        ),

        "diagram": """
                          +---------------------------+
                          |      Control Plane        |
                          +---------------------------+
                          | API Server                |
                          | Scheduler                 |
                          | Controller Manager        |
                          | etcd (stockage)           |
                          +-------------+-------------+
                                        |
                       -------------------------------------
                       |                                   |
                       v                                   v
              +------------------+               +------------------+
              |    Worker Node   |               |    Worker Node   |
              +------------------+               +------------------+
              | Kubelet          |               | Kubelet          |
              | Kube Proxy       |               | Kube Proxy       |
              | Pods (containers)|               | Pods (containers)|
              +------------------+               +------------------+
        """,

        "components": [
            "API Server",
            "Scheduler",
            "Controller Manager",
            "etcd",
            "Kubelet",
            "Kube Proxy",
            "Pods",
            "Deployments / Services / Ingress",
        ],

        "explanation": (
            "Le Control Plane gère l'état global du cluster : planification, "
            "orchestration, supervision. Les Worker Nodes exécutent les Pods, "
            "qui contiennent les conteneurs. etcd stocke l'état du cluster."
        ),

        "benefits": [
            "Scalabilité automatique",
            "Résilience",
            "Auto-réparation",
        ],

        "challenges": [
            "Courbe d'apprentissage élevée",
            "Observabilité nécessaire",
            "Sécurisation du cluster complexe",
        ],
    },

    # -----------------------------------------------------
    # 3. Architecture CI/CD (GitLab CI)
    # -----------------------------------------------------
    "cicd_architecture": {
        "description": (
            "Pipeline CI/CD complet utilisant GitLab CI pour automatiser les tests, "
            "l'intégration et les déploiements."
        ),

        "diagram": """
   Developer
       |
       v
 +-----------+        +------------------+       +--------------------+
 |   GitLab  | -----> | GitLab Runner    | ----> | Environments       |
 |  Repo     |        | (CI/CD Engine)   |       | Dev / Staging /Prod|
 +-----------+        +------------------+       +--------------------+
        """,

        "components": [
            "GitLab Repository",
            "GitLab CI/CD Pipeline",
            "GitLab Runner",
            "Artifacts",
            "Environments (Dev, Staging, Prod)",
        ],

        "explanation": (
            "Chaque push déclenche un pipeline CI/CD. Les Runners exécutent les jobs "
            "(tests, build, déploiements). Les artefacts sont utilisés pour maintenir "
            "les résultats intermédiaires."
        ),

        "benefits": [
            "Automatisation complète",
            "Déploiements rapides et fiables",
            "Historique clair via Git",
        ],

        "challenges": [
            "Gestion des secrets",
            "Coût des pipelines",
            "Maintenance des Runners",
        ],
    },

    # -----------------------------------------------------
    # 4. Architecture Microservices
    # -----------------------------------------------------
    "microservices_architecture": {
        "description": (
            "Architecture orientée microservices, où chaque service est autonome "
            "et communique via API."
        ),

        "diagram": """
     +--------------+        +----------------+        +-----------------+
     | Auth Service | <----> |  API Gateway   | <----> |  Frontend App   |
     +--------------+        +----------------+        +-----------------+
            |                        |
            v                        v
     +--------------+        +----------------+
     | Billing Svc  |        |  User Svc      |
     +--------------+        +----------------+
        """,

        "components": [
            "API Gateway",
            "Microservices (Auth, Billing, User, etc.)",
            "Base de données par service",
            "Communication REST ou gRPC",
            "Observability stack",
        ],

        "explanation": (
            "Chaque microservice est indépendant, possède son propre cycle de vie "
            "et peut être déployé séparément. L’API Gateway unifie l'entrée et gère "
            "l'authentification, le routage et la communication."
        ),

        "benefits": [
            "Évolutivité",
            "Modularité",
            "Déploiements indépendants",
        ],

        "challenges": [
            "Complexité du monitoring",
            "Gestion des communications inter-services",
            "Versioning d’API",
        ],
    },

    # -----------------------------------------------------
    # 5. Architecture GitOps (ArgoCD)
    # -----------------------------------------------------
    "gitops_architecture": {
        "description": (
            "Architecture GitOps avec ArgoCD, où Git est la source de vérité "
            "pour les déploiements."
        ),

        "diagram": """
 +--------------+            +------------------+            +------------------+
 | Developer    |   Push     |    Git Repo      |   Sync     |   Kubernetes     |
 | (commit)     | ---------> | (Manifests YAML) | ---------> |    Cluster       |
 +--------------+            +------------------+            +---------+--------+
                                                                   |
                                                                   v
                                                             +-----------+
                                                             | ArgoCD    |
                                                             | Controller|
                                                             +-----------+
        """,

        "components": [
            "Repository Git",
            "Manifests Kubernetes",
            "ArgoCD",
            "Kubernetes Cluster",
            "Web UI ArgoCD",
        ],

        "explanation": (
            "Lorsque l'état désiré est modifié dans Git, ArgoCD détecte le changement "
            "et synchronise automatiquement le cluster Kubernetes. Cela garantit "
            "que la production reflète exactement ce qui est dans Git."
        ),

        "benefits": [
            "Audit clair via Git",
            "Reproductibilité totale",
            "Rollback extrêmement simple",
        ],

        "challenges": [
            "Gestion des Secrets",
            "Structure Git propre",
            "Compréhension de Kubernetes requise",
        ],
    },
}
