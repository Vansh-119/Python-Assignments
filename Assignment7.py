import pandas as pd

print("1) PANDAS SERIES\n")

student_dict = {
    "Math": 85,
    "Science": 90,
    "English": 88
}

series_dict = pd.Series(student_dict)
print("Series from Dictionary:")
print(series_dict)

print("\n\n")

marks_list = [70, 80, 90, 100]

series_list = pd.Series(marks_list)
print("Series from List:")
print(series_list)

print("\n\n")

print("Access Elements:")
print("First Element:", series_list[0])
print("Second Element:", series_list[1])

print("\n\n")

print("2) DATAFRAMES\n")

data = [
    [1, "Rahul", 85],
    [2, "Aman", 90],
    [3, "Priya", 95]
]

df1 = pd.DataFrame(data, columns=["ID", "Name", "Marks"])

print("DataFrame from 2D List:")
print(df1)

print("\n\n")

dict_data = {
    "Name": ["Ravi", "Simran", "Karan"],
    "Age": [21, 22, 23]
}

df2 = pd.DataFrame(dict_data)

print("DataFrame from Dictionary:")
print(df2)

print("\n\n")

list_of_lists = [
    ["Laptop", 50000],
    ["Mobile", 20000],
    ["Tablet", 15000]
]

df3 = pd.DataFrame(list_of_lists, columns=["Product", "Price"])

print("DataFrame from List of Lists:")
print(df3)

print("\n\n")

list_of_tuples = [
    ("Amit", 101),
    ("Neha", 102),
    ("Rohit", 103)
]

df4 = pd.DataFrame(list_of_tuples, columns=["Name", "Roll No"])

print("DataFrame from List of Tuples:")
print(df4)

print("\n\n")

list_of_dicts = [
    {"Name": "Ankit", "City": "Delhi"},
    {"Name": "Pooja", "City": "Mumbai"},
    {"Name": "Suresh", "City": "Jaipur"}
]

df5 = pd.DataFrame(list_of_dicts)

print("DataFrame from List of Dicts:")
print(df5)

print("\n\n")

print("3) DATA ITERATION\n")

student_data = {
    "Name": ["Aman", "Riya", "Kunal", "Sneha"],
    "Marks": [75, 92, 60, 85],
    "City": ["Delhi", "Mumbai", "Pune", "Jaipur"]
}

df = pd.DataFrame(student_data)

print("Original DataFrame:")
print(df)

print("\n\n")

print("Iterating using iterrows():")
for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])

print("\n\n")

print("Students with Marks greater than 80:")
print(df[df["Marks"] > 80])

print("\n\n")

print("Select Second Row using iloc:")
print(df.iloc[1])

print("\n\n")

print("Selecting Name column of first 2 rows:")
print(df.loc[0:1, ["Name"]])

print("\n\n")

print("Dropping rows where Marks less than 70:")
df_new = df[df["Marks"] >= 70]
print(df_new)

print("\n\n")

new_row = pd.DataFrame({
    "Name": ["Arjun"],
    "Marks": [88],
    "City": ["Chennai"]
})

df_top = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)

print("DataFrame after inserting row:")
print(df_top)

print("\n\n")

print("Create list from rows:")
row_list = df.values.tolist()
print(row_list)