n = float(input())
ed = n % 10
des = (n //10) % 10
sot = (n // 100) % 10
t = (n // 1000) % 10
des_t = (n // 10000) % 10
print (des**ed * sot / (des_t - t))
