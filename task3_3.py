import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Level 3\Dataset.csv"
df = pd.read_csv(file_path)

df_service = df[['Price range', 'Has Online delivery', 'Has Table booking']].dropna()

df_service['Has Online delivery'] = df_service['Has Online delivery'].map({'Yes': 1, 'No': 0})
df_service['Has Table booking'] = df_service['Has Table booking'].map({'Yes': 1, 'No': 0})

grouped = df_service.groupby('Price range').mean().reset_index()

print("Average availability of services by Price Range:\n")
print(grouped)

# Plot Online Delivery vs Price Range
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.barplot(data=grouped, x='Price range', y='Has Online delivery', palette='coolwarm')
plt.title('Online Delivery vs Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion with Online Delivery')
plt.ylim(0, 1)

# Plot Table Booking vs Price Range
plt.subplot(1, 2, 2)
sns.barplot(data=grouped, x='Price range', y='Has Table booking', palette='viridis')
plt.title('Table Booking vs Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion with Table Booking')
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
