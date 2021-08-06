from linked_list.linked_list import Linked_list, Node
from forimp import Linked_list,Node

def zip_lists(first:Linked_list,second:Linked_list):
    var1 =first.head
    var2=second.head

    new=Linked_list()
    while True:
        if var1:
            new.append(var1.value)
            var1=var1.next

        if var2:
            new.append(var2.value)
            var2=var2.next

        if not var1 and not var2 :
            break

    return new



if __name__ == "__main__":
    first=Linked_list()
    second=Linked_list()
    first.append(11)
    first.append(12)
    first.append(13)
    first.append(14)

    second.append(21)
    second.append(22)
    second.append(23)
    second.append(24)

    new=zip_lists(first,second)
    print(new)
    sec=new.__str__
    print(sec)
