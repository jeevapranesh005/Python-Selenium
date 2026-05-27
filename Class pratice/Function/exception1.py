try:
    fh=open("test.txt","w")
    try:
        fh.write("This is my test file for exception hsndling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error : can\t find file to read data")
else:
    print("i will execute when no expection occurs")
finally:
    print("I am always executing")