project = "EMAI-COPD"
author = "Your Name or Lab"
release = "0.1"

extensions = [
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
# html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_logo = "_static/logo.png"
# html_theme_options = {"sidebar_hide_name": False}