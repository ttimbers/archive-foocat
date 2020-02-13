from foocat import __version__
import pytest
import pandas as pd
from foocat import cat

def test_version():
    assert __version__ == '0.1.0'
    
def test_catbind():
  a = pd.Categorical(["character", "hits", "your", "eyeballs"])
  b = pd.Categorical(["but", "integer", "where it", "counts"])
  assert ((cat.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
  assert ((cat.catbind(a, b)).categories == ["but", "character", "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()
