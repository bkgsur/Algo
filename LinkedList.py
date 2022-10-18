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
            n = ListNode(data=d.pop(0))
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
test()


# def mergell(l1:ll)

