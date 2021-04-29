from PyPDF2 import PdfFileMerger


pdfs = ['merge1.pdf', 'merge2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
