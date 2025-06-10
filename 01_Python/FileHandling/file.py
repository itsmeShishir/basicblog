# file handling -> read, write, append, delter using os module
# read operations  -> mode, r, r+, w, w+, a, a+
fsw = open("FileHandling/hello.txt" ,"r+")
helo = fsw.read()

# write Operations -> w+, w
fs = open('FileHandling/bye.txt', 'w+')
fs.write("hello shishir\n")
fs.write("bye shishir")
fs.close()

# Append  -> a+
fs = open('FileHandling/bye.txt', 'a+')
fs.write(helo)
fs.close

# with statement with read operations
with open("FileHandling/h.txt", "r+") as fo:
    print(fo.read())

# delete
import os
# os.remove("FileHandling/bye.txt")

