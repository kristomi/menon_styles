from IPython.display import HTML
import matplotlib.pyplot as plt
import collections
import json
from pathlib import Path
import os
import sys

curr_path = Path(os.path.realpath(__file__)).parent

farge_path = curr_path / 'menon_farger.json'
menon_farger = json.loads(farge_path.read_text(),
                          object_pairs_hook=collections.OrderedDict)


def menon_headings():
    """
    Applies Menon colors and numbering to headings in Jupyter notebooks
    """
    return HTML((curr_path / 'menon_headings.css').read_text())


def menon_logo():
    """
    Adds the Menon logo to the top header (h1) in Jupyter notebooks
    """
    return HTML((curr_path / 'menon_logo.css').read_text())


def menon_matplotlib():
    """
    Sets the Menon colors as the default color scheme in matplotlib
    """
    from cycler import cycler
    plt.style.use('bmh')
    plt.rcParams['axes.prop_cycle'] = cycler(
        color=[color for _, color in menon_farger.items()])


def menon_styles():
    """
    Applies Menon colors and numberings to headings in Jupyter notebooks,
    and adds the Menon logo to the top header (h1).
    Also sets the Menon colors to the default color scheme in Matplotlib.
    """
    menon_matplotlib()
    css_styles = ((curr_path / 'menon_logo.css').read_text()
                  + '\n'
                  + (curr_path / 'menon_headings.css').read_text()
                  )
    return HTML(css_styles)
