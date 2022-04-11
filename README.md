
#  STEP 
---
# 1. Installation of Sphinx

```
$ pip install Sphinx
```

## 2. Making a 'Docs' folder

```
$ sphinx-quickstart
```

If you are inputting above command, you might meet below screens. Just set as u want.
![image](https://user-images.githubusercontent.com/71545160/162664384-30c275e8-48a6-4b6c-81d2-44d1c9d24c0a.png)


## 3.  Modify 'conf.py' file

```python
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [    'sphinx.ext.autodoc',
                    'sphinx.ext.todo',
                    'sphinx.ext.mathjax',
                    'sphinx.ext.githubpages',
                  'recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The master toctree document.
master_doc = 'index'
source_suffix = ['.rst', '.md']
source_parsers = {
  '.md': CommonMarkParser,
}
```

## 4. Making 'html' file

```
$ make html
```
![image](https://user-images.githubusercontent.com/71545160/162605763-e36c96b0-4d98-4973-b9ec-0d4710d757fd.png)

## 5. Results

![image](https://user-images.githubusercontent.com/71545160/162605779-83f62a32-f202-4b7a-bbdb-2f2b6a484242.png)

![image](https://user-images.githubusercontent.com/71545160/162605783-51ea6f53-0e9c-4a4e-957d-eb666aed061e.png)
