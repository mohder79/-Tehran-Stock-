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





import pandas as pd

# Create example dataframe
df = pd.DataFrame({
    'Symbol_id': ['dgdfg', 'gfdfg', 'gfsgsg'],
    'Name': ['sgfsfg', 'فخوز', 'sgfsg'],
    'Sell_No': ['dgtdfg', 'gfjdfg', 'gfsgesg']
})

def symbol_info(name):
    filtered_rows = df[df['Name'] == name]

    if not filtered_rows.empty:
        row = filtered_rows.iloc[0]
        print(f"Symbol_id: {row['Symbol_id']}, Name: {row['Name']}, Sell_No: {row['Sell_No']}")
    else:
        print(f"No rows found with name = {name}")

symbol_info('فخوز')