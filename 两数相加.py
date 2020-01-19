# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def reverseListNode(self, listnode):
        """列表反转"""
        pre, head = None, listnode
        length = 0
        while head is not None:
            
            next = head.next
            head.next = pre
            pre = head
            head = next
            length += 1
        
        return pre, length
        

    
    def print_listnode(self, listnode):
        while listnode:
            print listnode.val
            listnode = listnode.next
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # self.print_listnode(l1)
        # l1, l1_len = self.reverseListNode(l1)
        # l2, l2_len = self.reverseListNode(l2)
        
        # self.print_listnode(node)
        cur = None
        first = None
        while any([l1, l2]):
            if not cur:
                cur = ListNode(0)
                first = cur
            
            # 获取对应节点的值相加
            _sum = cur.val + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur_forward = _sum / 10  # 进位
            # 更新当前节点值
            cur.val = _sum % 10  # 当前节点值

            if (l1 and l1.next) or (l2 and l2.next):
                cur.next = ListNode(0)
            if cur_forward > 0:
                # 进位更新下级节点
                if cur.next:
                    cur.next = ListNode(cur.next.val + cur_forward)
                else:
                    cur.next = ListNode(cur_forward) 
            
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
            cur = cur.next

        return first
            
                 
        
        


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(5)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    # l1 = ListNode(0)
    # l2 = ListNode(0)
    
    # l1 = ListNode(5)
    # l2 = ListNode(5)
    
    
    
    print Solution().addTwoNumbers(l1, l2)
