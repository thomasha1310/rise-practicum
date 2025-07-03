import pandas
import re
import string

def clean_strings(strings: pandas.Series) -> pandas.Series:
    strings = strings.dropna()
    strings = strings.astype(str)
    strings = strings.str.lower()
    strings = strings.str.strip()
    pattern = f"[{re.escape(string.punctuation)}]" # regex pattern for punctuation
    strings = strings.str.replace(pattern, '', regex=True)
    return strings