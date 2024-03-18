# Import the base configuration file
from . import conf

# Language specific configuration for French documentation
language = 'fr'

# Add or override configurations specific to French docs here
# For example:
# html_title = 'Medulla - Documentation Française'  # Set a French title

# Inherit configurations from the base file
extensions = conf.extensions
templates_path = conf.templates_path
exclude_patterns = conf.exclude_patterns
html_static_path = conf.html_static_path

# Add project specific configurations here (common to both languages)
project = 'Medulla'
copyright = '2024, Yvan Manon'
author = 'Yvan Manon'
release = '5.1'

# ... rest of your project specific configurations ...

