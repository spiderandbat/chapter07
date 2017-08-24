import os

def run(**args):
    print "[liukang *] In dirlister module."
    files = os.listdir(".")

    return str(files)
