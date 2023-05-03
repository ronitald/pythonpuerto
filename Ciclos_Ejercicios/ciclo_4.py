num=1
while num <= 1000:
    i=1
    sum=0
    while i<num:
        if num % i == 0:
            sum+=i
        i+=1
    if num==sum:
        print (f'{sum} es perfecto. ')
    num+=1