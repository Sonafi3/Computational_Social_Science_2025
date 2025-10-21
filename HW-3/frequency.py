import pandas as pd

file_names = [
    'FINAL_CommentsV2_2018-09.csv',
    'FINAL_CommentsV2_2021-09.csv',
    'FINAL_CommentsV2_2023-05.csv',
    'FINAL_SubmissionsV2_2018-09.csv',
    'FINAL_SubmissionsV2_2021-09.csv',
    'FINAL_SubmissionsV2_2023-05.csv'
]

total_type_counts = pd.Series(dtype='int64')

for file in file_names:
    try:
        print(f"Аналізую файл: {file}...")
        
        df = pd.read_csv(file, low_memory=False) 
        
        type_counts = df.dtypes.value_counts()
        
        total_type_counts = total_type_counts.add(type_counts, fill_value=0)
        
    except FileNotFoundError:
        print(f"Файл '{file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при обробці файлу '{file}': {e}")

print("\n" + "="*40)
print("Загальний огляд частоти типів даних:")
print("="*40)
print(total_type_counts.astype(int))