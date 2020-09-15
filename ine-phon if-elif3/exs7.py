s1 = "English = 78 Science =83 math = 68 Histoly = 65"
s3 = (s1.split())
sam = 0
y = 0

for x in s3:
  if x.isnumeric():
      sam = sam + int(x)
      y = y + 1

print('sam is',sam)
print('average:',sam/y)

    



