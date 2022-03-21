from pandas.plotting import scatter_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class corrplot:

    def __init__(self, input1, factors):

        self.input1 = input1
        self.factors = factors

    def corrplot(self):

        df1 = pd.read_csv (self.input1)

        fig, ax = plt.subplots()
        filename = 'corrplot'
        cmap = sns.diverging_palette(20, 220, n=200)

        df = df1[self.factors]

        corr = df.corr()

        sns.set(font_scale=0.7)
        sns.heatmap(corr, cmap=cmap, vmin=-1, vmax=1, square=True, cbar_kws={'shrink': 0.5})

        ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        fontsize=11, 
        horizontalalignment='right'
        )

        ax.set_yticklabels(
        ax.get_yticklabels(),
        fontsize=11, 
        )

        plt.savefig(f'./result/{filename}.png', bbox_inches='tight', dpi=300, transparent=True) 


    def corrplotlabel(self):

        df1 = pd.read_csv (self.input1)

        fig, ax = plt.subplots()
        filename = 'corrplot'
        cmap = sns.diverging_palette(20, 220, n=200)

        df = df1[self.factors]

        corr = df.corr()

        sns.set(font_scale=0.7)
        sns.heatmap(corr, annot=True, cmap=cmap, vmin=-1, vmax=1, square=True, cbar_kws={'shrink': 0.5})

        ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        fontsize=11, 
        horizontalalignment='right'
        )

        ax.set_yticklabels(
        ax.get_yticklabels(),
        fontsize=11, 
        )

        plt.savefig(f'./result/{filename}_label.png', bbox_inches='tight', dpi=300, transparent=True) 