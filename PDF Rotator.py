# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:52:24 2022

@author: Hans
"""

import PyPDF2
pdf_in = open('C:/Users/Hans/Downloads/HUM 330 Research Paper attachment.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(90)
    pdf_writer.addPage(page)

pdf_out = open('G:/My Drive/Professional/Education/Simon Fraser University/2022/3-Fall/HUM 330/HUM 330 Research Paper attachment.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()