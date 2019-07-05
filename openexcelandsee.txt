import openpyxl

path = "C:/Users\Android - PC\Desktop\data3.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active
#sheet=workbook.get_sheet_by_name("Sheet1")

rows = sheet.max_row
cols = sheet.max_column

print(rows)
print(cols)

for r in range (1,rows+1):
    for c in range(1, cols+1):  #always take +1 to range function
        print(sheet.cell(row=r,column=c).value,end="  ")   #end used for space
    print()
