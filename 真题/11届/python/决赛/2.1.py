i=4
j=2
count=0

for i in range(4,2021):
  for j in range(2,i):
    if i%j==0:
      count+=1
      break
    else:
      j+=1
  i+=1
print(count)
