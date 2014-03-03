# -*- coding: utf-8 -*-
#
# Infantium documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 28 12:47:44 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import sys
import os
sys.path.insert(0, os.path.abspath('../../'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames. Default is '.rst'
# source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The document name of the “master” document, that is, the document that contains the root toctree directive.
# Default is 'contents'.
master_doc = 'index'

# General information about the project.
project = u'Infantium Dev Center'
copyright = u'2014, Infantium S.L. Barcelona, Spain'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.1'
# The full version, including alpha/beta/rc tags.
release = '2.1.0.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
# The default language to highlight source code in. The default is 'python'.
highlight_language = 'java'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Infantium Developers Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Infantium Docs'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/logo.png"

# Custom sidebar templates, must be a dictionary that maps document names to template names.
# html_sidebars = {
#     '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
# }

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Infantiumdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Infantium.tex', u'Infantium Documentation',
     u'Infantium', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'infantium', u'Infantium Documentation',
     [u'Infantium'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Infantium', u'Infantium Documentation',
     u'Infantium', 'Infantium', 'Developing Minds.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# A string of reStructuredText that will be included at the end of every source file that is read.
# This is the right place to add substitutions that should be available in every file.
rst_epilog = """

Docs version: |version| |br| Last update: |today|

.. |br| raw:: html

   <br />
"""