import openpyxl

path = "C:/Users\Android - PC\Desktop\data3.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active
#sheet = workbook.get_sheet_by_name("Sheet2")

for r in range (1,13):
    for c in range(1,4):  #always take +1 to range function
      sheet.cell(row=r,column=c).value="welcome"
workbook.save(path)