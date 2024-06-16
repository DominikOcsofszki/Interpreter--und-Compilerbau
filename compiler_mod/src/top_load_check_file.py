
def getFilesFromFile():
    with open('/Users/dominikocsofszki/ss2024/compiler/projekt/compiler_mod/data.tx', 'r') as file:
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
            with open(file, 'r') as file:
                data = file.readlines()
                return data

files = getFilesFromFile()
data = openAllFilesChecker(files)
print("====================input:=======================")
# print(data)
lst_check =[]
for x in data:
    x =x.replace("\n","")
    if not x.startswith("#"):
        if not x.endswith(";"):
            if not x.endswith("{"):
                lst_check.append(x)
    
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
def print_no_comments_newlines():
    files = getFilesFromFile()
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                # data = file.read()
                for line in file:
                    if not line.startswith("\n"):
                        line = line.partition('#')[0]
                        line = line.rstrip()
                        if len(line) > 0:
                            print(line)
                return data
print_no_comments_newlines()
print("====================output:=======================")
