import pandas as pd

df=pd.read_csv("organizations-100.csv", encoding="latin1")

#Data Ingestion
print("First Five Rows:")
print(df.head())

print("\nShape of the Dataset:")
print(df.shape)

print("\nInformation about the Dataset:")
print(df.info())

#Deduplication
dup=df.duplicated().sum()
print("\nThe no. of Duplicate values are:", dup)

df=df.drop_duplicates()
print("\nTotal Duplicates after removal:", df.duplicated().sum())

#Column Management and Format Standardization
print("\noriginal column names:")
print(df.columns)

df=df.rename(columns={'Founded':'Year founded'})

df.columns=df.columns.str.lower().str.replace(" ","_")
print("\nafter cleaning column names:")
print(df.columns)

#Handling Missing Values
missing_val=df.isnull().sum()
print("\nTotal no. of Missing Values per column:")
print(missing_val) # no missing values present

#practice
print("\noriginal index order")
print(df.info())
print(df.columns.to_list())
df=df[

       ['index', 'organization_id', 'name', 'website', 'country', 'year_founded', 'description', 'industry', 'number_of_employees']
]
print(df.info())
print(df.head())

df.to_csv("Organizations-100_cleaned.csv", index=False)
