s1 ="This is a test. This test is simple.".replace('.'," ").split()
print(s1)
di={}
for i in s1:
  if i in di:
    di[i] =  di[i] + 1
  else:
    di[i]=1
    for key in di.keys():
      print(f'{key}: {di[key]}')
#print(di)  
  p= "  shalu  ".strip()# It remove leading and trailing spaces 
  print(p)