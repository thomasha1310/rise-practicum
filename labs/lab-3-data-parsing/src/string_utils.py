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

df = pandas.DataFrame(columns=['raw', 'clean'])
df['raw'] = pandas.read_csv('../data/messy_strings.csv')
df['clean'] = clean_strings(df['raw'])

assert list(df['clean'].value_counts()) == [12, 11, 9, 9, 5, 4]
print('Outputs matched expected values.')