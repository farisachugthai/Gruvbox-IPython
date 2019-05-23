# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Apr 21, 2019: This is neat
# Apr 22, 2019. Holy hell. I don't know enough about logging to utilize this.
from sphinx.util import logging

logger = logging.getLogger(__name__)

logger.setLevel(level=logging.LEVEL_NAMES['DEBUG'])
# Or you can go logger.setLevel(level=logging.VERBOSE) where VERBOSE==15
# Regardless level is required and the levels are anonymized through a lambda into
# :class:`defaultdict`
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = u'Gruvbox IPython'
copyright = u'2019, Faris A Chugthai'
author = u'Faris A Chugthai'

# The short X.Y version
version = '2019'
# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# here are a bunch of useful options i just stumbled upon!
# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# Set the default role so we can use `foo` instead of ``foo``
default_role = 'py:obj'

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'numpydoc.numpydoc',
    'matplotlib.sphinxext.plot_directive',
    'matplotlib.sphinxext.mathmpl',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['.*ipynb_checkpoints**']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'Gruvbox'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_user": "Faris A. Chugthai",
    "github_repo": "Gruvbox-IPython",
    "github_banner": True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
html_sidebars = {
    '**': [
        'about.html',
        'relations.html',
        'localtoc.html',
        'searchbox.html',
        'sourcelink.html',
    ]
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GruvboxIPython'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GruvboxIPython.tex', 'Gruvbox IPython Documentation',
     'Faris A Chugthai', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'gruvboxipython', 'Gruvbox IPython Documentation', [
    author
], 1)]

manpages_url = "https://linux.die.net/man"
# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GruvboxIPython', 'Gruvbox IPython Documentation', author,
     'GruvboxIPython', 'One line description of project.', 'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.


def pygments_traceback():
    """Pygments got commented out because of this error.

    May 07, 2019:

    .. code-block:: python3-traceback

        WARNING: failed to reach any of the inventories with the following issues:
        intersphinx inventory 'http://pygments.org/objects.inv' not readable
        due to ValueError: unknown or unsupported inventory version:
        ValueError('invalid inventory header: <!DOCTYPE html PUBLIC "-//W3C//DTD
        XHTML 1.0 Transitional//EN"')

    ...?

    """
    pass


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'ipython': ('https://ipython.readthedocs.io/en/stable/', None),
    # 'pygments': ('http://pygments.org/', None),
    'neovim': ('https://pynvim.readthedocs.io/en/latest/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/master', None),
}

#  -- numpydoc configuration --------------------------------------------------
# All parameters:
# cfg = {'use_plots': app.config.numpydoc_use_plots,
#        'use_blockquotes': app.config.numpydoc_use_blockquotes,
#        'show_class_members': app.config.numpydoc_show_class_members,
#        'show_inherited_class_members':
#        app.config.numpydoc_show_inherited_class_members,
#        'class_members_toctree': app.config.numpydoc_class_members_toctree,
#        'attributes_as_param_list':
#        app.config.numpydoc_attributes_as_param_list,
#        'xref_param_type': app.config.numpydoc_xref_param_type,
#        'xref_aliases': app.config.numpydoc_xref_aliases,
#        'xref_ignore': app.config.numpydoc_xref_ignore,
#        }

numpydoc_show_class_members = False  # Otherwise Sphinx emits thousands of warnings
numpydoc_class_members_toctree = False
ipython_warning_is_error = True


def setup(app):
    """Add flask css.

     Use the method ``add_css_file`` method as ``add_stylesheet`` was deprecated.

     Also note that the ``app.add_css_file`` method refers to the parameter
     ``html_static_path`` and therefore doesn't need {and shouldn't be} specified
     as a pathname relative to this file.
     """
    app.add_css_file(os.path.join('_static', '', 'flask.css_t'))
    app.add_css_file('gruvbox.css')
    logger.debug('gruvbox.css added.')
