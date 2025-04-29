import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'file_path/titanic.csv')

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
plt.subplots_adjust(hspace=0.3, wspace=0.3)
sns.set_style('whitegrid')

# Chart 1: Pie chart of Survival
survived_counts = df['Survived'].value_counts()
axes[0,0].pie(survived_counts, labels=['Did not survive', 'Survived'], autopct='%1.1f%%', startangle=90)
axes[0,0].set_title('Survival Distribution')

# Chart 2: Histogram of Age
sns.histplot(df['Age'], bins=30, kde=True, ax=axes[0,1])
axes[0,1].set_title('Age Distribution')
axes[0,1].set_xlabel('Age')
axes[0,1].set_ylabel('Count')

# Chart 3: Pie chart of Gender Distribution
gender_counts = df['Sex'].value_counts()
axes[0,2].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
axes[0,2].set_title('Gender Distribution')

# Chart 4: Box plot of Fare by Class
sns.boxplot(x='Pclass', y='Fare', data=df, ax=axes[1,0])
axes[1,0].set_title('Fare by Passenger Class')
axes[1,0].set_xlabel('Passenger Class')
axes[1,0].set_ylabel('Fare')

# Chart 5: Violin plot of Age by Survival
sns.violinplot(x='Survived', y='Age', data=df, split=True, ax=axes[1,1])
axes[1,1].set_title('Age Distribution by Survival')
axes[1,1].set_xlabel('Survived')
axes[1,1].set_ylabel('Age')

# Chart 6: Scatter plot Age vs Fare colored by Pclass
sns.scatterplot(x='Age', y='Fare', hue='Pclass', palette='deep', data=df, ax=axes[1,2])
axes[1,2].set_title('Age vs Fare Colored by Class')
axes[1,2].set_xlabel('Age')
axes[1,2].set_ylabel('Fare')

# Show the dashboard
plt.show()
