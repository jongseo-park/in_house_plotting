from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class multihistplot:

    def __init__(self, input1, factors, xn, yn, title, color, label, fontsize, ncl, nrw, alpha):

        self.input1 = input1
        self.factors = factors
        self.xn = xn
        self.yn = yn
        self.title = title
        self.color = color
        self.label = label
        self.fontsize = fontsize
        self.ncl = ncl
        self.nrw = nrw
        self.alpha = alpha
        

    def multihistplot(self, x, xcu, xcl):
        
        filename = 'multihist'
        df1 = pd.read_csv(self.input1)
        
        fig, ax = plt.subplots(self.nrw, self.ncl, sharex=False, sharey=True, constrained_layout=True)
        for i in range(self.nrw):
            ax[i,0].set_ylabel(self.yn, size=11)

        if x == 0:
            dt1 = df1

        else:
            dt1 = df1[(df1[x] <= xcu) & (df1[x] >= xcl)]

        k = 0

        # for l in range(self.nrw)
        row = [i for i in range(self.nrw)]
        col = [i for i in range(self.ncl)]
        
        a = []
        for i in row:
            for j in col:
                array = [i, j]
                a.append(array)

        for arr, fac in zip(a, self.factors):
            
            dt2 = dt1[fac]
            n = arr[0]
            i = arr[1]

            ax[n, i].set_xlabel(fac, size=11)
            ax[n, i].hist(dt2, bins=15, histtype='bar', rwidth=0.8, alpha=self.alpha, label=j, edgecolor='black', lw=0.7, color=self.color)


        fig.savefig(f'./result/multihist_{filename}.png', bbox_inches='tight', dpi=300, transparent=True)