# in_house_plotting

Automated plotting script for results of AutoDock-GPU_for_ZINC

`Link` *[AutoDock-GPU_for_ZINC](https://github.com/jongseo-park/AutoDock-GPU_for_ZINC)*

<br>

* required packages
`numpy`
`pandas`
`matplotlib`
`seaborn`


- - -

## Required 'result' directory
```
mkdir ./result
```

<br>

## scatter plot
```
python3 inhouseplot.py --input1 ./datasets/testset.csv --xn Mwt --yn PSA --x Mwt --y PSA --scatter y
```

<br>

## Corr matrix
```
python3 inhouseplot.py --input1 ./datasets/testset.csv --corr y --factors Lowest_E Mwt 'Rotatable bonds' PSA
```

<br>

## etc
```
python3 inhouseplot.py --input1 ./datasets/testset.csv --hist y --x QED_mean
```

- - -

## arguments

#### for corr
required: `--input1` `--factors`

```
--factors A B C 'A and B' 'D or E' F
```

#### for hist
required: `--input1` `--x`
optional: `--xn` `--yn` `--title` `--color` `--label` `--fontsize` `--alpha`
(alpha: transparency, 0 ~ 1)

#### for scatter
... 