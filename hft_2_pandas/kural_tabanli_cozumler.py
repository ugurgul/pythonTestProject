

######################################################################
#GÖREV 1
######################################################################

#1
import pandas as pd
df = pd.read_csv("../datasets/persona.csv")

df.info

#2
df["SOURCE"].nunique()

df["SOURCE"].value_counts()

#3
df["PRICE"].nunique()

#4
df["PRICE"].value_counts()

#5
df["COUNTRY"].value_counts()

#6
df.groupby("COUNTRY")["PRICE"].sum()

#7
df["SOURCE"].value_counts()

#8
df.groupby("COUNTRY")["PRICE"].mean()

#9
df.groupby("SOURCE")["PRICE"].mean()

#10
df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()

######################################################################
#GÖREV 2
######################################################################
new_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()

######################################################################
#GÖREV 3
######################################################################
agg_df = new_df.reset_index().sort_values('PRICE', ascending=False)

######################################################################
#GÖREV 4
######################################################################
agg_df.reset_index()

######################################################################
#GÖREV 5
######################################################################
age_bins = [0, 18, 23, 30, 40, 70]
age_labels = ['0_18', '19_23', '24_30', '31_40', '41_70']
agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=age_bins, labels=age_labels, right=False)
agg_df.head()

######################################################################
#GÖREV 6
######################################################################
# Önce 'AGE_CAT' sütununu string tipine dönüştürüyoruz
agg_df['AGE_CAT'] = agg_df['AGE_CAT'].astype(str)

# Daha sonra 'customers_level_based' sütununu oluşturuyoruz
agg_df['customers_level_based'] = agg_df['COUNTRY'].str.upper() + "_" + \
                              agg_df['SOURCE'].str.upper() + "_" + \
                              agg_df['SEX'].str.upper() + "_" + \
                              agg_df['AGE_CAT']

agg_df.head()

######################################################################
#GÖREV 7
######################################################################
agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, labels=["D", "C", "B", "A"])

agg_df.groupby('SEGMENT')['PRICE'].agg(['mean', 'max', 'sum'])


######################################################################
#GÖREV 8
######################################################################
new_user = "TUR_ANDROID_FEMALE_31_40"
customer_segment = agg_df.loc[agg_df['customers_level_based'] == new_user]
customer_segment["PRICE"].mean()

new_user_fra = "FRA_IOS_FEMALE_31_40"
customer_fra = agg_df.loc[agg_df["customers_level_based"] == new_user_fra]
customer_fra["PRICE"].mean()






