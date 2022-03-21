from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

from tools import corr_plot
from tools import hist_plot
from tools import scatter_plot
from tools import multihist_plot
from tools import hist_overlap_plot

# General arguments
parser = argparse.ArgumentParser (description='Basic tool for plotting of our lab')

parser.add_argument("--input1", required=True, help='Input data 1')
parser.add_argument("--input2", required=False, help='Input data 2')
parser.add_argument("--xn", required=False, default='x-axis', help='Name of the x-axis')
parser.add_argument("--yn", required=False, default='y-axis', help='Name of the y-axis')
parser.add_argument("--title", required=False, default='title', help='Title')
parser.add_argument("--fontsize", required=False, default='12', help='Fontsize')
parser.add_argument("--color", required=False, default='orange', help='Color')
parser.add_argument("--color2", required=False, default='skyblue', help='Color 2')
parser.add_argument("--label", required=False, default='label_1', help='Label')
parser.add_argument("--label2", required=False, default='label_2', help='Label 2')
parser.add_argument("--alpha", required=False, type=float, default=0.8, help='Transparency')
parser.add_argument("--xr", required=False, type=int, nargs='+', default=[-10, -5, 0, 5, 10], help='x_range')
parser.add_argument("--yr", required=False, type=int, nargs='+', default=[0], help='y_range')

parser.add_argument("--factors", required=False, type=str, nargs='+', default=0, help='factors for corr')
 
parser.add_argument("--x", required=False, default=0, help='x_data')
parser.add_argument("--y", required=False, default=0, help='x_data')
parser.add_argument("--xcu", required=False, type=float, default=99999999, help='x_axis upper cutoff')
parser.add_argument("--xcl", required=False, type=float, default=-99999999, help='x_axis lower cutoff')
parser.add_argument("--ycu", required=False, type=float, default=99999999, help='y_axis upper cutoff')
parser.add_argument("--ycl", required=False, type=float, default=-99999999, help='y_axis lower cutoff')

parser.add_argument("--ncl", required=False, type=int, default=4, help='Number of columns')
parser.add_argument("--nrw", required=False, type=int, default=2, help='Number of rows')

# Plot selection
parser.add_argument("--corr", required=False, help='correlation plot')
parser.add_argument("--hist", required=False, help='histogram plot')
parser.add_argument("--multihist", required=False, help='multiple histogram plot')
parser.add_argument("--scatter", required=False, help='scatter plot')
parser.add_argument("--overlaphist", required=False, help='Overlapped histogram plot')


args = parser.parse_args()


# factor = ['Lowest_E', 'PSA', 'Mwt']

if __name__ == '__main__':
    if args.corr == 'y':
        pl = corr_plot.corrplot(args.input1, args.factors)
        pl.corrplot()
        pl.corrplotlabel()

    if args.hist == 'y':
        pl = hist_plot.histplot(args.input1, args.x, args.xn, args.yn, args.title, args.color, args.label, args.fontsize, args.alpha)
        pl.histplot(args.xcu, args.xcl)
        pl.histplot_range(args.xcu, args.xcl, args.xr, args.yr)

    if args.scatter == 'y':
        pl = scatter_plot.scatterplot(args.input1, args.x, args.y, args.xn, args.yn, args.title, args.color, args.fontsize, args.alpha)
        pl.fancyscatterplot(args.xcu, args.xcl, args.ycu, args.ycl)
        pl.fancyscatterplot_range(args.xcu, args.xcl, args.ycu, args.ycl, args.xr, args.yr)
        pl.scatterplot(args.xcu, args.xcl, args.ycu, args.ycl)
        pl.scatterplot_range(args.xcu, args.xcl, args.ycu, args.ycl, args.xr, args.yr)

    if args.multihist == 'y':
        pl = multihist_plot.multihistplot(args.input1, args.factors, args.xn, args.yn, args.title, args.color, args.label, args.fontsize, args.ncl, args.nrw, args.alpha)
        pl.multihistplot(args.x, args.xcu, args.xcl)

    if args.overlaphist == 'y':
        pl = hist_overlap_plot.histoverplot(args.input1, args.input2, args.x, args.xn, args.yn, args.title, args.color, args.color2, args.label, args.label2, args.fontsize, args.alpha)
        pl.histoverplot(args.xcu, args.xcl)
        pl.histoverplot_range(args.xcu, args.xcl, args.xr, args.yr)
