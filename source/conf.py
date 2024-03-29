# -*- coding: utf-8 -*-
#
# wradlib documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 26 13:48:08 2011.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import glob
import subprocess

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['nbsphinx',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.coverage',
              "sphinx.ext.extlinks",
              'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax',
              'sphinx.ext.todo',
              'sphinxcontrib.bibtex',
              ]

extlinks = {
    "issue": ("https://github.com/wradlib/wradlib/issues/%s", "GH%s"),
    "pull": ("https://github.com/wradlib/wradlib/pull/%s", "PR%s"),
}

mathjax_path = ("https://cdn.mathjax.org/mathjax/latest/MathJax.js?"
                "config=TeX-AMS-MML_HTMLorMML")

# The suffix of source filenames.
# source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The main toctree document.
root_doc = 'index'

# General information about the project.
project = u'wradlib'
copyright = u'2011-2022, wradlib developers'
docs = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()
url = 'https://github.com/wradlib'

# check readthedocs
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# processing on readthedocs
if on_rtd:
    # rtd_version will be either 'latest', 'stable' or some tag name which
    # should correspond to the wradlib and wradlib-docs tag
    rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
    print("RTD Version: {}".format(rtd_version))
    # latest wradlib commit
    if rtd_version == 'latest':
        wradlib_notebooks_branch = 'devel'
        wradlib_branch_or_tag = 'main'
    # latest tagged commit
    elif rtd_version == 'stable':
        tag = subprocess.check_output(['git', 'describe',
                                       '--abbrev=0', '--tags'],
                                      universal_newlines=True).strip()
        wradlib_notebooks_branch = tag
        wradlib_branch_or_tag = tag
    # rely on rtd_version (wradlib-docs tag)
    else:
        wradlib_notebooks_branch = rtd_version
        wradlib_branch_or_tag = rtd_version

    # clone wradlib-notebooks target branch
    repourl = '{0}/wradlib-notebooks.git'.format(url)
    reponame = 'wradlib-notebooks'
    # first remove any possible left overs
    subprocess.check_call(['rm', '-rf', 'wradlib-notebooks'])
    subprocess.check_call(['rm', '-rf', 'notebooks'])
    subprocess.check_call(['git', 'clone', '-b', wradlib_notebooks_branch,
                           repourl, reponame])
    branch = 'origin/{}'.format(wradlib_branch_or_tag)
    nb = subprocess.check_output(['git', '--git-dir=wradlib-notebooks/.git',
                                  'rev-parse', branch]).decode().strip()
    subprocess.check_call(['mv', 'wradlib-notebooks/notebooks', '.'])
    subprocess.check_call(['rm', '-rf', 'wradlib-notebooks'])

    # correct notebook doc-links
    if rtd_version != 'latest':
        baseurl = 'https://docs.wradlib.org/en/{}'
        search = baseurl.format('latest')
        replace = baseurl.format(rtd_version)
        subprocess.check_call(["find notebooks -type f -name '*.ipynb' -exec "
                               "sed -i 's%{search}%{replace}%g' {{}} +"
                               "".format(search=search, replace=replace)],
                              shell=True)

    # install wradlib target branch/tag
    subprocess.check_call(['python', '-m', 'pip', 'install', '--no-deps', '--upgrade',
                           "git+{0}/wradlib.git@{1}"
                           "".format(url, wradlib_branch_or_tag)])

# Mock modules
import sys
from unittest.mock import MagicMock


class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()


MOCK_MODULES = ['scipy', 'scipy.spatial', 'scipy.stats',
                'scipy.interpolate', 'scipy.ndimage',
                'scipy.ndimage.interpolation',
                'scipy.ndimage.filters', 'scipy.signal',
                # 'matplotlib', 'matplotlib.path', 'matplotlib.patches',
                # 'matplotlib.pyplot', 'matplotlib.projections',
                # 'matplotlib.transforms',
                # 'matplotlib.ticker',
                # 'matplotlib.dates',
                # 'matplotlib.collections',
                # 'mpl_toolkits',
                # 'mpl_toolkits.axisartist',
                # 'mpl_toolkits.axisartist.grid_finder',
                # 'mpl_toolkits.axisartist.angle_helper',
                # 'h5py', 'h5netcdf',
                # 'netCDF4', 'osgeo',
                # 'cartopy',
                ]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# get wradlib version
import wradlib  # noqa

