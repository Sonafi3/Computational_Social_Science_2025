import pandas as pd

file_names = [
    'RS_2018-09_subs_filtered.csv',
    'RS_2021-09_subs_filtered.csv',
    'RS_2023-05_subs_filtered.csv',
    'RS_2023-10_subs_filtered.csv',
    'RS_2024-09_subs_filtered.csv',
    'RC_2018-09_subs_filtered.csv',
    'RC_2021-09_subs_filtered.csv',
    'RC_2023-05_subs_filtered.csv',
    'RC_2023-10_subs_filtered.csv',
    'RC_2024-09_subs_filtered.csv'
]

total_type_counts = pd.Series(dtype='int64')

for file in file_names:
    try:
        print(f"Analyzing the file: {file}...")
        
        df = pd.read_csv(file, low_memory=False) 
        
        type_counts = df.dtypes.value_counts()
        
        total_type_counts = total_type_counts.add(type_counts, fill_value=0)
        
    except FileNotFoundError:
        print(f"File '{file}' was not found")
    except Exception as e:
        print(f"Error while working with file '{file}': {e}")

print("\n" + "="*40)
print("General overview of data type frequency:")
print("="*40)
print(total_type_counts.astype(int))