import time
import math
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head=None
        # self.tail=None
    #normal insertion
    def insertion(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
        else:
            pointer=self.head
            while pointer.next is not None: #O(N)
                pointer=pointer.next
            pointer.next=node
    #insert at begin
    def insert_at_begin(self,data):
        node=Node(data,None)
        if self.head is not None:
            node.next =self.head 
        self.head=node
    

    def delete_last(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head =None
        pointer=self.head
        while pointer.next.next is not None:
            pointer=pointer.next
        pointer.next=None
    
    def print_all(self):
        current=self.head
        ll=[]
        while current is not None:
            ll.append(current.data)
            current=current.next
        print(ll)

    def findlistlength(self):
        pointer=self.head 
        count=0
        while pointer is not None:
            count+=1
            pointer=pointer.next
        return count 

    def findtheelement(self,k):
        pointer=self.head
        while pointer is not None:
            if(pointer.data==k):
                return 1
            pointer=pointer.next
        return 0
    def delete_k_element(self,k):
        #head element check
        pointer=self.head
        if self.head is None:
            return 
        if(self.head.data==k):
            to_delete = self.head
            self.head = self.head.next
            to_delete.next=None
            return
        previous=None
        while pointer is not None:
            if(pointer.data==k):
                previous.next=pointer.next          
            previous=pointer
            pointer=pointer.next 
    
    def delete_without_head(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def middleNode(self):
        fast=self.head
        slow=self.head
        #Tortoise and Hare method
        while((fast is not None) and (fast.next is not None) ):
            slow=slow.next
            fast=fast.next.next
        return slow 
    def reverseList(self, head: Optional[ListNode]):  
        # we need to create a dummy node which holds null
        temp=None
        cur=head
        while ( head is not None):
            cur=cur.next
            #reversing the arrow
            head.next=temp
            #carrying the head
            temp=head
            head=cur
        return temp
    def hasCycle_brute(self, head) -> bool:
        val1=set()
        pointer=self.head
        while pointer is not None:
            if(pointer.val in val1):
                return True
            else:
                val1.add(pointer.val)
            pointer=pointer.next
        return False
    def hasCycle(self, head) -> bool:
        fast=self.head
        slow=self.head
        while((fast is not None) and (fast.next is not None) ):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
    
    def firstNodecycle_brute(self, head) -> bool:
        val1=set()
        pointer=self.head
        while pointer is not None:
            if(pointer in val1):
                return pointer
            else:
                val1.add(pointer)
            pointer=pointer.next
        return None
    
    def firstNodecycle(self, head) -> bool:
        fast=head
        slow=head
        tracker=head
        while((fast is not None) and (fast.next is not None) ):
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                while tracker!=slow:
                    slow=slow.next 
                    tracker=tracker.next
                return tracker
        return None
    
    def lengthOfLoop_brute(head: Node) -> int: #wrong approch
        fast=head
        slow=head
        tracker=head
        length1=0
        length2=0
        while((fast is not None) and (fast.next is not None) ):
            fast=fast.next.next
            slow=slow.next
            length1+=1
            if slow==fast:
                while tracker!=slow:
                    slow=slow.next 
                    tracker=tracker.next
                    length2+=1
                return (length1-length2)+1
        return 0
    def lengthOfLoop(head: Node) -> int:
        fast=head
        slow=head
        flag=0
        count=1
        while((fast is not None) and (fast.next is not None) ):
            
            if (slow==fast) and flag==1:
                count=1
                slow=slow.next # loop starting we include the length as one (count1)
                while fast!=slow:
                    slow=slow.next
                    count+=1 
                return count
            slow=slow.next
            fast=fast.next.next
            flag=1
        return 0
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        temp=head 
        while fast.next != None and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next 
        slow.next=self.reverse_link(slow.next)
        slow=slow.next
        while slow is not None:
            if temp.val is not slow.val:
                return False
            temp = temp.next
            slow = slow.next
        return True

    def reverse_link(self,midhead):
        temp=None
        current=None
        while midhead is not None:
            current=midhead.next
            midhead.next=temp
            temp=midhead
            midhead=current
        return temp
    def oddEvenList(self, head):
        current=head
        if(head is None):
          return None
        if(current.next is None):
            return head
        if(current.next.next is None):
            return head
        odd_pointer=head
        even_pointer=head.next 
        even_head=even_pointer
        i=1
        while current is not None:
            if (i>2 and i%2!=0):
                odd_pointer.next=current
                odd_pointer=odd_pointer.next 
            elif (i>2 and i%2==0):
                even_pointer.next=current
                even_pointer=even_pointer.next 
            i+=1
            current=current.next

        even_pointer.next =None
        odd_pointer.next=even_head
        return head 
    def removeNthFromEnd_brute(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        pos=0
        prev=None 
        len=0
        while current is not None:
            len+=1
        print(len)
        while(current is not None):
            if(pos==n):
                if(current.next is not None):
                    prev.next=current.next
                else:
                    prev.next=None
                return head 
            prev=current
            current=current.next 
            pos+=1
        return None
    def removeNthFromEnd_opt(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=Node(None,None)
        start.next=head
        fast=start
        slow=start 
        while (n>0):
            fast=fast.next
        while fast.next is None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next 
        return start.next
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=self.head
        slow=self.head
        prev=None
        while ((fast is not None) and fast.next is not None):
            prev=slow
            slow=slow.next
            fast=fast.next.next 
        prev.next=slow.next
        return head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start=Node(None,None)
        temp=start
        carry=0
        while ( (l1 is not None ) or (l2 is not None) or carry):
            sum1=0
            if(l1!=None):
                sum1+=l1.val
                l1=l1.next
            if(l2!=None):
                sum1+=l2.val
                l2=l2.next
            sum1+=carry
            carry=(sum1//10)
            new_=Node(sum1%10,None)
            temp.next=new_
            temp=temp.next 
        return start.next
    
    def addOne(self,head: Node) -> Node:
        k =self.reverse_list(head)
        carry = 0
        prev = None
        head.data += 1
        while(head != None) and (head.data > 9 or carry > 0):
            prev = head
            head.data += carry
            carry = head.data // 10
            head.data = head.data % 10
            head = head.next
        return self.reverse_list(k)
    #hard problem -- >reverse on k group element 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #we need to find the length 
        if head == None or head.next == None:
          return head
        count=0
        cur=head
        while(cur!=None):
            count+=1
            cur=cur.next

        # a dummy node 
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        nex=None
        while (count >= k):
            cur=prev.next
            nex=cur.next
            for i in range(1, k,1):
                cur.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=cur.next
            prev=cur
            count-=k
        return dummy.next
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        count=1
        if head == None or head.next == None:
          return head
        while(cur.next!=None):
            count+=1
            cur=cur.next
        if(k%count==0):
            return head
        cur.next=head #to mark last node to first
        k=k%count
        k=count-k
        print(count)
        while(k>0):
            cur=cur.next
            k-=1
        head=cur.next
        cur.next=None
        return head 
    
    def flattenLinkedList(root: Node) -> Node:
            if root == None or root.next == None:
                return root
            # recursion to find the end and end -1 node and combine it
            root.next = flattenLinkedList(root.next)
            # now merge
            root = mergeTwoLists(root, root.next)
            # return the root
            # it will be in turn merged with its left
            return root

    def mergeTwoLists(a, b):
        temp=Node(0,None,None)
        res=temp
        while (a!= None and b!= None):
            if (a.data < b.data):#compare it
                temp.child=a
                temp=temp.child
                a=a.child
            else:
                temp.child=b
                temp=temp.child
                b=b.child
        if (a!=None):
            temp.child=a
        else:
            temp.child=b
        return res.child    

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #step1 :to create a copy of a node and connect in middle
        #step2 :connect the random node as original
        #step3 :then discard the link
        itr=head
        front=head
        if head == None or head.next == None:
            return head
        while(itr!=None):
            front=itr.next
        copy=Node(itr.data)
        itr=front
        #step2
        itr=head
        while(itr!=None):
            if(itr.random!=None):
                itr.next.random=itr.random.next
            itr=itr.next.next
        #step3
        new=Node
        copy=new
        itr=head
        front=head
        while(itr!=None):
            front=itr.next.next
            copy.next=itr.next
            itr.next=front
            itr=itr.next
            copy=copy.next
        return new.next





    




    



            






ll=Linked_list()
ll.insertion(1)
ll.insertion(2)
ll.insertion(3)
ll.insertion(4)
print(ll.middleNode())
print(ll.delete_k_element(1))
print(ll.reverseList())

# [4] -> next = H
# [1, (none)]              ----------->
# None -> [4,(1)]-->[2,(3)]-->[2,(3)]->[3,(none)]->None
#                      C         
#                             P.next     C.next
# set node.next= head
# head = node
#  N -> H       H
#  H = N     