import os,sys
folder = "C:\\Users\\hhson\\OneDrive\\Masaüstü\\deneme"
for filename in os.listdir(folder):
       
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.jpg','.jpeg')
       output = os.rename(infilename, newname)
       
