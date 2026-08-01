import pandas as pd
df = pd.DataFrame({'Name':['Alice','Bob','Alice']})
df = df.drop_duplicates()