# get wradlib modules and create automodule rst-files
import types
modules = []
for k, v in wradlib.__dict__.items():
    if type(v) is types.ModuleType:
        if not k in ['_warnings', 'version']:
            modules.append(k)
            file = open('{0}.rst'.format(k), mode='w')
            file.write('.. automodule:: wradlib.{}\n'.format(k))
            file.close()

# create API/Library reference rst-file
reference = """Library Reference
=================

.. toctree::
   :maxdepth: 1
"""

file = open('reference.rst', mode='w')
file.write('{}\n'.format(reference))
for mod in sorted(modules):
    file.write('   {}\n'.format(mod))
file.close()

# get all rst files, do it manually
rst_files = glob.glob('*.rst')
autosummary_generate = rst_files
autoclass_content = 'both'

# The full version, including alpha/beta/rc tags.
version = wradlib.__version__
release = wradlib.__version__

print("RELEASE, VERSION", release, version)

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# exclude_patterns = []
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'notebooks/overview.ipynb']

# -- nbsphinx specifics --
# do not execute notebooks ever while building docs
nbsphinx_execute = 'never'

# The reST default role (used for this markup: `text`)
# to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# linkcheck options
linkcheck_ignore = [
    "https://data.apps.fao.org/map/catalog/srv/eng/catalog.search#"
]

# -- Options for HTML output --------------------------------------------------

import sphinx_rtd_theme  # noqa

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {'sticky_navigation': True}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "images/wradlib_logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "images/favicon.ico"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# # If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable', None),
    'scipy': ('https://docs.scipy.org/doc/scipy', None),
    'matplotlib': ('https://matplotlib.org/stable', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
    'xarray': ('https://docs.xarray.dev/en/stable', None),
    'cartopy': ('https://scitools.org.uk/cartopy/docs/latest', None),
    'gdal': ('https://gdal.org/python', "objects_gdal.inv")
}

# -- Napoleon settings for docstring processing -------------------------------
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_special_with_doc = False
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    "scalar": ":term:`scalar`",
    "sequence": ":term:`sequence`",
    "callable": ":py:func:`callable`",
    "file-like": ":term:`file-like <file-like object>`",
    "array-like": ":term:`array-like <array_like>`",
    "Path": "~~pathlib.Path",
}

bibtex_bibfiles = ['refs.bib', 'refs_links.bib']
bibtex_encoding = 'latin'
# bibtex_cite_id = "cite-{key}"

# -- pybtex definitions for changing citation reference labels ----------------
from pybtex.style.formatting.unsrt import Style  # noqa
from pybtex.style.labels.alpha import LabelStyle, _strip_nonalnum  # noqa
from pybtex.plugin import register_plugin  # noqa


class WradlibLabelStyle(LabelStyle):

    # copy from AlphaStyle
    def format_label(self, entry):
        if entry.type == "book" or entry.type == "inbook":
            label = self.author_editor_key_label(entry)
        elif entry.type == "proceedings":
            label = self.editor_key_organization_label(entry)
        elif entry.type == "manual":
            label = self.author_key_organization_label(entry)
        else:
            label = self.author_key_label(entry)
        # add full year comma separated
        if "year" in entry.fields:
            return '{0}, {1}'.format(label, entry.fields["year"])
        else:
            return label

    def format_lab_names(self, persons):
        numnames = len(persons)
        person = persons[0]
        result = _strip_nonalnum(person.prelast_names +
                                 person.last_names)
        if numnames > 1:
            result += " et al."
        return result


class WradlibStyle(Style):
    default_label_style = 'wrl'


register_plugin('pybtex.style.labels', 'wrl', WradlibLabelStyle)
register_plugin('pybtex.style.formatting', 'wrlstyle', WradlibStyle)

# get version
version_tuple = wradlib.version.version_tuple

# is release
if len(version_tuple) == 3:
    gh_tree_name = f"v{wradlib.version.version}"
else:
    # extract git revision
    gh_tree_name = version_tuple[-1].split(".")[0][1:]

try:
    nb = ('`{0} <{1}/wradlib-notebooks/tree/{2}>`__'.format(nb[0:7], url, nb))
except NameError:
    nb = 'Missing'

docs = ('`{0} <{1}/wradlib-docs/tree/{2}>`__'.format(docs[0:7], url, docs))

rel = ('`{0} <{1}/wradlib/tree/{2}>`__'.format(release, url, gh_tree_name))

rst_epilog = ""
rst_epilog += f"""
.. |release-link| replace:: {rel}
.. |notebooks-link| replace:: {nb}
.. |docs-link| replace:: {docs}
"""
