from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class histplot:

    def __init__(self, input1, x, xn, yn, title, color, label, fontsize, alpha):

        self.input1 = input1
        self.x = x
        self.xn = xn
        self.yn = yn
        self.title = title
        self.color = color
        self.label = label
        self.fontsize = fontsize
        self.alpha = alpha


    def histplot(self, xcu, xcl):
        
        xcu = float(xcu)
        xcl = float(xcl)

        filename = 'histplot'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()
        

        dt1 = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]

        ax.hist(dt1, bins=20, histtype='bar', rwidth=0.8, alpha=self.alpha, label=self.label, edgecolor='black', lw=0.7, color=self.color)
        # ax.hist(dt1, bins=20, histtype='bar', rwidth=0.8, alpha=0.8, edgecolor='black', lw=0.7, color=self.color)

        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        ax.legend(fontsize=self.fontsize)
        # plt.xticks([-10, -8, -6, -4, -2, 0], fontsize=15)
        # plt.xticks([-11.0, -10.5, -10.0, -9.5, -9.0], fontsize=15)
        plt.xticks(fontsize=self.fontsize)
        plt.yticks(fontsize=self.fontsize)

        fig.savefig(f'./result/hist_{filename}.png', bbox_inches='tight', dpi=300, transparent=True)



    def histplot_range(self, xcu, xcl, xr, yr):

        xcu = float(xcu)
        filename = 'histplot'

        df1 = pd.read_csv (self.input1)
        fig, ax = plt.subplots()
        

        dt1 = df1[(df1[self.x] <= xcu) & (df1[self.x] >= xcl)][self.x]

        ax.hist(dt1, bins=20, histtype='bar', rwidth=0.8, alpha=self.alpha, label=self.label, edgecolor='black', lw=0.7, color=self.color)
        # ax.hist(dt1, bins=20, histtype='bar', rwidth=0.8, alpha=0.8, edgecolor='black', lw=0.7, color=self.color)

        ax.set_title(self.title)
        ax.set_xlabel(self.xn, size=self.fontsize)
        ax.set_ylabel(self.yn, size=self.fontsize)
        ax.legend(fontsize=self.fontsize)
        plt.xticks(xr, fontsize=self.fontsize)
        plt.yticks(yr, fontsize=self.fontsize)

        fig.savefig(f'./result/hist_{filename}_range.png', bbox_inches='tight', dpi=300, transparent=True)
