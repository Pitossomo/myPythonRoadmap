# Creating an array of integer type
import array as arr 
a = arr.array('i', [1, 2, 3])

print('The new created arrays is: ', end = ' ')
for i in range(3):
  print (a[i], end = ' ')
print()