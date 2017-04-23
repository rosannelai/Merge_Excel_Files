import pandas as pd
import glob2
from os.path import basename as os

all_data = pd.DataFrame()

for f in glob2.glob("*.xls*"):

    sheets = pd.ExcelFile(f).sheet_names
    for s in sheets:
        df = pd.read_excel(f, sheetname = s, index=False, header=None, names=None, ignore_index=True)
        df.index = [os(f)] * len(df)
        all_data = all_data.append(df)

all_data.to_csv("MergedFile.csv", encoding='utf8')

print ("Completed! Number of Files Merged = " + str(all_data.index.nunique()))
print (all_data.index.unique())
