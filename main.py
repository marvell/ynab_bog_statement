import pandas as pd
import csv

def parse_purpose(s):
    out = {}
    purpose = s.removeprefix('Payment - ')
    lines = purpose.split(';')
    for l in lines:
        p = l.strip().split(':')
        out[p[0].strip()] = p[1].strip()

    return out

mcc_categories = [
    {
        'min': 1000,
        'max': 1100,
        'category': 'Grocery',
    },
]

def convert_mcc_to_category(mcc):
    return mcc_categories[0]['category']

file_path = 'data/Report-2024-Jan-21-12:34:36.xls'

df = pd.read_excel(file_path, sheet_name='Statement')

out = [
    ['Date', 'Payee', 'Memo', 'Amount'],
]

for index, row in df.iterrows():
    if row['Purpose'].startswith('Payment'):
        v = parse_purpose(row['Purpose'])
        category = convert_mcc_to_category(v['MCC'])

        out.append([
            row['Date'],
            '',
            v['Merchant'],
            row['USD'],
        ])

print(out)