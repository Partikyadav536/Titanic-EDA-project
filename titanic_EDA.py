
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv('titanic_dataset.csv')

# -----------------------------
# Sex vs Survived
# -----------------------------
survival_by_sex = df.groupby('Sex')['Survived'].mean()
print(survival_by_sex)

colors = ['#7A9E9F', '#2F4B7C']

plt.figure(figsize=(7,4))
plot = plt.bar(
    survival_by_sex.index,
    survival_by_sex.values,
    color = colors,
    edgecolor = 'black'
    )
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Survived')
for i, v in enumerate(survival_by_sex.values):
    plt.text(i, v + 0.02, f"{v*100:.0f}%", ha='center')
plt.tight_layout()
plt.show()
# Insight:
# Gender remains the dominant factor, especially among adults where survival differences are significant.


# -----------------------------
# Age vs Survived
# -----------------------------
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
df['Age_Group'] = pd.cut(
df['Age'],
    bins = [0,12,60,100],
    labels = ['Child','Adult','Elderly']
)
print(df.groupby(['Age_Group','Sex'], observed = True)['Survived'].mean(),'\n')
# Insight:
# Children have higher rates of survival.
#Gender is still a prominent feature, especially among adults.

# -----------------------------
# Passenger Class vs Survived
# -----------------------------
print(df.groupby(['Pclass','Sex'], observed = True)['Survived'].mean())
# Insight:
# Passenger class strongly affects survival.
# Higher-class passengers have better survival rates.
# The effect is more pronounced among males, while females maintain relatively high survival across all classes.

# -----------------------------
# Fare vs Survived
# -----------------------------
df['Fare_cat'] = pd.qcut(
    df['Fare'],
    q = 3,
    labels = ['Low','Medium','High']
)
print(df.groupby(['Fare_cat','Sex'], observed = True)['Survived'].mean())
# Insight:
# Higher fare passengers tend to survive more,
# but this is strongly linked to passenger class.

# -----------------------------
# Family Size vs Survived
# -----------------------------
df['Famsize'] = df['SibSp'] + df['Parch']

print(df.groupby('Famsize')['Survived'].mean())
# Insight:
# Survival is highest for small-medium size families (1–3 members).
# Large families show lower survival rates.
# Extreme values may be unreliable due to small sample size.