
df['Age'] =df['Age'].fillna(median_age)
df['Age_Group'] = pd.cut(
df['Age'],
    bins = [0,12,60,100],
    labels = ['Child','Adult','Elderly']
)
print(df.groupby(['Age_Group',