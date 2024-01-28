#1
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df.head()

#2
df["sex"].value_counts()

#3
df.columns.unique().value_counts()

#4
df["pclass"].nunique()

#5
df[["pclass", "parch"]].nunique()

#6????????????
type(df["embarked"])

#7
df.loc[[index for index, row in df.iterrows() if row['embarked'] == 'C']]

#8
df.loc[[index for index, row in df.iterrows() if row['embarked'] != 'S']]

#9
df.loc[(df["age"] < 30) & (df["sex"] == "female")]

#10
df.loc[(df["fare"] > 500) | (df["age"] > 70)]

#11
df.isnull().sum()

#12
df.drop("who", axis=1)

#13
df["deck"].fillna(df["deck"].mode()[0])

#14
df["age"].fillna(df["age"].median())

#15
df.groupby("survived").agg({"pclass": ["sum", "count", "mean"], "sex": ["count"]})

#16
def age_category(age):
    return 1 if age < 30 else 0

df["age_flag"] = df["age"].apply(lambda x: age_category(x))

print(df[['age', 'age_flag']])

#17
df_t = sns.load_dataset("tips")
df_t.head()

#18
df_t.groupby("time")["total_bill"].agg(["sum", "min", "max", "mean"])

#19
df_t.groupby(["day", "time"])["total_bill"].agg(["sum", "min", "max", "mean"])

#20
lunch_females = df_t[(df_t['time'] == 'Lunch') & (df_t['sex'] == 'Female')]
grouped = lunch_females.groupby('day')[['total_bill', 'tip']].agg(['sum', 'min', 'max', 'mean'])

#21
df_t.loc[(df_t["size"] < 3) & (df_t["total_bill"] > 10), "total_bill"].mean()

#22
df_t["total_bill_tip_sum"] = df_t["total_bill"] + df_t["tip"]

#23
siralama = df_t.sort_values(by="total_bill_tip_sum", ascending=False)

new_df = siralama.head(30)