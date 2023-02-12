import time
a = """"""
i = 1
k = 1
for i in range(11):
    for k in range(11):
        a = a + str(i)+' x '+str(k)+' = ' + str(i*k) + '\n'
    time.sleep(1)
    print(a)