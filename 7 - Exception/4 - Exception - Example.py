sname=input("Enter Existing file name ")
dname=input("Enter new file name ")
try:
   sh=open(sname, "r") 
   dh = open(dname, "w")
   str=sh.read() 
   dh.write(str)
except IOError:
   print ("Error: can\'t find file or read data ")
else:
   print ("File successfully copied ")
   sh.close()
   dh.close()
