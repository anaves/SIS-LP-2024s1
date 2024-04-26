import time
n = 1
while True:
    if n == 1:
        parcela = 1
    if n == 5:
        parcela = -1
    print("*"*n)
    time.sleep(0.1)
    n = n + parcela