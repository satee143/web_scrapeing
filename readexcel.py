import pytest,openpyxl
def read_data():
    wb=openpyxl.load_workbook('C:/Users/E005181/PycharmProjects/web_scrapeing/data.xlsx')
    ws=wb['Sheet1']
    row=ws.max_row
    l=[]
    for i in range(1, row + 1):
        l1 = []
        username = ws.cell(i, 1)
        l1.insert(0, username.value)
        l.insert(i - 1, l1)
    print(l)
    return l