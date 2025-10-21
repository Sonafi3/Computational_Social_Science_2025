import pandas as pd

file_name = "FINAL_Comments_2023-05.csv" 

try:
    df = pd.read_csv(file_name)
    
    print("Dataset successfully loaded. Here are the first 5 rows:")
    print(df.head()) 

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
