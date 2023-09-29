import pandas as pd

# creating a dataframe

data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["New York", "los Angeles", "Chicago"]
}

df = pd.DataFrame(data_dict)

# Selcting a single column
ages = df["Age"]
print("Ages\n", ages)

# selecting multiple columns
subset = df[["Name", "City"]]
print("subset:\n", subset)

# filtering based on a condition
adults = df[df["Age"] >= 18]
print("Adults:\n", adults)

# grouping by a column and calculating mean age
grouped = df.groupby("City")["Age"].mean()
print("mean age by city:\n", grouped)

# Sorting the dataframe by age in descending ordeer
sorted_df = df.sort_values(by="Age", ascending=False)
print("sorted Dataframe:\n", sorted_df)

# Adding a new column
df["Gender"] = ["Female", "Male", "Male"]
print("Dataframe with Gender:\n", df)

#removing a column
df.drop(columns=["Gender"], inplace=True)
print("Dataframe after removng gender:\n", df)

#applying a custom function to the age column
def classify_age(age):
    if age <25:
        return "Young"
    elif age >= 25 and age < 40:
        return "Adult"
    else:
         return "senior"

df["Age_Category"] = df["Age"].apply(classify_age())
print("Dataframe with Age Categories\n", df)

