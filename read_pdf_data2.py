import PyPDF2
import re
import tabula
pdfFileObj = open('C:/DE1512577.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numpages=pdfReader.numPages

# pageObj = pdfReader.getPage(n)
# abc=pageObj.extractText()
# if 'Tax Invoice(Original for Recipient)' in abc:
#     print(abc.strip())
#     xy=abc.find('r:')
#     print(xy)
#     xyz = abc.find('GSTIN')
#     print(xyz)
#     print(abc[xy+2:xyz])
#     print('-----------------------------')
#     xy = abc.find('Due Date:')
#     print(xy)
#     xyz = abc.find("Supplier's State Code:")
#     print(xyz)
#     print(abc[xy + 9:xyz])



for x in range(numpages):

    pageObj = pdfReader.getPage(x)
    abc=pageObj.extractText()
    if 'Tax Invoice(Original for Recipient)' in abc:
        print(abc.strip())
        xy = abc.find('r:')
        #print(xy)
        xyz = abc.find('GSTIN')
        #print(xyz)
        print(abc[xy + 2:xyz])

        xy = abc.find('Due Date:')
        #print(xy)
        xyz = abc.find("Supplier's State Code:")
        #print(xyz)
        print(abc[xy + 9:xyz])
        print('-----------------------------')
        df = tabula.read_pdf("C:/DE1512577.pdf",pages=x)


