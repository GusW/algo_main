from implementations.LinkedList import LinkedList


def middle_node(linked_list: LinkedList):
    fast_pointer, slow_pointer = linked_list.head, linked_list.head

    while fast_pointer.next_node and fast_pointer.next_node.next_node:
        slow_pointer = slow_pointer.next_node
        fast_pointer = fast_pointer.next_node.next_node

    return slow_pointer.data


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_start(100)
    linked_list.insert_start(1000)
    linked_list.insert_start(10000)
    linked_list.insert_start(100000)
    print(middle_node(linked_list))
