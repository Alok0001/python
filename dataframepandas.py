#creating a dataframe from a dictionary
import pandas as pd

data_dict = {
    "Name": ["Alice", "Bob", "charlie"],
    "age":[25, 30, 22]
}

df = pd.DataFrame(data_dict)
print(df)

#selecting a single column
ages =df["age"]
print(ages)

#selecting multiple columns
subset = df[["Name", "age"]]
print(subset)
