def sum(n):
    limit=0
    for i in range (1,1000):
        limit += i
        if i == n:
            break
    return limit

print(sum(10))

def check_age(age):
    if age > 18:
        print('you are allowed to enter this web site')

    else:
        print('you are not allowed to enter')


check_age(14)




