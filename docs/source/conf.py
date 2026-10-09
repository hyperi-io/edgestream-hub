import os
import sys

project = 'EdgeStream Hub'
copyright = '2026, Hyperi'
author = 'Hyperi'

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
]

# Allow Markdown and rST
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Root document (Sphinx defaults to index)
root_doc = 'index'

# Theme configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'collapse_navigation': True,   # Submenus stay closed until clicked or active
    'sticky_navigation': True,
    'navigation_depth': 6,         # Depth of expandable nesting allowed
    'includehidden': True,
    'titles_only': False,
}

# Useful MyST parsing extensions
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'fieldlist',
]