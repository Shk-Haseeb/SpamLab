import os
import pandas as pd

def load_emails_from_directory(directory, label):
    data = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='latin-1') as file:
                content = file.read()
                data.append({'text': content, 'label': label})
        except Exception as e:
            print(f"Skipping {filename}: {e}")
    return data

def load_spam_ham_data(base_path='data'):
    folders = [
        ('spam', 'spam'),
        ('spam_2', 'spam'),
        ('easy_ham', 'ham'),
        ('easy_ham_2', 'ham')
    ]

    all_data = []
    for folder_name, label in folders:
        folder_path = os.path.join(base_path, folder_name)
        emails = load_emails_from_directory(folder_path, label)
        all_data.extend(emails)

    df = pd.DataFrame(all_data)
    return df