x, a, b = map(float, input().split())
if a >= x and b < x:
  print("Mike")
elif b >= x and a < x:
  print("Ivan")
elif a >= x and b >= x:
  print ("2")
elif a+b >= x:
  print("1")
else:
  print("0")
