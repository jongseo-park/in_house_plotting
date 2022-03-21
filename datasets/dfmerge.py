import pandas as pd

import argparse

parser = argparse.ArgumentParser (description='Basic tool for data plotting in GISTXRAY Matplotlib')
parser.add_argument("--input1", required=True, help='Input data 1')
parser.add_argument("--input2", required=True, help='Input data 2')
parser.add_argument("--output", required=False, default='./output.csv', help='Input data 2')
args = parser.parse_args()



if __name__ == '__main__':
    df1 = pd.read_csv(args.input1)
    df2 = pd.read_csv(args.input2)

    pd.concat([df1, df2]).reset_index(drop=True).to_csv(args.output)