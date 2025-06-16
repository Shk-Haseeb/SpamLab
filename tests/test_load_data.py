import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data import load_spam_ham_data

def test_load_data_shape():
    df = load_spam_ham_data()
    assert isinstance(df, pd.DataFrame)
    assert 'text' in df.columns
    assert 'label' in df.columns
    assert df.shape[0] > 0  
    assert df['label'].isin(['spam', 'ham']).all() 
