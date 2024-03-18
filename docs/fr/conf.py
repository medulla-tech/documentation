from .. import conf  # Import the base configuration
ilanguage = 'fr'
project = 'Medulla (Français)'
copyright = '2024, Yvan Manon'
author = 'Yvan Manon'
release = '5.1'

# Build base directory (optional, set here or uncomment in conf.py)
# build_base = 'fr'  # Uncomment to use a separate directory for French build

# The `toctree` structure for French content
toctree = {
    'index': [
        'intro_fr',  # Use separate source files for French content (optional)
        'installation_fr',
        'utilisation',  # Translate titles for French sections
        'contribuer'
    ]
}

