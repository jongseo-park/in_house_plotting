from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class scatterplot:

    def __init__(self, input1, x, y, xn, yn, title, color, fontsize, alpha):

        self.input1 = input1
        self.x = x
        self.y = y
        self.xn = xn
        self.yn = yn
        self.title = title
        self.color = color
        self.fontsize = fontsize
        self.alpha = alpha

    def fancyscatterplot(self, xcu, xcl, ycu, ycl):

        xcu = float(xcu)
        xcl = float(xcl)
        ycu = float(ycu)
        ycl = float(ycl)

        filename = 'scatter'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()

        X = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]
        Y = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.y]


        # plotting
        ax.scatter(X, Y, 80, '0.0', lw=1.0)
        ax.scatter(X, Y, 80, '1.0', lw=0)
        ax.scatter(X, Y, 80, color=self.color, lw=0, alpha=self.alpha)

        # setting
        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        plt.xticks(fontsize=self.fontsize)
        # plt.xticks([-11.0, -10.5, -10.0, -9.5, -9.0], fontsize=15)
        # plt.yticks([0, 1, 2, 3], fontsize=15)
        plt.yticks(fontsize=self.fontsize)

        fig.savefig(f'./result/fancy_scatter_{filename}.png', bbox_inches='tight', dpi=300, transparent=True)


    def fancyscatterplot_range(self, xcu, xcl, ycu, ycl, xr, yr):

        xcu = float(xcu)
        xcl = float(xcl)
        ycu = float(ycu)
        ycl = float(ycl)

        filename = 'scatter'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()

        X = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]
        Y = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.y]


        # plotting
        ax.scatter(X, Y, 80, '0.0', lw=1.0)
        ax.scatter(X, Y, 80, '1.0', lw=0)
        ax.scatter(X, Y, 80, color=self.color, lw=0, alpha=self.alpha)

        # setting
        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        
        plt.xticks(xr, fontsize=self.fontsize)
        plt.yticks(yr, fontsize=self.fontsize)

        fig.savefig(f'./result/fancy_scatter_{filename}_range.png', bbox_inches='tight', dpi=300, transparent=True)

    def scatterplot(self, xcu, xcl, ycu, ycl):

        xcu = float(xcu)
        xcl = float(xcl)
        ycu = float(ycu)
        ycl = float(ycl)

        filename = 'scatter'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()

        X = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]
        Y = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.y]


        # plotting
        # ax.scatter(X, Y, 80, '0.0', lw=1.0)
        # ax.scatter(X, Y, 80, '1.0', lw=0)
        ax.scatter(X, Y, 80, color=self.color, lw=0, alpha=self.alpha)

        # setting
        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        plt.xticks(fontsize=self.fontsize)
        # plt.xticks([-11.0, -10.5, -10.0, -9.5, -9.0], fontsize=15)
        # plt.yticks([0, 1, 2, 3], fontsize=15)
        plt.yticks(fontsize=self.fontsize)

        fig.savefig(f'./result/scatter_{filename}.png', bbox_inches='tight', dpi=300, transparent=True)


    def scatterplot_range(self, xcu, xcl, ycu, ycl, xr, yr):

        xcu = float(xcu)
        xcl = float(xcl)
        ycu = float(ycu)
        ycl = float(ycl)

        filename = 'scatter'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()

        X = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]
        Y = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.y]


        # plotting
        # ax.scatter(X, Y, 80, '0.0', lw=1.0)
        # ax.scatter(X, Y, 80, '1.0', lw=0)
        ax.scatter(X, Y, 80, color=self.color, lw=0, alpha=self.alpha)

        # setting
        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        
        plt.xticks(xr, fontsize=self.fontsize)
        plt.yticks(yr, fontsize=self.fontsize)

        fig.savefig(f'./result/scatter_{filename}_range.png', bbox_inches='tight', dpi=300, transparent=True)