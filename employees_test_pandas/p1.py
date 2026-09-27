import pandas as pd
df1 = pd.DataFrame({
    "Nom": ["Ali", "Sara", "Ahmed"],
    "Age": [25, 28, 30],
    "Ville": ["Alger", "Sétif", "Oran"]
})

df2 = pd.DataFrame({
    "Nom": ["Lina", "Yacine", "Nour"],
    "Age": [22, 27, 29],
    "Ville": ["Constantine", "Annaba", "Batna"]
})
df3 = pd.concat([df1, df2], axis=1)
print(df3)
df = pd.DataFrame({
  
    "Date_Embauche": ["2022-01-15", "2023-06-20", "2024-03-10", "2001-05-10","2002-04_12"]
})


print(df)
import pandas as pd

data = {
   
    "Date_Embauche": [
        "2022-01-15",
        "2023-06-20",
        "2021-03-10",
        "2024-09-05",
        "2022-11-25"
    ]
}

df = pd.DataFrame(data)

# Convertir la colonne en date
df["Date_Embauche"] = pd.to_datetime(df["Date_Embauche"])

print(df)
dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(dict1)
print(df1)
df2=df1.head(3)
df2=df1.tail(3)
df2=df1.shape
df2=df1.info()
df2=df1.isnull().sum()
df2=df1.describe(include="all")
df3 = df1["Marks"].between(80, 90).sum()
df2=df1["Marks"].mean()
df2=df1["Marks"].max()
df2=df1["Marks"].min()
print(df2)
def df1_Marks(x):
    return x/2
df1=[]

print(df3)