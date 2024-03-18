from .. import conf  # Import the base configuration
language = 'fr'
project = 'Medulla (Français)'
copyright = '2024, Yvan Manon'
author = 'Yvan Manon'
release = '5.1'

# Build base directory (set based on language)
build_base = language  # 'fr' for French build directory

# The `toctree` structure for French content
toctree = {
    'index': [
        'intro_fr',  # Use separate source files for French content (optional)
        'installation_fr',
        'utilisation',  # Translate titles for French sections
        'contribuer'
    ]
}

