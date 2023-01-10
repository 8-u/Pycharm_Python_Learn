import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws['C5'] = "我喜欢编程"
wb.save("exercise7_3.xslx")
