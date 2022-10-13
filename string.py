import functools


def ispalindromic(S):
    return all(S[i] == S[~i] for i in range(len(S)//2))


#print(ispalindromic('abccba1'))


def inttostring(x):
    isnegative = False
    if x<0:
        isnegative =True
        x=-x
    s=[]
    while True:
        s.append(chr(ord('0') + x%10))
        x = x//10
        if x==0:
            break
    s.reverse()
    return ('-' if isnegative else '') +  ''.join(s)

S1 = inttostring(-1234)
print('inttostring',S1)


def stringtoint(S):
    isnegative = False
    if S[0] == '-':
        isnegative = True
        S = S[1:]
    sum =0
    for i in range(len(S)):
        sum +=  (ord(S[i]) - ord('0')) * pow(10,len(S)-(1+i))
    return (-1 if isnegative else 1) *  sum

print(stringtoint(S1))
