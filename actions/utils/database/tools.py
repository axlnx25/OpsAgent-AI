TOOLS_DATABASE = {
    "docker": {
        "definition": (
            "Docker est une plateforme de conteneurisation permettant d’empaqueter, "
            "distribuer et exécuter des applications dans des environnements isolés "
            "appelés *containers*."
        ),

        "explanation": (
            "Docker permet de créer des environnements légers et reproductibles. "
            "Il évite les problèmes du type 'chez moi ça marche' en standardisant "
            "l’exécution de l’application via une image contenant tout ce qu’il faut "
            "(code, dépendances, librairies…)."
        ),

        "installation": {
            "linux": [
                "sudo apt update",
                "sudo apt install docker.io -y",
                "sudo systemctl enable --now docker",
                "sudo usermod -aG docker $USER"
            ],
            "windows": [
                "Installer Docker Desktop",
                "Activer WSL2",
                "Redémarrer la machine"
            ],
            "mac": [
                "Installer Docker Desktop depuis le site officiel",
                "Lancer l’application Docker"
            ],
        },

        "configuration": [
            "Créer un fichier Dockerfile pour décrire l’image",
            "Configurer docker-compose.yml pour orchestrer plusieurs services",
            "Configurer un registry privé si nécessaire"
        ],

        "usage": [
            "docker build -t app .",
            "docker run -p 8080:80 app",
            "docker ps, docker images, docker logs…"
        ],

        "step_by_step": [
            "Créer Dockerfile",
            "Construire l’image avec docker build",
            "Lancer le conteneur",
            "Tester depuis le navigateur / API",
            "Optimiser l’image (multi-stage etc.)"
        ],

        "best_practices": [
            "Utiliser des images officielles et légères (alpine)",
            "Éviter de lancer les conteneurs en root",
            "Nettoyer les images inutiles (docker system prune)"
        ],

        "resources": [
            "Documentation officielle : docs.docker.com",
            "Docker Hub",
            "Play with Docker"
        ],
    },

    # ======================================================
    # Kubernetes
    # ======================================================
    "kubernetes": {
        "definition": (
            "Kubernetes est une plateforme d’orchestration de conteneurs permettant "
            "de déployer, scaler et gérer automatiquement des applications distribuées."
        ),

        "explanation": (
            "Kubernetes regroupe les conteneurs en *pods*, gère le réseau, la "
            "scalabilité, les mises à jour sans interruption (rolling updates) "
            "et surveille l’état de l’application."
        ),

        "installation": {
            "linux": [
                "Installer kubectl",
                "Installer minikube pour un cluster local",
                "minikube start"
            ],
        },

        "configuration": [
            "Créer des manifests YAML : Deployment, Service, ConfigMap, Secret",
            "Appliquer avec kubectl apply -f",
            "Créer des namespaces pour isoler les environnements"
        ],

        "usage": [
            "kubectl get pods",
            "kubectl logs <pod>",
            "kubectl apply -f app.yaml"
        ],

        "step_by_step": [
            "Rédiger un Deployment",
            "Créer un Service",
            "Déployer avec kubectl",
            "Exposer l’application",
            "Observer les pods et logs"
        ],

        "best_practices": [
            "Définir des requests/limits CPU et RAM",
            "Utiliser des ConfigMaps et Secrets",
            "Externaliser la configuration",
            "Éviter les images trop lourdes"
        ],

        "resources": [
            "kubernetes.io/docs",
            "Katacoda Kubernetes scenarios",
            "Play with Kubernetes"
        ],
    },

    # ======================================================
    # Git
    # ======================================================
    "git": {
        "definition": (
            "Git est un système de contrôle de version distribué permettant de "
            "suivre les modifications du code et de collaborer efficacement."
        ),

        "explanation": (
            "Git permet de créer des branches, gérer des versions, collaborer via "
            "GitHub/GitLab, et suivre l'historique complet d'un projet."
        ),

        "installation": {
            "linux": ["sudo apt install git"],
            "windows": ["Installer Git for Windows"],
            "mac": ["brew install git"],
        },

        "configuration": [
                "Configurer l’identité utilisateur :",
                "  git config --global user.name \"Ton Nom\"",
                "  git config --global user.email \"ton.email@example.com\"",

                "Définir l’éditeur par défaut :",
                "  git config --global core.editor \"vim\"",

                "Activer le stockage des identifiants :",
                "  git config --global credential.helper store",

                "Configurer le comportement du pull :",
                "  git config --global pull.rebase true",

                "Configurer la branche par défaut :",
                "  git config --global init.defaultBranch main"
            ],

        "usage": [
            "git clone url_du_repo",
            "git add .",
            "git commit -m 'message'",
            "git push"
        ],

        "step_by_step": [
            "Installer Git sur la machine",
            "Configurer l’identité utilisateur (nom et email)",
            "Initialiser un dépôt avec git init ou cloner un dépôt existant",
            "Créer ou modifier des fichiers du projet",
            "Ajouter les fichiers à l’index avec git add",
            "Créer un commit avec un message clair",
            "Créer une branche si nécessaire",
            "Pousser les changements vers le dépôt distant",
            "Mettre à jour le dépôt local avec git pull"
        ],


        "best_practices": [
            "Faire des commits petits et fréquents",
            "Nommer clairement les branches",
            "Éviter de commit des secrets"
        ],

        "resources": [
            "Documentation Git",
            "Pro Git book"
        ],
    },

    # ======================================================
    # GitLab CI
    # ======================================================
    "gitlab ci": {
        "definition": (
            "GitLab CI est une plateforme d’intégration et livraison continue "
            "basée sur un fichier .gitlab-ci.yml."
        ),

        "explanation": (
            "Il permet d’automatiser les tests, builds, déploiements et analyse de sécurité."
        ),

        "usage": [
            "Créer un fichier .gitlab-ci.yml",
            "Définir des stages : build, test, deploy",
            "Configurer un runner"
        ],

        "configuration": [
                "Configurer GitLab Runner :",
                "  sudo gitlab-runner register",
                "    -> choisir le type d’exécuteur (shell, docker, kubernetes)",
                "    -> coller le token du projet",
                "    -> définir le nom du runner",
                "",
                "Définir le fichier CI/CD : .gitlab-ci.yml",
                "Exemple minimal :",
                "  stages:",
                "    - build",
                "    - test",
                "",
                "  build_job:",
                "    stage: build",
                "    script:",
                "      - echo \"Build en cours...\"",
                "",
                "Configurer les variables CI/CD :",
                "  GitLab → Settings → CI/CD → Variables",
                "",
                "Configurer les règles de déclenchement :",
                "  rules:",
                "    - if: \"$CI_COMMIT_BRANCH == 'main'\""
            ],


        "step_by_step": [
            "Créer ou disposer d’un dépôt Git sur GitLab",
            "Vérifier que GitLab CI/CD est activé sur le projet",
            "Créer un fichier .gitlab-ci.yml à la racine du dépôt",
            "Définir les stages du pipeline (build, test, deploy)",
            "Créer les jobs associés à chaque stage",
            "Choisir l’environnement d’exécution (image Docker ou shell)",
            "Configurer ou enregistrer un GitLab Runner",
            "Définir les variables CI/CD (secrets, tokens, clés)",
            "Commiter et pousser le fichier .gitlab-ci.yml",
            "Observer l’exécution du pipeline dans l’interface GitLab",
            "Analyser les logs des jobs",
            "Corriger ou optimiser le pipeline si nécessaire"
        ],


        "resources": [
            "docs.gitlab.com/ci"
        ],
    },

    # ======================================================
    # Terraform
    # ======================================================
    "terraform": {
        "definition": (
            "Terraform est un outil Infrastructure as Code permettant de créer, "
            "modifier et versionner l’infrastructure via des fichiers déclaratifs."
        ),

        "explanation": (
            "Il permet de gérer cloud, réseau, VM, stockage et services via un langage "
            "appelé HCL, reproductible et versionnable."
        ),

        "usage": [
            "terraform init",
            "terraform plan",
            "terraform apply"
        ],

        "configuration": [
                "Initialiser un projet :",
                "  terraform init",
                "",
                "Définir un provider :",
                "  provider \"aws\" {",
                "    region = \"us-east-1\"",
                "  }",
                "",
                "Configurer un backend distant (S3) :",
                "  terraform {",
                "    backend \"s3\" {",
                "      bucket = \"mon-bucket-terraform\"",
                "      region = \"us-east-1\"",
                "      key    = \"state.tfstate\"",
                "    }",
                "  }",
                "",
                "Configurer des variables :",
                "  variable \"instance_type\" {",
                "    default = \"t2.micro\"",
                "  }",
                "",
                "Créer un fichier terraform.tfvars :",
                "  instance_type = \"t3.micro\"",
                "",
                "Vérifier la configuration :",
                "  terraform validate",
                "",
                "Générer un plan d’exécution :",
                "  terraform plan"
            ],

        "step_by_step": [
            "Installer Terraform",
            "Créer un nouveau dossier de projet",
            "Définir le provider cloud dans un fichier .tf",
            "Décrire les ressources d’infrastructure",
            "Initialiser le projet avec terraform init",
            "Vérifier la configuration avec terraform validate",
            "Générer le plan d’exécution avec terraform plan",
            "Appliquer l’infrastructure avec terraform apply",
            "Vérifier les ressources créées dans le cloud",
            "Modifier la configuration et réappliquer si nécessaire"
        ],


        "resources": [
            "developer.hashicorp.com/terraform"
        ],
    },

    # ======================================================
    # Ansible
    # ======================================================
    "ansible": {
        "definition": (
            "Ansible est un outil de configuration automatique permettant de gérer "
            "des serveurs via des playbooks YAML sans agent."
        ),

        "explanation": (
            "Ansible utilise SSH pour exécuter des tâches sur des serveurs. "
            "Il est simple, modulaire et idéal pour la configuration."
        ),

        "usage": [
            "ansible all -m ping",
            "ansible-playbook site.yml"
        ],

        "configuration": [
                "Créer un fichier d'inventaire hosts.ini :",
                "  [web]",
                "  192.168.1.10",
                "  192.168.1.11",
                "",
                "Configurer ansible.cfg :",
                "  [defaults]",
                "  inventory = ./hosts.ini",
                "  remote_user = ubuntu",
                "  host_key_checking = False",
                "",
                "Configurer l’accès SSH :",
                "  ssh-copy-id ubuntu@192.168.1.10",
                "",
                "Définir un playbook minimal :",
                "  - hosts: web",
                "    become: true",
                "    tasks:",
                "      - name: Installer nginx",
                "        apt:",
                "          name: nginx",
                "          state: present",
                "",
                "Tester la connectivité :",
                "  ansible all -m ping",
                "",
                "Exécuter un playbook :",
                "  ansible-playbook site.yml"
            ],


        "step_by_step": [
            "Installer Ansible sur la machine de contrôle",
            "Créer un fichier d’inventaire listant les serveurs",
            "Configurer l’accès SSH vers les machines distantes",
            "Créer un fichier ansible.cfg pour les paramètres globaux",
            "Écrire un playbook YAML simple",
            "Définir les hôtes ciblés et les privilèges (become)",
            "Ajouter des tâches (installation, configuration, services)",
            "Tester la connectivité avec ansible all -m ping",
            "Exécuter le playbook avec ansible-playbook",
            "Vérifier l’état final des serveurs"
        ],



        "resources": [
            "docs.ansible.com"
        ],
    },
}
