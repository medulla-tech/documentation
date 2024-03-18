from .. import conf  # Import the base configuration

# Set language-specific information
language = 'en'  # Or 'fr' for the French file
project = 'Medulla (English)'  # Set project title for English
copyright = '2024, Yvan Manon'
author = 'Yvan Manon'
release = '5.1'

# Sphinx extensions to load (can be language-specific)
extensions = []  # Add language-specific extensions here if needed

# The theme to use for HTML and HTML Help output (can be language-specific)
html_theme = 'sphinx_rtd_theme'

# Options for HTML output (can be language-specific)
# pygments_style = 'sphinx'  # Add language-specific styling if needed

# Grouping the doc source files (by topic) -------------------------------------

# List of patterns, relative to source directory, that match files and
# directories to group into doc trees.
# For example, 'intro.rst' documents in the root directory will be part of
# the 'intro' doc tree.
# toctree_glob = []  # Add language-specific toctree configuration if needed

# Use the language code 'en' for English content
toctree = {
    'index': [
        'intro',
        'installation',
        'usage',
        'contribute'
    ]
}

