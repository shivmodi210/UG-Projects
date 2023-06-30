import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  

n=pdfReader.numPages

for i in range(n):
    pageObj = pdfReader.getPage(i)
    text=pageObj.extractText()
    f= open("myFile.txt", "a")
    f.write("{}".format(text))
    f.close()

pdfFileObj.close()

f = open("myFile.txt", "rt")
print(f.read())