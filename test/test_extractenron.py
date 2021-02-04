from extractenronlib import extractenron
import pandas as pd
import os

def test_extract():
    emails =  pd.read_csv(os.path.abspath('emails30MB.csv'), names=['file', 'emails'])
    emails_extracted = extractenron.extract(emails, ['Date', 'Subject'], extract_payload=False)
    assert  len(emails_extracted.columns) == 4