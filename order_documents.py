import os


downloaddFolder = "/Users/Jhonney Correa/Downloads/"
picturesFolder = "/Users/Jhonney Correa/Downloads/pictures/"
executablesFolder = "/Users/Jhonney Correa/Downloads/executables/"
pdfFolder = "/Users/Jhonney Correa/Downloads/pdf/"

if __name__=='__main__':
    for filename in os.listdir(downloaddFolder):
        name, extension = os.path.splitext(downloaddFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".jfif"]:
            os.rename(downloaddFolder + filename, picturesFolder + filename)
        if extension in [".pdf"]:
            os.rename(downloaddFolder + filename, pdfFolder + filename)
        if extension in [".exe", ".msi"]:
            os.rename(downloaddFolder + filename, executablesFolder + filename)