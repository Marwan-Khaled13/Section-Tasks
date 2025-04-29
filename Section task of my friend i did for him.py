import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\snake\Desktop\student_habits_performance_cleaned.csv')

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
plt.subplots_adjust(hspace=0.3, wspace=0.3)
sns.set_style('whitegrid')

# Chart 1: Pie chart of Gender Distribution
gender_counts = df['gender'].value_counts()
axes[0,0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
axes[0,0].set_title('Gender Distribution')

# Chart 2: Histogram of Study Hours per Day
sns.histplot(df['study_hours_per_day'], bins=30, kde=True, ax=axes[0,1])
axes[0,1].set_title('Study Hours per Day Distribution')
axes[0,1].set_xlabel('Study Hours')
axes[0,1].set_ylabel('Count')

# Chart 3: Pie chart of Part-time Job Status
job_counts = df['part_time_job'].value_counts()
axes[0,2].pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=90)
axes[0,2].set_title('Part-time Job Distribution')

# Chart 4: Box plot of Exam Score by Diet Quality
sns.boxplot(x='diet_quality', y='exam_score', data=df, ax=axes[1,0])
axes[1,0].set_title('Exam Score by Diet Quality')
axes[1,0].set_xlabel('Diet Quality')
axes[1,0].set_ylabel('Exam Score')

# Chart 5: Violin plot of Sleep Hours by Gender
sns.violinplot(x='gender', y='sleep_hours', data=df, split=True, ax=axes[1,1])
axes[1,1].set_title('Sleep Hours by Gender')
axes[1,1].set_xlabel('Gender')
axes[1,1].set_ylabel('Sleep Hours')

# Chart 6: Scatter plot of Social Media Hours vs Exam Score colored by Internet Quality
sns.scatterplot(x='social_media_hours', y='exam_score', hue='internet_quality', palette='deep', data=df, ax=axes[1,2])
axes[1,2].set_title('Social Media Use vs Exam Score')
axes[1,2].set_xlabel('Social Media Hours')
axes[1,2].set_ylabel('Exam Score')

plt.show()
