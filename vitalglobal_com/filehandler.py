import os
import random
from PyPDF2 import PdfFileReader
from docx import Document

def FileValidation(filename):
    MAX_SIZE = 3000000  # in bytes
    if filename.size <= MAX_SIZE:
        filename = str(filename)
        _, file_extension = os.path.splitext(filename)
        if file_extension.lower() in [".pdf", ".doc", ".docx"]:
            return True
        
    return False




def SaveResume(filename, filepath, basepath, email):
    basepath = os.path.join(os.getcwd(), basepath)
    newfilename = f"{email}.{filename.name.split('.')[-1]}"
    full_filepath = os.path.join(filepath, newfilename)
    if not os.path.isfile(os.path.join(basepath, newfilename)):
        with open(full_filepath, "wb+") as destination:
            for chunk in filename.chunks():
                destination.write(chunk)
        return newfilename
    else:
        newfilename = f"{email}{random.randint(1000, 9999)}.{filename.name.split('.')[-1]}"
        full_filepath = os.path.join(filepath, newfilename)
        with open(full_filepath, "wb+") as destination:
            for chunk in filename.chunks():
                destination.write(chunk)
        return newfilename

def doctodocx(filepath, filename, basepath):
    basepath = os.path.join(os.getcwd(), basepath)
    docxfile = filename.replace('.doc', '.docx')
    full_docx_filepath = os.path.join(filepath, docxfile)
    if not os.path.isfile(os.path.join(basepath, docxfile)):
        doc = Document(os.path.join(filepath, filename))
        doc.save(full_docx_filepath)
        os.remove(os.path.join('media', filename))
        return docxfile
    else:
        newfilename = filename.split(".")
        output = ""
        for i in range(len(newfilename) - 1):
            output += newfilename[i]
        docxfile = output + str(random.randint(1000, 9999)) + '.docx'
        full_docx_filepath = os.path.join(filepath, docxfile)
        doc = Document(os.path.join(filepath, filename))
        doc.save(full_docx_filepath)
        os.remove(os.path.join('media', filename))
        return docxfile