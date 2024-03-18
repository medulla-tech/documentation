# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Medulla'
copyright = '2024, Yvan Manon'
author = 'Yvan Manon'
release = '5.1'

# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = "en"

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
