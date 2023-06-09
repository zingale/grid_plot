#__all__ = ['grid_plot']

import matplotlib as mpl

# Use LaTeX for rendering
mpl.rcParams["text.usetex"] = True
# load the xfrac package
mpl.rcParams["text.latex.preamble"] += r"""
\usepackage{xfrac}
\newcommand{\myhalf}{\sfrac{1}{2}}
\newcommand{\mythreehalf}{\sfrac{3}{2}}
\newcommand{\myfivehalf}{\sfrac{5}{2}}
"""
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'

# font sizes
mpl.rcParams['font.size'] = 12
mpl.rcParams['legend.fontsize'] = 'large'
mpl.rcParams['figure.titlesize'] = 'medium'

from .grid_1d import (CellCentered, FDGrid, FVGrid, PiecewiseConstant,
                      PiecewiseLinear, PiecewiseParabolic)
from .grid_2d import FDGrid2d, FVGrid2d, Grid2d
