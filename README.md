## `foocat`
Tiffany Timbers, 2020-02-18

*note - this is a toy Python package repo for UBC's [DSCI 524](https://github.com/UBC-MDS/DSCI_524_collab-sw-dev) Collaborative Software Development course*

Python package that eases the pain concatenating Pandas categoricals! 

![](https://github.com/ttimbers/foocat/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/ttimbers/foocat/branch/master/graph/badge.svg)](https://codecov.io/gh/ttimbers/foocat) ![Release](https://github.com/ttimbers/foocat/workflows/Release/badge.svg)

### Installation:

```
pip install -i https://test.pypi.org/simple/ foocat
```

### Dependencies

- Pandas

### Usage

```
>>> import pandas as pd
>>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
>>> b = pd.Categorical(["but", "integer", "where it", "counts"])
>>> cat.catbind(a, b)
```

```
[character, hits, your, eyeballs, but, integer, where it, counts]
Categories (8, object): [but, character, counts, eyeballs, hits, integer, where it, your]
```
