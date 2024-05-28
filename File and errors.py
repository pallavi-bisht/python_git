#TIY 189
from pathlib import Path

path=Path('learning_python.txt')
content= path.read_text()
print(content)

for i in content.splitlines():
 print(i)
 
x=content.replace('Python','Java')
print(f"\n{x}")

#TIY 192
""" 
from pathlib import Path

path=Path('Output.txt')
abc=input("What is Your name ?\n")
path.write_text(abc)
print(path.read_text())

from pathlib import Path

lmn=""
while True:
 pqr=input("What is Your name ? Enter (y/n) to quit .\n")
 if pqr =='y':
  break
 else:
  lmn+=pqr+"\n"
  print(lmn)
  
path2=Path('Output2.txt')
path2.write_text(lmn)
print(path2.read_text())"""

#TIY 200

a=input("enter a value .\n")
b=input("enter b value .\n")
try:
 
 ab=int(a)+int(b)

except ValueError:
  print(" Error !! Please enter integer value\n")
else:
 print(f"sum of {a} and {b} is {ab}\n")

from pathlib import Path
path1=Path("Output.txt")
path2=Path("Output2.txt")

try:
 path1.read_text()
 path2.read_text()

except FileNotFoundError:
  #print("File not Found!") 
  # or 
  pass
else:

 print(path1.read_text())
 print(path2.read_text())

from pathlib import Path
path1=Path("Output2.txt")
abc= path1.read_text()
print(len(abc.split()))
  

