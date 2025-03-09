try:
    file=open("sample.txt","r")
    read_text=file.readlines(1)
    read_text1=file.readlines(2)
    print("Reading file content : \n Line 1 : ",read_text)
    print("\n Line 2 : ",read_text1)
    file.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found")
finally:
    '''nothing'''