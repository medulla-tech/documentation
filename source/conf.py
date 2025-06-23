# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Medulla RMM'
copyright = ''
author = ''
release = '5.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

# Set the default language to French (FR)
language = 'fr'

templates_path = ['_templates']
exclude_patterns = []

html_sidebars = {
    '**': [
        'globaltoc.html',
    ]
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

