# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = list_node_to_list(l1)
        l2_list = list_node_to_list(l2)

        result = function(l1_list, l2_list)

        return list_to_list_node(result)


def list_node_to_list(list_node: ListNode):
    result = []
    while True:
        result.append(list_node.val)
        if list_node.next is not None:
            list_node = list_node.next
        else:
            return result


def list_to_list_node(this_list: list):
    this_list.reverse()
    num = 0
    next_node = None
    while True:
        next_node = ListNode(val=this_list[num], next=next_node)
        num = num + 1
        if num == len(this_list):
            return next_node


def function(l1: list, l2: list):
    l_l1 = len(l1)
    l_l2 = len(l2)
    l_max = 0
    if l_l1 > l_l2:
        l_max = l_l1
        for i in range(0, l_l1 - l_l2):
            l2.append(0)
    else:
        l_max = l_l2
        for i in range(0, l_l2 - l_l1):
            l1.append(0)

    result = []
    for i in range(0, l_max):
        result.append(l1[i] + l2[i])

    result.append(0)

    for i in range(0, len(result)):
        if result[i] >= 10:
            result[i] = result[i] - 10
            result[i + 1] = result[i + 1] + 1

    last = len(result) - 1
    if result[last] == 0:
        result.pop(last)

    return result
