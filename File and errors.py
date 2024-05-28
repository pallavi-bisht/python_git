#TIY 189
from pathlib import Path

path=Path('learning_python.txt')
content= path.read_text()
print(content)

line=content.splitlines()
for i in line:
 print(i)
 
x=content.replace('Python','Java')
print(f"\n{x}")
