dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4,
              'e': 5}

dictionary.keys()
dictionary.values()
dictionary.items()

{v ** 2 for v in dictionary.values()}


numbers = range(10)

new_dict = {}

{n: n ** 2 for n in numbers if n % 2 == 0}



import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = [col.upper() for col in df.columns]

['FLAG'+col  if 'INS' in col else 'NO_FLAG_'+col for col in df.columns]


df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
#data tipi "Object" olmayan değişkenkeri yani sayısal değişkenleri getir dedik

soz = {}
agg_list = ["mean", "min", "max", "sum"]


#kısayol
{col: agg_list for col in num_cols}

#uzunyol
for col in num_cols:
    soz[col] = agg_list






