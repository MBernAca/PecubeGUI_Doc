# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PecubeGUI'
copyright = '2022, Maxime Bernard'
author = 'Maxime Bernard'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx-rtd-theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"logo_only": True}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/Pecube_icon.ico"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/Pecube_icon.ico"


# -- Options for EPUB output
epub_show_urls = 'footnote'
