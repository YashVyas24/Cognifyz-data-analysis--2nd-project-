import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

nltk.download('stopwords')

file_path = r"C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Level 3\Dataset.csv"
df = pd.read_csv(file_path)

df = df[['Cuisines', 'Aggregate rating', 'Rating text']].dropna()

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return words

df['tokens'] = df['Cuisines'].apply(clean_text)

positive_reviews = df[df['Rating text'].isin(['Excellent', 'Very Good'])]
negative_reviews = df[df['Rating text'].isin(['Average', 'Poor', 'Not rated'])]

positive_words = [word for tokens in positive_reviews['tokens'] for word in tokens]
negative_words = [word for tokens in negative_reviews['tokens'] for word in tokens]

top_positive = Counter(positive_words).most_common(10)
top_negative = Counter(negative_words).most_common(10)

pos_words_df = pd.DataFrame(top_positive, columns=['Keyword', 'Frequency'])
neg_words_df = pd.DataFrame(top_negative, columns=['Keyword', 'Frequency'])

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(data=pos_words_df, x='Frequency', y='Keyword', palette='Greens_r', ax=axes[0])
axes[0].set_title("Top 10 Positive Keywords")
axes[0].set_xlabel("Count")
axes[0].set_ylabel("Keyword")

sns.barplot(data=neg_words_df, x='Frequency', y='Keyword', palette='Reds_r', ax=axes[1])
axes[1].set_title("Top 10 Negative Keywords")
axes[1].set_xlabel("Count")
axes[1].set_ylabel("Keyword")

plt.tight_layout()
plt.show()
