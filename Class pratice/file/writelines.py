myobj = open("myfile.txt","r+")
lines = ["Hello eveny one\n","one\n","two\n","three\n","four"]
myobj.writelines(lines)
myobj.close()
