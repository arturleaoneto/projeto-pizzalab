import os
import sys
import django

# Caminho para a raiz do projeto Django
sys.path.insert(0, os.path.abspath("../.."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

# Informacoes do projeto
project = "Pizza Lab"
author = "Seu Nome ou Equipe"
release = "0.1.0"

# Idioma da documentacao
language = "pt_BR"

# Extensoes
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Diretórios de template e arquivos estáticos
templates_path = ["_templates"]
exclude_patterns = []
html_static_path = ["_static"]

# Tema HTML
html_theme = "alabaster"


html_theme = "sphinx_rtd_theme"
