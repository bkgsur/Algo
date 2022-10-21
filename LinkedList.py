class ListNode:
    def __init__(self, data:int=0,next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return self.data
class LinkedList:

    def __init__(self):
        self.head=None

    def __repr__(self):
        node = self.head
        n=[]
        while node is not None:
            n.append(node.data)
            node = node.next
        return '->'.join([str(x) for x in n])

    def create(self,d:[]=None)->None:
        if d is None:
            d = [1,2,3,4,5,6]
        self.head=None
        if d :
            n:ListNode = ListNode(data=d.pop(0))
            self.head = n
            while d:
                n.next = ListNode(data=d.pop(0))
                n = n.next

    def search(self,key:int) -> ListNode:
        n:ListNode = self.head
        while n and n.data !=key:
            n=n.next
        return n

    def insertafter(self,n:int,n1:int)->None:
        node:ListNode = self.head
        if node:
            node= self.search(n)
        # print(node.data)
        if node:
            newnode:ListNode = ListNode(data=n1)
            newnode.next = node.next
            node.next = newnode


    def deleteafter(self,n:int)->None:
        n:ListNode = self.search(n)
        if n and n.next:
            n.next = n.next.next
def test():
    l = LinkedList()
    l.create(d=[ i for i in range(5,15)])
    print(l)
    l.insertafter(5,8)
    print(l)
    l.deleteafter(5)
    print(l)
# test()

l1 = LinkedList()
l1.create(d= [1,3,5,7,9,11,13,15])
l2 = LinkedList()
l2.create(d =[2,4,6,8,10,12,14])
l3 = LinkedList()
l3.create(d= [ i for i in range(1,15)])



def mergell(l1:LinkedList,l2:LinkedList)->LinkedList:
    n:ListNode=ListNode()
    ll: LinkedList = LinkedList()

    h1:ListNode = l1.head
    h2:ListNode = l2.head

    while  h1 and h2:
        if h1.data<h2.data:
            n.next = h1
            h1 = h1.next
        else:
            n.next = h2
            h2= h2.next
        n = n.next
        if ll.head is None:
            ll.head = n
    n.next = h1 or h2

    return ll

# print(mergell(l1,l2))

def reversesublist(ll:LinkedList, s:int,f:int)->LinkedList:
    dummyhead = sublisthead= ll.head
    if ll.head:
        for _ in range(2, s):
            sublisthead = sublisthead.next

        sublistiter:ListNode = sublisthead.next
        for _ in range(f-s):
            temp:ListNode = sublistiter.next
            sublistiter.next, temp.next,  sublisthead.next = (temp.next, sublisthead.next, temp)
        ll.head = dummyhead
    return ll

print(reversesublist(l3,4,7))





