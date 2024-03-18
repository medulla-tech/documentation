# -- Common configurations (placeholders, set language-specific in docs/en/conf.py and docs/fr/conf.py) --------

# List of patterns, relative to source directory, that match files and
# directories to exclude from the build.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The path for custom CSS files.
html_static_path = ['_static']

# Optional: Set build base directory based on environment variable (set by RTD)
# Uncomment and adjust if not using separate build directories in .readthedocs.yml
# build_base = os.environ.get('READTHEDOCS_LANGUAGE', '')

# -- Sphinx extensions to load (can be language-specific) --------
# Add language-specific extensions here if needed
extensions = []

# The theme to use for HTML and HTML Help output (can be language-specific)
html_theme = 'sphinx_rtd_theme'

# Options for HTML output (can be language-specific)
# pygments_style = 'sphinx'  # Add language-specific styling if needed

