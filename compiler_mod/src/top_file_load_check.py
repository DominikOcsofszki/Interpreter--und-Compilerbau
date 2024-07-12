
def getFilesFromFile():
    with open('code.tx', 'r') as file:
        files = file.read()
        return files

def checkFile(file:str):
    if file.startswith('#'):
        return None
    return file

def openAllFiles(files):
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                data = file.read()
                return data

def openAllFilesChecker(files):
    for file in files.splitlines():
        if checkFile(file) :
            print(file)
            with open(file, 'r') as file:
                data = file.readlines()
                return data

def checkAndOpenFile():
    files = getFilesFromFile()
    data = openAllFilesChecker(files)
    print("====================input:=======================")
    print_no_comments_newlines()
    # print(data)
    lst_check =[]
    check_exit = False # <<change to True for check
    for x in data:
        x =x.replace("\n","")
        if x.__contains__("#DONT"):
            check_exit = False
        if not x.startswith("#"):
            if not x.endswith(";"):
                if not x.endswith("{"):
                    lst_check.append(x)
        
    if check_exit:
        missing_end = [x for x in lst_check if len(x)>1]
        if len(missing_end) > 1:
            print("PROBLEM WITH ; TO MANY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! exit()")
            print(missing_end)
            # exit()
        if len(missing_end) == 0:
            print("PROBLEM WITH ; MISSING  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! exit()")
            print(missing_end)
            # exit()
    data = openAllFiles(files)
    print("====================output:=======================\n")
    return data

def print_no_comments_newlines():
    files = getFilesFromFile()
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                linenr=1
                # data = file.read()
                for line in file:
                    if not line.startswith("\n"):
                        line = line.partition('#')[0]
                        line = line.rstrip()
                        if len(line) > 0:
                            print(linenr,line)
                    linenr +=1
                return 
def print_line_nr(lineno):
    files = getFilesFromFile()
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                linenr=1
                # data = file.read()
                for line in file:
                    if lineno == linenr:
                        print(linenr, line)
                        return 
                    linenr +=1

