import pandas as pd

def catbind(a, b):
  concatenated = pd.concat([pd.Series(a.astype("string")), pd.Series(b.astype("string"))])
  return pd.Categorical(concatenated)
