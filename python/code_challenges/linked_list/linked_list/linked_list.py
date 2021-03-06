class Node :
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list:
    def __init__(self,head=None):

        self.head=head


    def insert(self,value):

        # creating a new node in front of the Linked List
        new_node=Node(value)

        # node that comes next will become the head
        if self.head:
            new_node.next=self.head

        #Assign new_node to self.head
        self.head = new_node

    def includes(self, value):
        # define the head, which is the current variable
        # Return T/F if value is in the linked list or not

        current = self.head

        while (current) :
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):

        new_node = Node(value)
        current = self.head

        if current == None:
           current = new_node
        else:
            while current.next != None:
                current = current.next
        current.next = new_node


    def insert_before(self,value,new_value):
        node = Node(new_value)
        current_node=self.head
        if current_node.value==value:
             node.next = self.head
             self.head = node
        else:
            while current_node.next:
                if current_node.next.value==value:
                    node.next=current_node.next
                    current_node.next=node
                    break
                current_node=current_node.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def kthFromEnd(self,k):
        current = self.head
        if current == None:
            return ("Empty List")

        if k <= -1:
           return("Negative number not acceptable")
        values=[]
        while current:
            values =values+ [current.value]
            current = current.next
        print(values)
        try:

            return values[::-1][k]
        except IndexError:
            return ("out of index")



    def __str__(self):

        string = ''
        current = self.head
        while (current):
            string = string + f"{ { current.value } } -> "
            current = current.next
        else:
            string = string + 'Null'
        return string

def zipLists(list1, list2):

        current1 = list1.head
        current2 = list2.head
        new=Linked_list()
        while True:
            if current1 :
                new.append(current1.value)
                current1=current1.next
            if current2:
                new.append(current2.value)
                current2=current2.next

            if not current1 and not current2:
                break

        return new

if __name__ == "__main__":

    ll_one = Linked_list()
    ll_one.insert(1)
    ll_one.insert(5)
    ll_one.insert(7)
    ll_one.insert(9)
    print(ll_one)

    ll_two = Linked_list()
    ll_two.insert('a')
    ll_two.insert('b')
    ll_two.insert('c')
    ll_two.insert('d')
    print(ll_two)

    actual =zipLists(ll_one, ll_two)
    print(actual)
