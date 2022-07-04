"""Sphinx configuration."""
project = "stocked"
author = "Dovid Greenberger"
copyright = "2022, Dovid Greenberger"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
