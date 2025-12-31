r = '''987654321111111
811111111111119
234234234234278
818181911112111'''
r = r.split("\n")
num = []
for i in r:
    while (len(i) > 12):
        min_no = "9"
        for j in i:
            if j<min_no:
               min_no = j
        i = i.replace(min_no," ",1)
        i = i.split(" ")
        i = i[0]+i[-1]
    num.append(int(i))
    print(i)
print(sum(num))
