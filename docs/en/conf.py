# Import the base configuration file
from . import conf

# Language specific configuration for English documentation
language = 'en'

# Add or override configurations specific to English docs here
# For example:
# html_theme = 'custom_english_theme'  # Replace with your theme if different

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
