'''
将pdf转换为word,这里用了pdf2docx的模块,方法一：
'''
#导入pdf2docx模块
from pdf2docx import Converter

#选择需要存储的pdf文件，并新建一个docx文件
pdf_file = r'C:\Users\XMILES\Desktop\work\plan\102.pdf'
docx_file = r'C:\Users\XMILES\Desktop\work\plan\102.docx'

#将pdf文件转换成docx格式
cv = Converter(pdf_file)

#将保存的数据导入docx文件中
cv.convert(docx_file,start=0,end=None)

#关闭该数据文件
cv.close()

'''
将pdf转换为word,这里用了Aspose.Words Cloud SDK的模块,方法二：
'''