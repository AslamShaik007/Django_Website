import aspose.words as aw
import os
import random

def FileValidation(filename):
    MAX_SIZE = 3000000  # in bytes
    if filename.size <= MAX_SIZE:
        filename = (str(filename)).split(".")
        if filename[-1] == "pdf" or filename[-1] == "doc" or filename[-1] == "docx":
            return True
        else:
            return False
    else:
        return False



# saves the resume in resumes folder with duplicate validation
def SaveResume(filename, filepath, basepath, email):
    basepath = str(os.getcwd()) + basepath + "/"
    # path = os.listdir(basepath)
    newfilename =  email+ '.'+ (filename.name).split('.')[-1]
    if not os.path.isfile(basepath + newfilename):
        with open(filepath + newfilename, "wb+") as destination:
            for chunk in filename.chunks():
                destination.write(chunk)
        return newfilename
    else:
        newfilename =  email+ str(random.randint(1000, 9999))  +'.'+ (filename.name).split('.')[-1]
        with open(filepath + newfilename, "wb+") as destination:
            for chunk in filename.chunks():
                destination.write(chunk)
        return newfilename


# changes the .doc document to .docx
def doctodocx(filepath, filename , basepath):
    basepath = str(os.getcwd()) + basepath + "/"
    # path = os.listdir(basepath)
    docxfile= filename.replace('.doc', '.docx')
    if not os.path.isfile(basepath + docxfile):
        doc = aw.Document(filepath + filename)
        doc.save(filepath + docxfile)
        os.remove(f'media/{filename}')
        return docxfile
    else:
        newfilename = filename.split(".")
        output = ""
        for i in range(0, len(newfilename) - 1):
            output += newfilename[i]
        docxfile= output + str(random.randint(1000, 9999)) + '.docx'
        doc = aw.Document(filepath + filename)
        doc.save(filepath + docxfile)
        os.remove(f'media/{filename}')
        return docxfile

# # saves the resume in resumes folder with duplicate validation
# def SaveResume(filename, email):
#     filename.name =  email+ '.'+ (filename.name).split('.')[-1]
#     with open('media/' + filename.name , "wb+") as destination:
#         for chunk in filename.chunks():
#             destination.write(chunk)
#     return filename.name
