r = '''11-22'''
r = r.split(",")

def check(num):
    for i in num:
        

for i in r:
    num = []
    i = i.split("-")
    for j in range(int(i[0]),int(i[1])+1):
        num.append(j)
    check(num)
