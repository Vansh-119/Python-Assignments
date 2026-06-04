import pandas as pd

dates = ['2026-01-01', '2026-02-15', '2026-03-20', '2026-04-10']

timeseries = pd.to_datetime(dates)

print("Time Series:")
print(timeseries)


df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Aman', 'Rahul', 'Priya', 'Neha']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Marks': [85, 90, 88, 95]
})

print("\nDataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)


inner_merge = pd.merge(df1, df2, on='ID', how='inner')

print("\nInner Merge:")
print(inner_merge)


left_join = pd.merge(df1, df2, on='ID', how='left')

print("\nLeft Join:")
print(left_join)




right_join = pd.merge(df1, df2, on='ID', how='right')

print("\nRight Join:")
print(right_join)


df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

index_join = df1_index.join(df2_index)

print("\nIndex-Based Join:")
print(index_join)


df3 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 70000]
})

df4 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'Finance'],
    'Bonus': [5000, 6000, 7000]
})

multiple_merge = pd.merge(df3, df4, on=['ID', 'Dept'], how='inner')

print("\nMerge with Multiple Keys:")
print(multiple_merge)


df5 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['Arjun', 'Karan']
})

df6 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Riya', 'Simran']
})

df7 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'City': ['Delhi', 'Mumbai', 'Pune', 'Jaipur']
})

concat_df = pd.concat([df5, df6], ignore_index=True)

print("\nConcatenated DataFrame:")
print(concat_df)


final_merge = pd.merge(concat_df, df7, on='ID')

print("\nMerged DataFrame:")
print(final_merge)


