import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Level 3\Dataset.csv"
df = pd.read_csv(file_path)

# Select relevant columns and clean data
df_votes = df[['Restaurant Name', 'Votes', 'Aggregate rating']].dropna()
df_votes['Votes'] = pd.to_numeric(df_votes['Votes'], errors='coerce')
df_votes = df_votes.dropna(subset=['Votes'])

# restaurant with highest and lowest votes
max_votes = df_votes.loc[df_votes['Votes'].idxmax()]
min_votes = df_votes.loc[df_votes['Votes'].idxmin()]

print("Restaurant with Highest Votes:")
print(max_votes, "\n")

print("Restaurant with Lowest Votes:")
print(min_votes, "\n")

correlation = df_votes['Votes'].corr(df_votes['Aggregate rating'])
print(f"Correlation between Votes and Aggregate Rating: {correlation:.2f}\n")

# Histogram of votes
plt.figure(figsize=(10, 6))
sns.histplot(df_votes['Votes'], bins=30, kde=True, color='teal')
plt.title("Distribution of Votes")
plt.xlabel("Number of Votes")
plt.ylabel("Number of Restaurants")
plt.grid(True)
plt.tight_layout()
plt.show()
