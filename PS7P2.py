a = 1
b = 1
count = 1
print("First 20 Fibonacci numbers:")
while count <= 20:
   print(a, end=" ")
   next_num = a + b
   a = b
   b = next_num
   count += 1