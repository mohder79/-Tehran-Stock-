import pandas as pd
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16],
    'E': [17, 18, 19, 20]
}
df = pd.DataFrame(data)

# select the first 23 columns of the dataframe
subset = df.iloc[:,:2]
print(subset)