from implementations.LinkedList import LinkedList


def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head
    while curr:
        next_ = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next_

    linked_list.head = prev
    return linked_list


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_start(100)
    linked_list.insert_start(1000)
    linked_list.insert_start(10000)
    linked_list.insert_start(100000)
    linked_list.traverse()
    print("----")
    print(reverse_linked_list(linked_list).traverse())
