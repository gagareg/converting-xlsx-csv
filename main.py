import xlrd
import pandas as pd

location = ("input.xlsx")
rows = []
csv_row = []

wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

sheet.cell_value(0, 0)

for i in range(1, sheet.nrows):
    rows.append(sheet.row_values(i))

for i in range(0, sheet.nrows - 1):
    split_row1 = rows[i][1].split('_', 1).pop(1)
    split_row4 = rows[i][4].split('/', 1).pop(1)
    fin_split_rows = '{0},{1},'.format(split_row1, split_row4)
    csv_row.append(fin_split_rows)

df = pd.DataFrame(csv_row)
df.to_csv('output.csv', sep='\t', header=None, index=None)
