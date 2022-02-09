import xlwt
# workbook = xlwt.Workbook(encoding = 'utf-8')#W是大写
# worksheet = workbook.add_sheet('sheet1')
# worksheet.write(0,0,'hello')
# workbook.save('student.xls')

workbook = xlwt.Workbook(encoding='utf-8') #创建workbook 对象
worksheet = workbook.add_sheet('sheet1') #创建工作表sheet
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i, j, "%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
# worksheet.write(0, 0, 'hello') #往表中写内容,第一各参数 行,第二个参数列,第三个参数内容
workbook.save('students.xls') #保存表为students.xls