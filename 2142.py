s=input()
# 创建一个空字典来存储每个字符的出现次数
char_count={}

for char in s:
  if char in char_count:
    char_count[char]+=1
  else:
    char_count[char]=1

max_count=max(char_count.values())
  
result = [char for char in sorted(char_count.keys()) if char_count[char] == max_count]

print("".join(result))
