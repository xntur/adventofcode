lo = 168630
hi = 718098

def has2(i):
    ct = 1
    curr = i[0]
    for x in range(1, len(i)):
        if i[x] == curr:
            ct += 1
        else:
            if ct == 2:
                return True
            ct = 1
            curr = i[x]
    return ct == 2

def atLeast2(i):
    ct = 1
    curr = i[0]
    for x in range(1, len(i)):
        if i[x] == curr:
            ct += 1
        else:
            if ct >= 2:
                return True
            ct = 1
            curr = i[x]
    return ct >= 2

def good(i):
    curr = int(i[0])
    for x in i:
        if int(x) < curr:
            return False
        curr = int(x)
    return True

count1 = 0
count2 = 0
for i in range(lo, hi):
    a = str(i)
    if good(a):
        if atLeast2(a):
            count1 += 1
        if has2(a):
            count2 += 1

print(count1)
print(count2)
