from src.data import load_spam_ham_data

df = load_spam_ham_data()

print(f"Loaded {len(df)} emails.")
print(df['label'].value_counts())
print(df.head())