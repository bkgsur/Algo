import functools
import string

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
#print('inttostring',S1)


def stringtoint(S):
    isnegative = False
    if S[0] == '-':
        isnegative = True
        S = S[1:]
    sum=0
    for i in range(len(S)):
        sum +=  (ord(S[i]) - ord('0')) * pow(10,len(S)-(i+1))
    return (-1 if isnegative else 1) *  sum

#print(stringtoint(S1))

# convert number from one base to next
def baseconversion(S:string,b1:int,b2:int)->str:
    print(string.hexdigits)
    def constructfrombase(num_as_int:int,base:int)->str:
        return ('0' if num_as_int==0 else constructfrombase(num_as_int//base, base)+string.hexdigits[num_as_int%base].upper())

    is_negative = S[0] =='-'
    num_as_int = functools.reduce(lambda a,b: a*b1 + string.hexdigits.index(b.lower()),S[is_negative:],0)

    return '-' if is_negative else constructfrombase(num_as_int,b2)

print(baseconversion('615',10,13))

def spreadsheetdecode(C):
    return functools.reduce(lambda a,b: a*26 + ord(b) - ord('A')+1 ,C,0)

# print(spreadsheetdecode('ZZ'))
# print(spreadsheetdecode('A'))

# Consider the following two rules that are to be applied to an array of characters.
# o Replace each'a'by two'd's.
# o Delete each entry containing a'b'.
def replaceandreduce(A:[],n:int)->[]:
    write_idx=-1
    a_count=0
    for i in range(n):
        if A[i] == 'a':
            a_count+=1
        if A[i]!='b':
            write_idx+=1
            A[write_idx]=A[i] # move valid items to left

    curr_idx = write_idx
    write_idx += a_count # go to last index of the array
    final_size = write_idx+1
    #print(A, write_idx, a_count)
    while curr_idx>=0:
        if A[curr_idx] == 'a':
            A[write_idx-1:write_idx+1]='dd'
            write_idx-=2 # move 2 spots to the left
        else:
            A[write_idx] = A[curr_idx] # move valid ites to left
            write_idx-=1
        curr_idx-=1
    return A

A= ['a','c','d','b','b','c','a']


# print(A)
# print(replaceandreduce(A,7))


