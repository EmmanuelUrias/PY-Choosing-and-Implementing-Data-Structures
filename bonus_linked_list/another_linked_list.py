def empty_list():
    return None


def prepend(data, linked_list):
    return (data, linked_list)


def is_empty(linked_list):
    return linked_list is None


linked_list = empty_list()
linked_list = prepend(3, linked_list)
linked_list = prepend(2, linked_list)
linked_list = prepend(1, linked_list)

if is_empty(linked_list):
    print('The linked list is empty')
else:
    current_node = linked_list
    while not is_empty(current_node):
        print(current_node[0])
        current_node = current_node[1]
