from IPython.display import HTML
import matplotlib.pyplot as plt
import collections
from pathlib import Path


def menon_headings():
    HTML(Path('menon_headings.css').read_text().decode('utf-8'))


def menon_logo():
    HTML(Path('menon_logo.css').read_text().decode('utf-8'))


def menon_matplotlib():
    import json
    from cycler import cycler
    menon_farger = json.load(Path('menon_farger.json').read_text(),
                             object_pairs_hook=collections.OrderedDict)
    plt.style.use('bmh')
    plt.rcParams['axes.prop_cycle'] = cycler(
        color=[color for _, color in menon_farger.items()])


def menon_styles():
    menon_headings()
    menon_logo()
    menon_matplotlib()
