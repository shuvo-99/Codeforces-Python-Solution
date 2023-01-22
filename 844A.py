s = input()
n = int(input())
unique = []

for i in s:
  if i not in unique:
    unique.append(i)

if len(s)<n:
  print('impossible')
  
else:
  length = len(unique)
  if length >= n:
    print(0)
  else:
    print(n-length)

# Alternative Approach - 


def func(s):
    
    ff = set()
    for c in s:
        ff.add(c)
    if len(s)<n:
        print('impossible')
    else:
        w = len(ff)
        if w>=n:
            print(0)
        else:
            print(n-w)
func(s)