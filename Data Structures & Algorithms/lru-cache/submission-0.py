class Node:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.h={}
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key in self.h:
            node=self.h[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node=self.h[key]
            self.remove(node)
            self.insert(node)
            node.value=value
        else:
            if len(self.h)>=self.capacity:
                temp=self.tail.prev
                self.remove(temp)
                del self.h[temp.key]
            node=Node(key,value)
            self.h[key]=node
            self.insert(node)


    
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def insert(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next=node
        node.next.prev=node

        
