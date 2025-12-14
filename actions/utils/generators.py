# actions/utils/generators.py

"""
Générateurs dynamiques :
- exemples
- analogies
- pas-à-pas
- snippets de code (Shell, YAML, Dockerfile, Terraform…)
- explications pratiques
"""

from .database.tools import TOOLS_DATABASE
from .database.concept import CONCEPTS_DATABASE


# ------------------------------
# 1. Génération d’exemples
# ------------------------------

def generate_example(tool: str, concept: str = None) -> str:
    """
    Retourne un exemple concret basé sur un outil ou un concept.
    """
    tool = tool.lower() if tool else None
    concept = concept.lower() if concept else None

    if tool and tool in TOOLS_DATABASE:
        examples = TOOLS_DATABASE[tool].get("examples")
        if examples:
            return examples[0]  # simple pour l’instant, peut être random()
        else:
            return f"Aucun exemple n'est défini pour l'outil **{tool}**."

    if concept and concept in CONCEPTS_DATABASE:
        examples = CONCEPTS_DATABASE[concept].get("examples")
        if examples:
            return examples[0]
        else:
            return f"Aucun exemple n'est défini pour le concept **{concept}**."

    return "Je n’ai pas d’exemple disponible pour cette demande."


# ------------------------------
# 2. Génération d’analogies
# ------------------------------

def generate_analogy(tool: str = None, concept: str = None) -> str:
    """
    Génère une analogie pédagogique.
    """
    tool = tool.lower() if tool else None
    concept = concept.lower() if concept else None

    if tool and tool in TOOLS_DATABASE:
        analogy = TOOLS_DATABASE[tool].get("analogy")
        if analogy:
            return analogy
        return f"Je n'ai pas encore d'analogie enregistrée pour {tool}."

    if concept and concept in CONCEPTS_DATABASE:
        analogy = CONCEPTS_DATABASE[concept].get("analogy")
        if analogy:
            return analogy
        return f"Je n'ai pas encore d'analogie enregistrée pour {concept}."

    return "Je n’ai pas d’analogie pour ce sujet."


# ------------------------------
# 3. Pas-à-pas générique
# ------------------------------

def generate_step_by_step(tool: str, action: str = "install") -> list:
    """
    Génère un guide pas-à-pas pour :
    - installer un outil
    - le configurer
    - le déployer
    """

    tool = tool.lower()

    if tool not in TOOLS_DATABASE:
        return [f"Aucune information pas-à-pas pour {tool}."]

    data = TOOLS_DATABASE[tool]

    if action == "install":
        install = data.get("installation", {})
        if isinstance(install, dict):
            steps = install.get("linux") or install.get("windows") or install.get("macos")
            return steps if steps else ["Installation non disponible."]

    if action == "configure":
        config = data.get("configuration")
        if config:
            return config

    return ["Pas-à-pas non disponible pour cette action."]


# ------------------------------
# 4. Génération de code
# ------------------------------

def generate_code(tool: str, language: str):
    """
    Génère des snippets de code courants pour un outil DevOps.
    Supporte : shell, dockerfile, yaml, terraform, ansible
    """
    tool = tool.lower()
    language = language.lower()

    if tool == "docker":
        return _docker_code(language)

    if tool == "kubernetes":
        return _k8s_code(language)

    if tool == "terraform":
        return _terraform_code(language)

    if tool == "ansible":
        return _ansible_code()

    if tool == "git":
        return _git_code()

    return f"Je n'ai pas encore de génération de code pour {tool} en {language}."


# ------------------------------
# Docker
# ------------------------------

def _docker_code(lang):
    if lang == "dockerfile":
        return (
            "FROM python:3.10-slim\n"
            "WORKDIR /app\n"
            "COPY . .\n"
            "RUN pip install -r requirements.txt\n"
            "CMD [\"python\", \"main.py\"]"
        )
    if lang == "shell":
        return "docker build -t mon_app . && docker run -p 8000:8000 mon_app"
    return "Format non supporté pour Docker."


# ------------------------------
# Kubernetes
# ------------------------------

def _k8s_code(lang):
    if lang == "yaml":
        return (
            "apiVersion: apps/v1\n"
            "kind: Deployment\n"
            "metadata:\n"
            "  name: my-app\n"
            "spec:\n"
            "  replicas: 2\n"
            "  selector:\n"
            "    matchLabels:\n"
            "      app: my-app\n"
            "  template:\n"
            "    metadata:\n"
            "      labels:\n"
            "        app: my-app\n"
            "    spec:\n"
            "      containers:\n"
            "      - name: my-app\n"
            "        image: my-image:latest\n"
            "        ports:\n"
            "        - containerPort: 8080"
        )
    return "Format non supporté pour Kubernetes."


# ------------------------------
# Terraform
# ------------------------------

def _terraform_code(lang):
    return (
        'provider "aws" {\n'
        '  region = "us-east-1"\n'
        '}\n\n'
        'resource "aws_s3_bucket" "bucket" {\n'
        '  bucket = "my-terraform-bucket"\n'
        '}'
    )


# ------------------------------
# Ansible
# ------------------------------

def _ansible_code():
    return (
        "- name: Installer Nginx\n"
        "  hosts: web\n"
        "  become: yes\n"
        "  tasks:\n"
        "    - name: installer nginx\n"
        "      apt:\n"
        "        name: nginx\n"
        "        state: present"
    )


# ------------------------------
# Git
# ------------------------------

def _git_code():
    return (
        "git init\n"
        "git add .\n"
        "git commit -m 'Initial commit'\n"
        "git push origin main"
    )
