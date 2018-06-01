from IPython.display import HTML
import matplotlib.pyplot as plt

menon_farger = {"Bl\u00e5": [0.22265625, 0.33984375, 0.45703125],
                "Oransje": [0.83984375, 0.49609375, 0.0859375],
                "M\u00f8rk gr\u00e5": [0.44921875, 0.48046875, 0.5078125],
                "Gr\u00e5": [0.671875, 0.69921875, 0.71875],
                "Gr\u00f8nn": [0.6484375, 0.69921875, 0.25],
                "M\u00f8rk r\u00f8d": [0.578125, 0.06640625, 0.0]
                }

headings = """
<style>
html {
  font-size: 62.5% !important;
}
table.dataframe {
    border-collapse: collapse;
    border: none;
}
table.dataframe tr {
    border: none;
}
table.dataframe td, table.dataframe th {
    margin: 0;
    border: 1px solid white;
    padding-left: 0.25em;
    padding-right: 0.25em;
}
table.dataframe th:not(:empty) {
    text-align: left;
    font-weight: normal;
}
table.dataframe tr:nth-child(2) th:empty {
    border-left: none;
    border-right: 1px dashed #888;
}
table.dataframe td {
    border: 2px solid #ccf;
}
tr:nth-child(2) tr:hover {
  background: yellow;
}

div.text_cell_render {
    font-family: Calibri, sans-serif !important;
    font-size: 10pt;
}
.text_cell.rendered h1, h2, h3, h4 {
  font-family: Calibri, sans-serif !important;
	margin-top: 0 !important;
  margin-bottom: 2rem !important;
  font-weight: bold !important; }
.text_cell.rendered h1 {
  font-size: 30pt;
}
.text_cell.rendered h2 {
	font-size: 24pt;
  color: rgb(57,87,117);
}
.text_cell.rendered h3 {
	font-size: 20pt;
  color: rgb(214,127,22);
}
.text_cell.rendered h4 {
	font-size: 14pt;
  color: rgb(57,87,117);
}
</style>
"""

logo = """
<style>
h1:after {
    content: url('https://www.menon.no/wp-content/uploads/2017logo@2x.png');
    float: right;
}
</style>
"""



def menon_headings():
    """
    Applies Menon colors and numbering to headings in Jupyter notebooks
    """
    return HTML(headings)


def menon_logo():
    """
    Adds the Menon logo to the top header (h1) in Jupyter notebooks
    """
    return HTML(logo)


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
    css_styles = headings + '\n' + logo
    return HTML(css_styles)


if __name__ == '__main__':
    menon_styles()
